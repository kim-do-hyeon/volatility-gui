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
time = "{}{}{}{}{}{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
print("Init TIME : " + time, file = log)
print("Init TIME : " + time)

ui = uic.loadUiType("gui.ui")[0]

#Main Window
class MyWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))

        #File Path Call
        self.open_file_btn.clicked.connect(self.callfile)

        #Init Scan
        self.init_scan.clicked.connect(self.Init_Scan) #Scan

        #Scan, Cancel Button Call
        self.scan.clicked.connect(self.scan_btn) #Scan
        self.exit.clicked.connect(self.Exit) #Exit

        #Plugin Call
        self.imageinfo_btn.clicked.connect(self.imageinfo)
        self.cmdscan_btn.clicked.connect(self.cmdscan)
        self.pstree_btn.clicked.connect(self.pslist)


    #Call File Function
    def callfile(self):
        fname = QFileDialog.getOpenFileName(self)
        self.file_path.setText(fname[0])
        path = pathlib.Path(fname[0])
        print(" > [CALL FILE] Selected Image Path " + str(path), file = log)
        print(" > [CALL FILE] Selected Image Path " + str(path))
        return path

    #Init_Scan Button - Message
    #Imageinfo > Initial
    def Init_Scan(self):
        path = self.file_path.toPlainText()
        path = pathlib.Path(path)

        print(" > [INIT SCAN] Image Scan Path " + str(path), file = log)
        print(" > [INIT SCAN] Image Scan Path " + str(path))

        self.Command.setText("Init Scanning!")

        print(" > [INIT SCAN] Scanning!", file = log)
        print(" > [INIT SCAN] Scanning!")

        plugin = self.work.toPlainText()

        print(" > [INIT SCAN] Imageinfo Scan", file = log)
        print(" > [INIT SCAN] Imageinfo Scan")

        #Run Volatility With Subprocess
        shell = ['volatility_2.6_win64_standalone.exe','-f', str(path), 'imageinfo']
        fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
        data = fd_open.read().strip().decode('utf8')
        fd_open.close()

        imageinfo = open('plugin/init/init_info.txt','w',-1,"utf-8")
        print (data, file = imageinfo) #init_info(imageinfo) Save

        self.Command.setText("Scanned!")
        print(" > [INIT SCAN] Scanned!", file = log)
        print(" > [INIT SCAN] Scanned!")

        self.Command_Result.setText(data)

    #Scan
    def scan_btn(self):
        path = self.file_path.toPlainText()
        path = pathlib.Path(path)

        print(" > [SCAN] Image Scan Path " + str(path), file = log)
        print(" > [SCAN] Image Scan Path " + str(path))

        self.Command.setText("Scanning!")

        print(" > [SCAN] Scanning!", file = log)
        print(" > [SCAN] Scanning!")

        plugin = self.work.toPlainText()

        print(" > [SCAN] Plugin : " + plugin, file = log)
        print(" > [SCAN] Plugin : " + plugin)

        #Run Volatility With Subprocess
        shell = ['volatility_2.6_win64_standalone.exe','-f', str(path), plugin]
        fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
        data = fd_open.read().strip().decode('utf8')
        fd_open.close()

        plugin_log = open('plugin/init/plugin.txt','w',-1,"utf-8")
        print (data, file = plugin_log)

        self.Command.setText("Scanned!")
        print(" > [SCAN] Scanned!", file = log)
        print(" > [SCAN] Scanned!")

        self.Command_Result.setText(data)

#------------------------------------------------------------------------------

    #Plugin - imageinfo
    def imageinfo(self):
        print(" > [PLUGIN] imageinfo Selected!", file = log)
        print(" > [PLUGIN] imageinfo Selected!")
        self.work.setText('imageinfo')

        #File Path Set
        pwd = os.getcwd() + "\plugin\imageinfo\Extract_Image_information.py"
        print(" > [PLUGIN] imageinfo manage : ", pwd, file = log)
        print(" > [PLUGIN] imageinfo manage : ", pwd)

        #Call Plugin
        subprocess.call(["python", pwd])

        #File Open
        imageinfo_result_file = open('plugin/imageinfo/imageinfo_result.txt','r')

        #Get Profile
        line = imageinfo_result_file.readlines()
        profile = line[5]
        self.os.setText(profile)

        #Result Manage
        Textstring = imageinfo_result_file.read()
        self.Command_Result.setText(Textstring)

        #File Close
        imageinfo_result_file.close()

        
        
#--------------------PLUGIN----------------------------------------------#

    #Plugin - cmdscan
    def cmdscan(self):
        cmdscan_result_file = open('plugin/cmdscan/cmdscan.txt','r')
        Textstring = cmdscan_result_file.read()
        self.Command_Result.setText(Textstring)
        cmdscan_result_file.close()
        self.work.setText('cmdscan')

    #Plugin - pslist
    def pslist(self):
        pslist_result_file = open('plugin/pslist/pslist.txt','r')
        Textstring = pslist_result_file.read()
        self.Command_Result.setText(Textstring)
        pslist_result_file.close()
        self.work.setText('pslist')

    #Exit
    def Exit(self):
        print(" > [EXIT] Exit! Bye", file = log)
        print(" > [EXIT] Exit! Bye")
        self.exit.clicked.connect(app.quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()