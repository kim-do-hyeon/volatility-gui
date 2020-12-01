import os
import sys
import pathlib
import sqlite3
import subprocess

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from . import plugin


ui = uic.loadUiType('res/analyzer.ui')[0]

class AnalyzerWindow(QWidget, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('res/icon.ico'))

        #Button Click
        self.select.clicked.connect(self.callfile)
        self.analyze.clicked.connect(self.scan)
        self.pslist.clicked.connect(self.pslist_analyze)
        self.psscan.clicked.connect(self.psscan_analyze)
        self.pstree.clicked.connect(self.pstree_analyze)
        self.info.clicked.connect(self.info_analyze)
        self.cmdline.clicked.connect(self.cmdline_analyze)
        self.dlllist.clicked.connect(self.dlllist_analyze)


    def pslist_analyze(self):
        if not 'pslist' in globals():
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return

        self.log_report.setText("Selected Pslist!!")
        _translate = QCoreApplication.translate
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(len(pslist))

        for i in range(len(pslist)):
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(11):
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()

        for j in range(len(pslist)):
            for i in range(11):
                self.tableWidget.setItem(j, i, item)
                item = QTableWidgetItem()

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
        if not 'psscan' in globals():
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
            
        self.log_report.setText("Selected Psscan!!")
        _translate = QCoreApplication.translate
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(len(psscan))

        for i in range(len(psscan)):
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(11):
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()

        for j in range(len(psscan)):
            for i in range(11):
                self.tableWidget.setItem(j, i, item)
                item = QTableWidgetItem()

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
        if not 'pstree' in globals():
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
            
        self.log_report.setText("Selected Pstree!!")
        _translate = QCoreApplication.translate
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(len(psscan))

        for i in range(len(pstree)):
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(10):
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()

        for j in range(len(pstree)):
            for i in range(10):
                self.tableWidget.setItem(j, i, item)
                item = QTableWidgetItem()

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

    def info_analyze(self):
        if not 'info' in globals():
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
            
        self.log_report.setText("Selected info!!")
        _translate = QCoreApplication.translate
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(info))

        for i in range(len(info)):
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(2):
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()

        for j in range(len(info)):
            for i in range(2):
                self.tableWidget.setItem(j, i, item)
                item = QTableWidgetItem()

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("VAGA", "Variable"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("VAGA", "Value"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for j in range(len(info)):
            for i in range(2):
                item = self.tableWidget.item(j, i)
                item.setText(_translate("Dialog", str(info[j][i])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)
    
    def cmdline_analyze(self):
        if not 'cmdline' in globals():
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
            
        self.log_report.setText("Selected cmdline!!")
        _translate = QCoreApplication.translate
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(cmdline))

        for i in range(len(cmdline)):
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(3):
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()

        for j in range(len(cmdline)):
            for i in range(3):
                self.tableWidget.setItem(j, i, item)
                item = QTableWidgetItem()

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
        if not 'dlllist' in globals():
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
            
        self.log_report.setText("Selected DLLlist!!")
        _translate = QCoreApplication.translate
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(len(dlllist))

        for i in range(len(dlllist)):
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(8):
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()

        for j in range(len(dlllist)):
            for i in range(8):
                self.tableWidget.setItem(j, i, item)
                item = QTableWidgetItem()

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
        if (path == ''):
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
            
        return path

    def scan(self):
        global pslist
        global psscan
        global pstree
        global info
        global cmdline
        global dlllist
        path = self.file_path.toPlainText()
        if (path == ''):
            QMessageBox.warning(self, 'Error', 'Please select an DB.', QMessageBox.Ok, QMessageBox.Ok)
            return
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
        cur.execute('select * from info')
        info = cur.fetchall()
        cur.execute('select * from cmdline')
        cmdline = cur.fetchall()
        cur.execute('select * from dlllist')
        dlllist = cur.fetchall()
        self.log_report.setText("Success Analyze")

