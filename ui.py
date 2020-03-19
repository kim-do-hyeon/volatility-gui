import os
import sys
import pathlib
import subprocess
import plugin
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Record Log
log = open('vol_log.txt','w',-1,"utf-8")

#Time Stamp
def timestamp(self):
    now = datetime.now()
    time = "{}{}{}{}{}{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second) #timestamp 형식
    return time

ui = uic.loadUiType("gui.ui")[0]

#Main Window
class MyWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))

        #Call File Path
        self.open_file_btn.clicked.connect(self.callfile)

        #Call Scan, Cancel Button
        self.exit.clicked.connect(self.Exit) #Exit
        self.scan_vol3.clicked.connect(self.scan) #Scan

        #Call Save log, Add DB
        self.save_log_btn.clicked.connect(self.save_log)
        self.add_db_btn.clicked.connect(self.add_db)

        #Call Plugin
        self.plugin_list.currentIndexChanged.connect(self.pluginlist)

    #Call Plugin List
    def pluginlist(self):
        self.work.setText(self.plugin_list.currentText())

    #Scan
    def scan(self):
        path = self.file_path.toPlainText()
        path = pathlib.Path(path)
        
        print(timestamp(self) + " > [SCAN] Image Scan Path " + str(path), file = log)
        print(timestamp(self) + " > [SCAN] Image Scan Path " + str(path))
        
        self.Command.setText("File Scanning!")
        print(timestamp(self) + " > [SCAN] Scanning!", file = log)
        print(timestamp(self) + " > [SCAN] Scanning!")

        plugin = self.work.toPlainText() #Call Plugin Text

        print(timestamp(self) + " > [SCAN] Plugin : " + plugin, file = log)
        print(timestamp(self) + " > [SCAN] Plugin : " + plugin)
    
        #Run Volatility With Subprocess
        volatility3 = os.getcwd() + "/volatility3/vol.py"
        
        shell = ['python', volatility3,'-f', str(path), plugin]
        fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
        data = fd_open.read().strip().decode('euc-kr')
        fd_open.close()

        save_log_path = 'plugin/init/' + plugin + '/' + plugin + '.txt'
        plugin_log = open(str(save_log_path),'w',-1,"utf-8")
        print (data, file = plugin_log)

        self.Command.setText(plugin + " Scanned!")
        print(timestamp(self) + " > [SCAN] " + plugin + "Scanned!", file = log)
        print(timestamp(self) + " > [SCAN] " + plugin + "Scanned!")
        data = data.replace('Volatility 3 Framework 1.0.0-beta.1','')
        self.Command_Result.setText(data)

    #Call File Function
    def callfile(self):
        fname = QFileDialog.getOpenFileName(self) 
        self.file_path.setText(fname[0])
        path = pathlib.Path(fname[0])
        print(timestamp(self) + " > [CALL FILE] Selected Image Path " + str(path), file = log)
        print(timestamp(self) + " > [CALL FILE] Selected Image Path " + str(path))
        return path

    #Add Db
    def add_db(self):
        plugin = self.work.toPlainText()
        path = os.getcwd() + "/plugin/init/" + plugin + "/" + plugin + ".py"
        path = pathlib.Path(path)
        print(timestamp(self) + " > [ADD DB] Plugin : " + plugin, file = log)
        print(timestamp(self) + " > [ADD DB] Plugin : " + plugin)
        os.system('python ' + str(path))
        print(timestamp(self) + " > [ADD DB] Added DB!", file = log)
        print(timestamp(self) + " > [ADD DB] Added DB!")


    #Save Log
    def save_log(self):
        print('save_log')


    #Exit
    def Exit(self):
        print(timestamp(self) + " > [EXIT] Exit! Bye", file = log)
        print(timestamp(self) + " > [EXIT] Exit! Bye")
        self.exit.clicked.connect(app.quit)

#Call Ui
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()