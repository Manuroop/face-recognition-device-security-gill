# face-recognition-device-security

*The repo contains two branches, in main branch the code signs out of windows where the processes shut down and in main-2 branch the code just locks the windows and no processes shut down. Locking windows is better as the processes do not shut down but the intruder is locked out of the system*

*WINDOWS SIGNS OUT IN THE BRANCH main*

INTRODUCTION

This is a project on Face Recognition done for the Microsoft Engage Program. The purpose of this desktop application is to provide device security and prevent anyone from using the laptop and tampering with it. This application has been made using Python and the OpenCV technology.

The application prevents anyone from using the laptop who doesn't have access to it. If the owner or anyone with access has left the laptop unattended and someone tries to interfer with it, then the app will save the photo of the intruder to MongoDB database in 2 seconds and in 5 seconds it will send a notification on email, and will sign out of windows, locking it so only people with the password can continue to use it.

IMPLEMENTATION and REQUIREMENTS

This app has been made on Python version 3.8.1.

- Download cmake - CMake is an open-source, cross-platform family of tools designed to build, test and package software
  https://cmake.org/download/
- Download and install Visual Studio with Desktop Development in C++ (required to use and install Face Recognition libraries), Visual Studio Code (with the Python extension) or any other IDE you are comfortable with.

- Now, in Python you need to install certain libraries/modules using these commands in cmd or vs code or powershell, wherever you are comfortable.
  
  pip install pyqt5
  
  pip install pyside2
  
  pip install cmake
  
  pip install dlib
  
  pip install yagmail
  
  pip install pillow
  
  pip install pymongo
  
  pip install dnspython
  
  pip install opencv-python
  
  pip install face_recognition

- In info.txt, change the email from 'manuroop678@gmail.com' to your email where you want to recieve the notification. Don't change the manuroop6789@gmail.com as it contains the database and collections in MongoDB.
- If you have multiple cameras on your device then you can change your camera number in camera_number.txt from 0 to whatever number you want.


The code should run perfectly after this.

FEATURES

- The application saves the intruder's photo to the database after 2 seconds.
- It sends an email notification after 5 seconds.
- It locks and signs out of windows after 5 seconds.
- There is a button in the app from where all the photos of the intruders can be downloaded from the MongoDB database.
- You can give access to multiple people who can use the laptop.

- The apps UI/UX is completely responsive, all contents inside the app resize themselves according to windows size.
- Most libraries are built in making it less resource consuming.
- It has high detection and recognition accuracy, it can detect multiple faces as well.
- It has a stable UI and a fast detection speed.
- Moreover, it is easy to use.

FUTURE GOALS

The app in future can be used at a big scale. The photo that was saved to the database can be put in the company's or university's or school's database to check and know the details of the intruder. 

A beep can be added that if the intruder commes then the laptop starts beeping so that everyone around knows that the laptop/computer is being interefered with. I tried adding it but the code needs to be altered a little for it to work.

If ever, the app starts malfunctioning and the recognition fails by any chance then there should be a password with which the app knows the person using the laptop is not an intruder and has access to it.


