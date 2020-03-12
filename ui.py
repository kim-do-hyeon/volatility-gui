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
def timestamp(self):
    now = datetime.now()
    time = "{}{}{}{}{}{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
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

        # #Call Plugin
        # self.imageinfo_btn.clicked.connect(self.imageinfo)
        # self.cmdscan_btn.clicked.connect(self.cmdscan)
        # self.info_btn.clicked.connect(self.info)

        # self.pslist_btn.clicked.connect(self.pslist)
        # self.psscan_btn.clicked.connect(self.psscan)
        # self.pstree_btn.clicked.connect(self.pstree)

        # self.dlllist_btn.clicked.connect(self.dlllist)
        # self.handles_btn.clicked.connect(self.handles)
        # self.driverscan_btn.clicked.connect(self.driverscan)
        # self.cmdline_btn.clicked.connect(self.cmdline)

        self.plugin_list.currentIndexChanged.connect(self.pluginlist)

    def pluginlist(self):
        self.work.setText(self.plugin_list.currentText())

    def scan(self):
        path = self.file_path.toPlainText()
        path = pathlib.Path(path)
        
        print(timestamp(self) + " > [SCAN] Image Scan Path " + str(path), file = log)
        print(timestamp(self) + " > [SCAN] Image Scan Path " + str(path))
        
        self.Command.setText("File Scanning!")
        print(timestamp(self) + " > [SCAN] Scanning!", file = log)
        print(timestamp(self) + " > [SCAN] Scanning!")

        plugin = self.work.toPlainText()

        print(timestamp(self) + " > [SCAN] Plugin : " + plugin, file = log)
        print(timestamp(self) + " > [SCAN] Plugin : " + plugin)

        #Run Volatility With Subprocess
        volatility3 = os.getcwd() + "/volatility3/vol.py"
        shell = ['python', volatility3,'-f', str(path), plugin]
        fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
        data = fd_open.read().strip().decode('utf8')
        fd_open.close()

        save_log_path = 'plugin/init/' + plugin + '.txt'
        plugin_log = open(str(save_log_path),'w',-1,"utf-8")
        print (data, file = plugin_log)

        self.Command.setText(plugin + " Scanned!")
        print(timestamp(self) + " > [SCAN] " + plugin + "Scanned!", file = log)
        print(timestamp(self) + " > [SCAN] " + plugin + "Scanned!")

        self.Command_Result.setText(data)        

    #Call File Function
    def callfile(self):
        fname = QFileDialog.getOpenFileName(self)
        self.file_path.setText(fname[0])
        path = pathlib.Path(fname[0])
        print(timestamp(self) + " > [CALL FILE] Selected Image Path " + str(path), file = log)
        print(timestamp(self) + " > [CALL FILE] Selected Image Path " + str(path))
        return path

#------------------------------------------------------------------------------

#     #Plugin - imageinfo
#     def imageinfo(self):
#         print(timestamp(self) + " > [IMAGEINFO] imageinfo Selected!", file = log)
#         print(timestamp(self) + " > [IMAGEINFO] imageinfo Selected!")
#         self.work.setText('imageinfo')

#         #File Path Set
#         pwd = os.getcwd() + "\plugin\imageinfo\Extract_Image_information.py"
#         print(timestamp(self) + " > [IMAGEINFO] imageinfo manage : ", pwd, file = log)
#         print(timestamp(self) + " > [IMAGEINFO] imageinfo manage : ", pwd)

#         #Call Plugin
#         subprocess.call(["python", pwd])

#         #File Open
#         imageinfo_result_file = open('plugin/imageinfo/imageinfo_result.txt','r')

#         #Get Profile
#         # line = imageinfo_result_file.readlines()
#         # profile = line[5]
#         # self.os.setText(profile)

#         #Result Manage
#         Textstring = imageinfo_result_file.read()
#         self.Command_Result.setText(Textstring)

#         #File Close
#         imageinfo_result_file.close()      
        
# #------------------------------------------------------------------

#     #Plugin - cmdscan
#     def cmdscan(self):
#         cmdscan_result_file = open('plugin/cmdscan/cmdscan.txt','r')
#         Textstring = cmdscan_result_file.read()
#         self.Command_Result.setText(Textstring)
#         cmdscan_result_file.close()
#         self.work.setText('cmdscan')

# #--------------------------------------------------------------------

#     #Plugin - info
#     def info(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [INFO] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [INFO] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.info']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip().decode('utf8')
#         fd_open.close()
        
#         plugin_log = open('plugin/info/info.txt','w',-1,"utf-8")
#         print (data, file = plugin_log)

