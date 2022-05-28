import threading
import dns.resolver

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']


import sys
import time
from tkinter.filedialog import askdirectory
from tkinter import Tk
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import cv2
import os
import face_recognition as fr
from send_mail import send_mail
from ui_main_ui import *
from pymongo import MongoClient
from random import randint
import gridfs
from PIL import Image
import io
from winsound import Beep


encoded_data = []


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global main_folder_address

        Tk().withdraw()
        main_folder_address = askdirectory()

        with open('camera_number.txt','r') as f:
            self.camnum = f.read()

        self.camnum = int(self.camnum)
        
        print(self.camnum)

        
        # Run the camera
        self.timer = QTimer()
        self.timer.timeout.connect(self.showcam)
        self.controlTimer()

        self.temp_coords = ''
        self.unknown_coords = []

        self.tolerance = 0.5
        
        with open('theme.qss', 'r') as f:
            stylee = f.read()
            self.setStyleSheet(stylee)

        self.start_time = time.time()
        self.first_detected = True
        self.notification_sent = False
        self.display = False
        self.beepp = False
        self.loading = False

        # Connect to the server with the hostName and portNumber.
        connection = MongoClient("mongodb://manuroop:12345@cluster0-shard-00-00.5lkk2.mongodb.net:27017,cluster0-shard-00-01.5lkk2.mongodb.net:27017,cluster0-shard-00-02.5lkk2.mongodb.net:27017/?ssl=true&replicaSet=atlas-8nm0lt-shard-0&authSource=admin&retryWrites=true&w=majority")

        # Connect to the Database where the images will be stored.
        self.database = connection['main_db']
        
        self.ui.show_btn.clicked.connect(lambda:self.display_camera())
        self.ui.searcch_btn.clicked.connect(lambda:self.download_images())

        self.fill_list()
        self.beep()
        self.Update_enc()

    def fill_list(self):
        global main_folder_address

        for files in os.listdir(main_folder_address):
            files = files.lower()
            files = files.replace('.jpg','')
            files = files.replace('.jpeg','')
            files = files.replace('.png','')

            self.ui.listWidget.addItem(files)

    def beep(self):
        t = threading.Timer(1.0,self.beep)
        t.daemon = True
        t.start()

        if self.beepp:
            Beep(440, 500)

    def display_camera(self):
        txt = self.ui.show_btn.text()

        if txt == 'Show cam':
            self.ui.show_btn.setText('Hide cam')
            self.display = True
        else:
            self.ui.show_btn.setText('Show cam')
            self.display = False

    def Update_enc(self):
        """
        This section loads all existing pics from images folder in memory (RAM).

        It is necessary because it enhances detection and recognition speed.
        """

        global main_folder_address
        global encoded_data
    
        while main_folder_address == '':
            Tk().withdraw()
            main_folder_address = askdirectory()

        

        try:
            for images in os.listdir(main_folder_address):
                full_address = os.path.join(main_folder_address,images)
                img = cv2.imread(full_address)
                print('Loading '+str(full_address))
                coords = fr.face_encodings(img)
                encoded_data.append(coords)
        except:
            pass

    def showcam(self):
        """
        This method displays frame of given camera

        Camera input is taken by a timer
        """
        
        global main_folder_address, encoded_data


        # Getting frame from webcam
        _, self.image = self.cap.read()

        if self.display:
            cv2.imshow('Display',self.image)
        else:
            cv2.destroyAllWindows()


        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        found = self.recognize_img(self.image)

        coordss = fr.face_locations(self.image)

        # If it detects anyone, store their name in database
        if not found and coordss != []:
            
            if self.first_detected:
                self.first_detected = False
                self.start_time = time.time()
            
            current_time = time.time()
            print(current_time-self.start_time)


            if current_time-self.start_time >= 2 and not self.notification_sent:
                self.upload_image()
                print('Saved on database')
                self.notification_sent = True
                self.beepp = True

            if current_time-self.start_time >= 5:
                send_mail()
                print('Email sent')
                encoded_data.append(self.temp_coords)
                self.temp_coords = ''
                self.notification_sent = False
                self.start_time = time.time()
                os.system("shutdown -l")

        else:
            self.start_time = time.time()

    def upload_image(self):
        unique_id = 0
        while True:
            unique_id = randint(1,1000)
            col = self.database['fs.files']
            pre_stored_data = col.find()
            for p in pre_stored_data:
                if p['filename'] == str(unique_id):
                    continue

            break

        name_of_file = str(unique_id)

        img = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        
        cv2.imwrite('temp.jpg',img)
        #Create an object of GridFs for the above database.
        fs = gridfs.GridFS(self.database)
        
        file_path = 'temp.jpg'

        # Open the image in read-only format.
        with open(file_path, 'rb') as f:
            contents = f.read()

        #Now store/put the image via GridFs object.

        print('Uploading '+str(name_of_file))

        fs.put(contents, filename=name_of_file)
        os.remove('temp.jpg')

    def download_images(self):
        #Create an object of GridFs for the above database.
        fs = gridfs.GridFS(self.database)
        col = self.database["fs.files"]
        pre_stored_data = col.find()
        
        count = 0

        for p in pre_stored_data:
            data = fs.get_last_version(p["filename"]).read()
            print("Loading "+p["filename"])
            image = Image.open(io.BytesIO(data))
            image.save("images/"+p["filename"]+'.jpeg')
            count+=1

        self.msg('Information',str(count)+' images downloaded',QMessageBox.Information)

    def msg(self, titl,txt,icon):
        """
        This is a simple messagebox function.
        """
    
        msg = QMessageBox()
        msg.setWindowTitle(titl)
        msg.setText(txt)
        msg.setIcon(icon)
        msg.exec_()

    def controlTimer(self):
        """
        This method takes camera input for display
        # """

        self.cap = cv2.VideoCapture(self.camnum)
        self.timer.start(20)

    def recognize_img(self, main_pic):
        """
        This function takes an image and checks if it exists in database

        Database exists in the same folder called 'images'
        """

        global encoded_data

        target_encoding = fr.face_encodings(main_pic)

        # Declaring a dictionary to hold names and encodings of available data

        if target_encoding != []:

            for coords in encoded_data:

                for t in target_encoding:

                    result = fr.compare_faces( t, coords, tolerance=0.5)

                    for result_f in result:

                        if result_f:
                            
                            return True
            
            self.temp_coords = target_encoding
            return False 



if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())