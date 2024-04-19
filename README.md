# Smart Vision Attendance System 📸

Welcome to the Smart Vision Attendance System! This innovative project leverages the ESP32-CAM module and Python programming to implement a smart attendance system based on facial recognition technology. This solution is designed to enhance efficiency in recording attendance in educational or workplace environments with the convenience of automated systems.
![Final Output](/Screenshot%20from%202024-04-18%2000-08-11.png)
## Features 🚀

- **Real-time Facial Recognition**: Identifies faces quickly and accurately from a live video feed.
- **Attendance Logging**: Automatically logs the attendance with timestamps for each recognized individual.
- **Easy Integration**: Can be integrated with existing infrastructures without significant modifications.
- **Cost-effective**: Utilizes affordable hardware components, making it accessible for budget-conscious environments.

## Hardware Requirements 🛠️

- **ESP32-CAM Module**: A small camera module capable of running independently as a small system.
- **A Computer with Python Installed**: A system with Python 3.x installed to run the facial recognition script.
- **Stable Internet Connection**: Required for both the ESP32-CAM and the computer to communicate effectively.

## Setup Instructions 🔧

### Setting Up the ESP32-CAM

1. **Connect** the ESP32-CAM to your computer using an FTDI programmer.
2. **Upload the Arduino Code**: Open the provided Arduino file `ESP32-CAM_Code.ino` in the Arduino IDE.
3. **Configure WiFi Settings**:
   ```cpp
   const char* WIFI_SSID = "your_wifi_ssid";
   const char* WIFI_PASS = "your_wifi_password";

    Replace your_wifi_ssid and your_wifi_password with your actual WiFi credentials.
4. Upload the Firmware: Ensure GPIO 0 is grounded only during the firmware upload. After uploading, reset the ESP32-CAM by disconnecting GPIO 0.

    Obtain IP Address: After the ESP32-CAM connects to the WiFi, it will display its assigned IP address in the Serial Monitor.

##Configuring the Python Script

    Configure the IP Address: Update the url variable in the project.py script with the IP address shown in the ESP32-CAM's Serial Monitor:

    python

url = 'http://<ESP32_IP>/cam-hi.jpg'

##Install Python Dependencies:

bash

    pip install numpy opencv-python face_recognition urllib3

##Running the System

Execute the project.py script to start the system. The script processes images from the ESP32-CAM, recognizes faces, and logs attendance in a CSV file.
Contributing

## Uploading Code to ESP32-CAM

Here is a screenshot of the code being uploaded to the Arduino IDE for the ESP32-CAM:

![Uploading Code](/toupload.jpeg)


Your contributions are welcome! Please feel free to fork the repository, make improvements, and submit pull requests.
## Acknowledgements

Thank you for your interest in the Smart Vision Attendance System. This project was made possible by the contributions of numerous individuals and the open-source community.
License

This project is licensed under the MIT License - see the LICENSE.md file for details
