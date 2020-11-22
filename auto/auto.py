# -*- coding: utf-8 -*-
import os
import sys
import pathlib
import subprocess
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pathlib
import shutil

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


dir_path = os.getcwd() + '\\data'
shutil.rmtree(dir_path)
os.mkdir(os.getcwd() + '\\data')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(765, 220)
        Dialog.setMinimumSize(QtCore.QSize(765, 220))
        Dialog.setMaximumSize(QtCore.QSize(765, 220))
        self.file_path = QtWidgets.QTextBrowser(Dialog)
        self.file_path.setGeometry(QtCore.QRect(10, 10, 420, 30))
        self.file_path.setObjectName("file_path")
        self.select = QtWidgets.QPushButton(Dialog)
        self.select.setGeometry(QtCore.QRect(440, 10, 75, 30))
        self.select.setObjectName("select")
        self.analyze = QtWidgets.QPushButton(Dialog)
        self.analyze.setGeometry(QtCore.QRect(520, 10, 75, 30))
        self.analyze.setObjectName("analyze")
        self.db = QtWidgets.QPushButton(Dialog)
        self.db.setGeometry(QtCore.QRect(600, 10, 75, 30))
        self.db.setObjectName("DB")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(680, 10, 75, 30))
        self.exit.setAcceptDrops(False)
        self.exit.setObjectName("exit")
        self.log = QtWidgets.QTextBrowser(Dialog)
        self.log.setGeometry(QtCore.QRect(10, 50, 745, 160))
        self.log.setObjectName("LOG")


        self.select.clicked.connect(self.callfile)
        self.analyze.clicked.connect(self.scan)
        self.db.clicked.connect(self.db_store)
        self.exit.clicked.connect(app.quit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Volatility Auto Analyzer"))
        self.select.setText(_translate("Dialog", "Select"))
        self.analyze.setText(_translate("Dialog", "Analyze"))
        self.db.setText(_translate("Dialog", "DB Store"))
        self.exit.setText(_translate("Dialog", "EXIT"))
        self.log.setText(text)

    def callfile(self):
        strFilter = "Raw file (*.raw) ;; Memory file (*.mem) ;; All files (*.*)";
        fname = QFileDialog.getOpenFileName(filter=strFilter)
        self.file_path.setText(fname[0])
        path = pathlib.Path(fname[0])
        return path

    def scan(self):
        path = self.file_path.toPlainText()
        path = pathlib.Path(path)
        volatility3 = os.getcwd() + "/volatility3/vol.py"
        f = open('plugin_list.txt', 'r', encoding='utf-8')
        plugin_list = f.read().split()
        f.close()
        for i in plugin_list:
            print(i)
            shell = ['python', volatility3,'-f', path, i]
            fd_open = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
            data = fd_open.read().strip().decode('euc-kr')
            fd_open.close()
            save_path = os.getcwd() + '\\data\\'
            f = open(save_path + str(i) + '.txt','wb')
            f.write(data.encode('utf-8'))
            f.close()
        print("Success")
        
    def db_store(self):
        os.system("python auto_db_store.py")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
