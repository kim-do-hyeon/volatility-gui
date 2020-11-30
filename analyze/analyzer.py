import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3
import pathlib


class Ui_VAGA(object):
    def setupUi(self, VAGA):
        VAGA.setObjectName("VAGA")
        VAGA.resize(1280, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        VAGA.setWindowIcon(icon)
        VAGA.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.tableWidget = QtWidgets.QTableWidget(VAGA)
        self.tableWidget.setGeometry(QtCore.QRect(100, 80, 1150, 370))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.file_path = QtWidgets.QTextBrowser(VAGA)
        self.file_path.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.file_path.setObjectName("file_path")
        
        self.select = QtWidgets.QPushButton(VAGA)
        self.select.setGeometry(QtCore.QRect(440, 10, 75, 31))
        self.select.setObjectName("select")

        self.analyze = QtWidgets.QPushButton(VAGA)
        self.analyze.setGeometry(QtCore.QRect(520, 10, 75, 31))
        self.analyze.setObjectName("analyze")

        self.pslist = QtWidgets.QPushButton(VAGA)
        self.pslist.setGeometry(QtCore.QRect(10, 80, 75, 24))
        self.pslist.setIcon(icon)
        self.pslist.setObjectName("pslist")

        self.psscan = QtWidgets.QPushButton(VAGA)
        self.psscan.setGeometry(QtCore.QRect(10, 110, 75, 24))
        self.psscan.setIcon(icon)
        self.psscan.setObjectName("psscan")

        self.pstree = QtWidgets.QPushButton(VAGA)
        self.pstree.setGeometry(QtCore.QRect(10, 140, 75, 24))
        self.pstree.setIcon(icon)
        self.pstree.setObjectName("pstree")
        
        self.info = QtWidgets.QPushButton(VAGA)
        self.info.setGeometry(QtCore.QRect(10, 170, 75, 24))
        self.info.setIcon(icon)
        self.info.setObjectName("info")

        self.cmdline = QtWidgets.QPushButton(VAGA)
        self.cmdline.setGeometry(QtCore.QRect(10, 200, 75, 24))
        self.cmdline.setIcon(icon)
        self.cmdline.setObjectName("cmdline")

        self.dlllist = QtWidgets.QPushButton(VAGA)
        self.dlllist.setGeometry(QtCore.QRect(10, 230, 75, 24))
        self.dlllist.setIcon(icon)
        self.dlllist.setObjectName("dlllist")

        self.log_report = QtWidgets.QLabel(VAGA)
        self.log_report.setGeometry(QtCore.QRect(10, 520, 640, 21))
        self.log_report.setObjectName("log_report")

        self.line = QtWidgets.QFrame(VAGA)
        self.line.setGeometry(QtCore.QRect(0, 500, 1281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #Button Click
        self.select.clicked.connect(self.callfile)
        self.analyze.clicked.connect(self.scan)
        self.pslist.clicked.connect(self.pslist_analyze)
        self.psscan.clicked.connect(self.psscan_analyze)
        self.pstree.clicked.connect(self.pstree_analyze)
        self.cmdline.clicked.connect(self.cmdline_analyze)
        self.dlllist.clicked.connect(self.dlllist_analyze)
        
        self.retranslateUi(VAGA)
        QtCore.QMetaObject.connectSlotsByName(VAGA)

    def retranslateUi(self, VAGA):
        _translate = QtCore.QCoreApplication.translate
        VAGA.setWindowTitle(_translate("VAGA", "VAGA - Volatility GUI Analyzer"))
        self.select.setText(_translate("VAGA", "Select"))
        self.analyze.setText(_translate("VAGA", "Analyze"))
        self.pslist.setText(_translate("VAGA", "pslist"))
        self.psscan.setText(_translate("VAGA", "psscan"))
        self.pstree.setText(_translate("VAGA", "pstree"))
        self.info.setText(_translate("VAGA", "info"))
        self.cmdline.setText(_translate("VAGA", "cmdline"))
        self.info.setText(_translate("VAGA", "info"))
        self.dlllist.setText(_translate("VAGA", "dlllist"))
        self.log_report.setText(_translate("VAGA", "Select DataBase File!!"))

    def pslist_analyze(self):
        self.log_report.setText("Selected Pslist!!")
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(len(pslist))

        for i in range(len(pslist)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(11):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()

        for j in range(len(pslist)):
            for i in range(11):
                self.tableWidget.setItem(j, i, item)
                item = QtWidgets.QTableWidgetItem()

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VAGA", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VAGA", "PPID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VAGA", "ImageFileName"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VAGA", "Offset"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("VAGA", "Threads"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("VAGA", "Handles"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("VAGA", "SessionID"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("VAGA", "Wow64"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("VAGA", "CreateTime"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("VAGA", "ExitTime"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("VAGA", "Dumped"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for j in range(len(pslist)):
            for i in range(11):
                item = self.tableWidget.item(j, i)
                item.setText(_translate("Dialog", str(pslist[j][i])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def psscan_analyze(self):
        self.log_report.setText("Selected Psscan!!")
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(len(psscan))

        for i in range(len(psscan)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(11):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()

        for j in range(len(psscan)):
            for i in range(11):
                self.tableWidget.setItem(j, i, item)
                item = QtWidgets.QTableWidgetItem()

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VAGA", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VAGA", "PPID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VAGA", "ImageFileName"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VAGA", "Offset"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("VAGA", "Threads"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("VAGA", "Handles"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("VAGA", "SessionID"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("VAGA", "Wow64"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("VAGA", "CreateTime"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("VAGA", "ExitTime"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("VAGA", "Dumped"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for j in range(len(pslist)):
            for i in range(11):
                item = self.tableWidget.item(j, i)
                item.setText(_translate("Dialog", str(psscan[j][i])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def pstree_analyze(self):
        self.log_report.setText("Selected Pstree!!")
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(len(psscan))

        for i in range(len(pstree)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(10):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()

        for j in range(len(pstree)):
            for i in range(10):
                self.tableWidget.setItem(j, i, item)
                item = QtWidgets.QTableWidgetItem()

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VAGA", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VAGA", "PPID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VAGA", "ImageFileName"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VAGA", "Offset"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("VAGA", "Threads"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("VAGA", "Handles"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("VAGA", "SessionID"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("VAGA", "Wow64"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("VAGA", "CreateTime"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("VAGA", "ExitTime"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for j in range(len(pstree)):
            for i in range(10):
                item = self.tableWidget.item(j, i)
                item.setText(_translate("Dialog", str(pstree[j][i])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)


    def cmdline_analyze(self):
        self.log_report.setText("Selected cmdline!!")
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(cmdline))

        for i in range(len(cmdline)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(3):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()

        for j in range(len(cmdline)):
            for i in range(3):
                self.tableWidget.setItem(j, i, item)
                item = QtWidgets.QTableWidgetItem()

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VAGA", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VAGA", "Process"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VAGA", "Args"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for j in range(len(cmdline)):
            for i in range(3):
                item = self.tableWidget.item(j, i)
                item.setText(_translate("Dialog", str(cmdline[j][i])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def dlllist_analyze(self):
        self.log_report.setText("Selected DLLlist!!")
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(len(dlllist))

        for i in range(len(dlllist)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(8):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()

        for j in range(len(dlllist)):
            for i in range(8):
                self.tableWidget.setItem(j, i, item)
                item = QtWidgets.QTableWidgetItem()

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VAGA", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VAGA", "Process"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("VAGA", "Base"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("VAGA", "Size"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("VAGA", "Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("VAGA", "Path"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("VAGA", "LoadTime"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("VAGA", "Dumped"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for j in range(len(dlllist)):
            for i in range(8):
                item = self.tableWidget.item(j, i)
                item.setText(_translate("Dialog", str(dlllist[j][i])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def callfile(self):
        self.log_report.setText("Selected DataBase!!")
        strFilter = "DataBase file (*.db) ;; All files (*.*)";
        fname = QFileDialog.getOpenFileName(filter=strFilter)
        self.file_path.setText(fname[0])
        path = pathlib.Path(fname[0])
        self.log_report.setText("File Path : {}".format(path))
        return path

    def scan(self):
        global pslist
        global psscan
        global pstree
        global cmdline
        global dlllist
        path = self.file_path.toPlainText()
        path = pathlib.Path(path)
        file_name = os.path.basename(path)
        self.log_report.setText("File Name : {}".format(file_name))
        conn = sqlite3.connect(file_name)
        cur = conn.cursor()
        cur.execute('select * from pslist')
        pslist = cur.fetchall()
        cur.execute('select * from psscan')
        psscan = cur.fetchall()
        cur.execute('select * from pstree')
        pstree = cur.fetchall()
        cur.execute('select * from cmdline')
        cmdline = cur.fetchall()
        cur.execute('select * from dlllist')
        dlllist = cur.fetchall()
        self.log_report.setText("Success Analyze")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VAGA = QtWidgets.QDialog()
    ui = Ui_VAGA()
    ui.setupUi(VAGA)
    VAGA.show()
    sys.exit(app.exec_())
