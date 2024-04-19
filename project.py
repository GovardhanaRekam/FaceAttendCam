import cv2
import numpy as np
import os
import face_recognition
import urllib.request
import csv
from datetime import datetime

# Replace the URL with your ESP32-CAM's stream URL
url = 'http://192.168.43.100/cam-hi.jpg'

# Path to directory containing known images
path = '/home/amma/Desktop/img_id'

# Load known images and their encodings
images = []
classNames = []
classIDs = []  # For storing IDs
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    name_id = os.path.splitext(cl)[0].split('_')  # Assuming 'name_id' format
    classNames.append(name_id[0])
    classIDs.append(name_id[1])

# Function to find encodings of known images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError as e:
            print(f"Unable to encode {img}: {e}")
    return encodeList

encodeListKnown = findEncodings(images)

# Set threshold for face recognition
threshold = 0.7

# CSV file to store recognized faces
csv_filename = 'recognized_faces.csv'
csv_header = ['Name', 'ID', 'Timestamp']

# Function to append recognized face to CSV file
def append_to_csv(name, id):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, id, datetime.now()])

# Create or append to CSV file with header
if not os.path.exists(csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_header)

while True:
    # Read image from the ESP32-CAM stream
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)

    # Convert image to RGB for face recognition
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect faces in the current frame
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < threshold:
            name = classNames[matchIndex].upper()
            id = classIDs[matchIndex]
            append_to_csv(name, id)  # Append recognized face to CSV file

            # Draw rectangle around the face and display name and ID
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f"{name} {id}", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        else:
            # Optionally handle unknown faces
            pass

    # Display the frame
    cv2.imshow('ESP32-CAM Stream', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()

