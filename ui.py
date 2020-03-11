import os
import sys
import pathlib
import subprocess
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Record Log
log = open('vol_log.txt','w',-1,"utf-8")

#Time Stamp
now = datetime.now()
time = "{}/{}/{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
print("Init TIME : " + time, file = log)
print("Init TIME : " + time)

# print("Init TIME : " + time , file=log)
ui = uic.loadUiType("gui.ui")[0]

#Main Window
class MyWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))

        #File Path Call
        self.open_file_btn.clicked.connect(self.callfile)

        #Scan, Cancel Button Call
        self.scan.clicked.connect(self.scan_btn) #Scan
        self.exit.clicked.connect(self.Exit) #Exit
        
        #Plugin Call
        self.imageinfo_btn.clicked.connect(self.imageinfo)
        self.cmdscan_btn.clicked.connect(self.cmdscan)
        self.pstree_btn.clicked.connect(self.PluginButtonClicked)

        #ProgressBar Call
        self.progressBar.valueChanged.connect(self.progress)
    
    #Call File Function
    def callfile(self):
        fname = QFileDialog.getOpenFileName(self)
        self.file_path.setText(fname[0])
        path = pathlib.Path(fname[0])
        print(time + " > [CALLFILE] Selected Image Path " + str(path), file = log)
        print(time + " > [CALLFILE] Selected Image Path " + str(path))
        return path

    #Scan Button - Message
    def scan_btn(self):
        path = self.file_path.toPlainText()
        path = pathlib.Path(path)
        print(time + " > [SCAN] Image Scan Path " + str(path), file = log)
        print(time + " > [SCAN] Image Scan Path " + str(path))
        self.Command.setText("Scanning!")
        print(time + " > [SCAN] Scanning!", file = log)
        print(time + " > [SCAN] Scanning!")
        subprocess.run(['volatility_2.6_win64_standalone.exe','-f', str(path),'imageinfo', '> ./imageinfo/imageinfo.txt'], shell=True, check=True)
        self.Command.setText("Scanned!")
        print(time + " > [SCAN] Scanned!", file = log)
        print(time + " > [SCAN] Scanned!")

    def progress(self):
            self.progressBar.setValue(100)

    #Plugin Call - Message // Soon Delete
    def PluginButtonClicked(self):
        msg = ""
        if self.imageinfo_btn.isChecked():
            msg = "Selected Imageinfo"
            print(time + " > [IMAGEINFO] " + msg, file = log)
        elif self.cmdscan_btn.isChecked():
            msg = "Selected Cmdscan"
            print(time + " > [CMDSCAN] " + msg, file = log)
        elif self.pstree_btn.isChecked():
            msg = "Selected Pstree"
            print(time + " > [PSTREE] " + msg, file = log)
        self.statusbar.showMessage(msg + "!")
    #-------------------------------------------------------

    #Plugin - imageinfo
    def imageinfo(self):
        msg = ""
        imageinfo_result_file = open('imageinfo/image.txt','r')
        Textstring = imageinfo_result_file.read()
        self.Command_Result.setText(Textstring)
        imageinfo_result_file.close()
        self.statusbar.showMessage("Selected imageinfo!")

    #Plugin - cmdscan
    def cmdscan(self):
        msg = ""
        cmdscan_result_file = open('cmdscan/cmdscan.txt','r')
        Textstring = cmdscan_result_file.read()
        self.Command_Result.setText(Textstring)
        cmdscan_result_file.close()
        self.statusbar.showMessage("Selected Cmdscan!")

    #Exit
    def Exit(self):
        print(time + " > [EXIT] Exit! Bye", file = log)
        print(time + " > [EXIT] Exit! Bye")
        self.exit.clicked.connect(app.quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()