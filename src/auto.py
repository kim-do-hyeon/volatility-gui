# -*- coding: utf-8 -*-
import os
import sys
import pathlib
import subprocess
import sqlite3
import pathlib
import shutil

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from . import plugin

print("                                                                                        ")
print(" #     #  ####  #        ##   ##### # #      # ##### #   #                              ")
print(" #     # #    # #       #  #    #   # #      #   #    # #                               ")
print(" #     # #    # #      #    #   #   # #      #   #     #                                ")
print("  #   #  #    # #      ######   #   # #      #   #     #                                ")
print("   # #   #    # #      #    #   #   # #      #   #     #                                ")
print("    #     ####  ###### #    #   #   # ###### #   #     #                                ")
print("                                                                                        ")
print("                                                                                        ")
print("   # #   #    # #####  ####       # #   #    #   ##   #      #   # ###### ###### #####  ")
print("  #   #  #    #   #   #    #     #   #  ##   #  #  #  #       # #      #  #      #    # ")
print(" #     # #    #   #   #    #    #     # # #  # #    # #        #      #   #####  #    # ")
print(" ####### #    #   #   #    #    ####### #  # # ###### #        #     #    #      #####  ")
print(" #     # #    #   #   #    #    #     # #   ## #    # #        #    #     #      #   #  ")
print(" #     #  ####    #    ####     #     # #    # #    # ######   #   ###### ###### #    # ")

text = 'Volatility Auto GUI environment. Sourced By PENTAL \
        \n \
        \n 1. Mount the image first.\
        \n 2. press the Analyze button.\
        \n 3. If Process finished, Click the DB Store button to check the result and add the database frame. \
        \n 4. Click the EXIT button to exit. \
        \n \n \
        Update & issue https://github.com/kim-do-hyeon/Volaltility-gui \
        \n Thanks for your use this program. \
        \n If possible, I would appreciate it if you hit the star button on github.'


dir_path = os.getcwd() + '\\src\\data'
shutil.rmtree(dir_path)
os.mkdir(os.getcwd() + '\\src\\data')

ui = uic.loadUiType('res/auto.ui')[0]

class AutoAnalyzer(QWidget, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('res/icon.ico'))

        #Button Click
        self.btn_select.clicked.connect(self.callfile)
        self.btn_analyze.clicked.connect(self.btn_scan_click)
        self.btn_db_store.clicked.connect(self.btn_db_store_click)
        self.btn_exit.clicked.connect(self.btn_exit_click)

    def callfile(self):
        strFilter = "Raw file (*.raw) ;; Memory file (*.mem) ;; All files (*.*)";
        fname = QFileDialog.getOpenFileName(filter=strFilter)
        self.file_path.setText(fname[0])
        path = pathlib.Path(fname[0])
        if (path == ''):
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
            
        return path

    def btn_scan_click(self):
        path = self.file_path.toPlainText()
        if (path == ''):
            QMessageBox.warning(self, 'Error', 'Please select an image.', QMessageBox.Ok, QMessageBox.Ok)
            return
        path = pathlib.Path(path)
        volatility3 = os.getcwd() + "/lib/volatility3-master/vol.py"
        plugin_list = []
        for plugin_name in plugin.__all__:
            plugin_list.append(plugin_name)
        try :
            for i in plugin_list:
                print(i)
                shell = ['python', volatility3,'-f', path, i]
                fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
                data = fd_open.read().strip().decode('euc-kr')
                fd_open.close()
                save_path = os.getcwd() + '\\src\\data\\'
                f = open(save_path + str(i) + '.txt','wb')
                f.write(data.encode('utf-8'))
                f.close()
        except :
            QMessageBox.warning(self, 'Error', 'Error. Please Retry', QMessageBox.Ok, QMessageBox.Ok)
            return
        QMessageBox.information(self, 'Success', 'Success Analyze, Open Examiner and Analyze Memory', QMessageBox.Ok, QMessageBox.Ok)
        return
        

    def btn_db_store_click(self):
        try :
            path = os.getcwd() + '\src/auto_db_store.py'
            path = pathlib.Path(path)
            db_store_run = 'python ' + str(path)
            os.system(db_store_run)
            QMessageBox.warning(self, 'Success', 'Success DB Store', QMessageBox.Ok, QMessageBox.Ok)
        except :
            QMessageBox.warning(self, 'Error', 'Does the auto_db_store.py file exist?', QMessageBox.Ok, QMessageBox.Ok)
            return
        

    def btn_exit_click(self): 
        QCoreApplication.quit()