#         print(timestamp(self) + " > [INFO] Scanned!", file = log)
#         print(timestamp(self) + " > [INFO] Scanned!")

#         self.Command_Result.setText(data)

# #-------------------------------------------------------------------------------

#     #Plugin - psscan
#     def psscan(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [PSSCAN] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [PSSCAN] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.psscan']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip().decode('utf8')
#         fd_open.close()
        
#         plugin_log = open('plugin/psscan/psccan.txt','w',-1,"utf-8")
#         print (data, file = plugin_log)

#         print(timestamp(self) + " > [PSSCAN] Scanned!", file = log)
#         print(timestamp(self) + " > [PSSCAN] Scanned!")

#         self.Command_Result.setText(data)

# #-------------------------------------------------------------------------------

#     #plugin - pslist
#     def pslist(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [PSLIST] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [PSLIST] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.pslist']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip().decode('utf8')
#         fd_open.close()
        
#         plugin_log = open('plugin/pslist/pslist.txt','w',-1,"utf-8")
#         print (data, file = plugin_log)

#         print(timestamp(self) + " > [PSLIST] Scanned!", file = log)
#         print(timestamp(self) + " > [PSLIST] Scanned!")

#         self.Command_Result.setText(data)

# #---------------------------------------------------------------------------------

#     #plugin - pstree
#     def pstree(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [PSTREE] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [PSTREE] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.pstree']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip().decode('utf8')
#         fd_open.close()
        
#         plugin_log = open('plugin/pstree/pstree.txt','w',-1,"utf-8")
#         print (data, file = plugin_log)

#         print(timestamp(self) + " > [PSTREE] Scanned!", file = log)
#         print(timestamp(self) + " > [PSTREE] Scanned!")

#         self.Command_Result.setText(data)

# #----------------------------------------------------------------------------------------------
    
#     #plugin - dlllist
#     def dlllist(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [DLLLIST] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [DLLLIST] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.dlllist']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip().decode('utf8')
#         fd_open.close()
        
#         plugin_log = open('plugin/dlllist/dlllist.txt','w',-1,"utf-8")
#         print (data, file = plugin_log)

#         print(timestamp(self) + " > [DLLLIST] Scanned!", file = log)
#         print(timestamp(self) + " > [DLLLIST] Scanned!")

#         self.Command_Result.setText(data)

# #----------------------------------------------------------------------------------------------
    
#     #plugin - handles
#     def handles(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [HANDLES] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [HANDLES] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.handles']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip().decode('utf8')
#         fd_open.close()
        
#         plugin_log = open('plugin/handles/handles.txt','w',-1,"utf-8")
#         print (data, file = plugin_log)

#         print(timestamp(self) + " > [HANDLES] Scanned!", file = log)
#         print(timestamp(self) + " > [HANDLES] Scanned!")

#         self.Command_Result.setText(data)

# #----------------------------------------------------------------------------------------------
    
#     #plugin - driverscan
#     def driverscan(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [DRIVERSCAN] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [DRIVERSCAN] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.driverscan']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip().decode('utf8')
#         fd_open.close()
        
#         plugin_log = open('plugin/driverscan/driverscan.txt','w',-1,"utf-8")
#         print (data, file = plugin_log)

#         print(timestamp(self) + " > [DRIVERSCAN] Scanned!", file = log)
#         print(timestamp(self) + " > [DRIVERSCAN] Scanned!")

#         self.Command_Result.setText(data)

# #----------------------------------------------------------------------------------------------
    
#     #plugin - cmdline
#     def cmdline(self):
#         image = self.file_path.toPlainText()
#         image = pathlib.Path(image)

#         print(timestamp(self) + " > [CMDLINE] Image Scan Path " + str(image), file = log)
#         print(timestamp(self) + " > [CMDLINE] Image Scan Path " + str(image))

#         volatility3 = os.getcwd() + "/volatility3/vol.py"
#         shell = ['python', volatility3,'-f', str(image), 'windows.cmdline']
#         fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
#         data = fd_open.read().strip()
#         fd_open.close()
        
#         plugin_log = open('plugin/cmdline/cmdline.txt','w',-1,"utf-8")
#         print(data, file = plugin_log)
#         print(data)

#         print(timestamp(self) + " > [CMDLINE] Scanned!", file = log)
#         print(timestamp(self) + " > [CMDLINE] Scanned!")

#         self.Command_Result.setText(data)

#-------------------------------------------------------------------------------------

    #Exit
    def Exit(self):
        print(timestamp(self) + " > [EXIT] Exit! Bye", file = log)
        print(timestamp(self) + " > [EXIT] Exit! Bye")
        self.exit.clicked.connect(app.quit)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()