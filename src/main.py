import os
import sys
import pathlib
import subprocess

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from . import plugin
from .util import *
from .analyzer import AnalyzerWindow
from .auto import AutoAnalyzer

log_file = open('log.txt', 'w', -1, 'utf-8')

def log(message):
    message = timestamp() + ' > ' + message
    print(message, file=log_file)
    print(message)

####################################

ui = uic.loadUiType('res/main.ui')[0]

default_message = 'Volatility GUI environment. Sourced By PENTAL \
        \n \
        \n 1. Mount the image first.\
        \n 2. After setting the plug-in, press the scan button.\
        \n 3. Click the EXIT button to exit. \
        \n \n \
        Update & issue https://github.com/kim-do-hyeon/Volaltility-gui \
        \n Thanks for your use this program. \
        \n If possible, I would appreciate it if you hit the star button on github. \
        \n \
        \n ###Logs are created only when they are normally shut down (click the Exit button).### \
        \n Linux Version will update later'


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('res/icon.ico'))
        
        # Button
        self.btn_image_open.clicked.connect(self.btn_image_open_click)
        self.btn_plugin_check.clicked.connect(self.btn_plugin_check_click)
        self.btn_plugin_uncheck.clicked.connect(self.btn_plugin_uncheck_click)
        # self.btn_plugin_check_linux.clicked.connect(self.btn_plugin_check_linux_click)
        # self.btn_plugin_uncheck_linux.clicked.connect(self.btn_plugin_uncheck_linux_click)
        self.btn_scan.clicked.connect(self.btn_scan_click)
        self.btn_save.clicked.connect(self.btn_save_click)
        self.btn_auto_analyze.clicked.connect(self.auto_analyze_click)
        self.btn_examine.clicked.connect(self.examine_click)
        self.btn_exit.clicked.connect(self.btn_exit_click)

        # Text
        self.txt_date.setText(timestamp())
        self.txt_result.setText(default_message)

        # Plugin List
        # self.list_plugins.itemClicked.connect(self.list_plugins_item_click)
        # self.list_plugins.itemDoubleClicked.connect(self.list_plugins_item_click)
        for plugin_name in plugin.__all__:
            item = QListWidgetItem()
            item.setText(plugin_name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            if (plugin_name in ['windows.cmdline', '1windows.filescan']): # for test
                item.setCheckState(Qt.Checked)
            self.list_plugins.addItem(item)
        
        # for plugin_name in plugin.__linux__:
        #     item = QListWidgetItem()
        #     item.setText(plugin_name)
        #     item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        #     item.setCheckState(Qt.Unchecked)
        #     if (plugin_name in ['linux.bash']): # for test
        #         item.setCheckState(Qt.Checked)
        #     self.list_plugins_linux.addItem(item)

        # Thread
        self.th_scan = ScanThread(self)
        self.th_scan.evt_result_append.connect(self.th_scan_result_handler)
        self.th_scan.evt_status_changed.connect(self.th_scan_status_handler)
        self.th_scan.evt_scan_finished.connect(self.th_scan_finish_handler)

    def examine_click(self):
        self.win_analyzer = AnalyzerWindow()
        self.win_analyzer.show()
    
    def auto_analyze_click(self):
        QMessageBox.information(self, 'Windows Memory', 'Only compatible with Windows Memeory \n #There are still many problems. We plan to update continuously.#', QMessageBox.Ok, QMessageBox.Ok)
        self.win_auto_analyzer = AutoAnalyzer()
        self.win_auto_analyzer.show()
        
    def list_plugins_item_click(self) :
        item = self.list_plugins.currentItem()
        print(item.text())
        if (item.checkState() == Qt.Checked):
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)


    def btn_image_open_click(self):
        file_filter = 'Raw file (*.raw) ;; Memory file (*.mem) ;; All files (*.*)'
        file_path = QFileDialog.getOpenFileName(self, 'Select Image', filter=file_filter)
        log('[FILE] Image Path: ' + file_path[0])
        self.txt_image_path.setText(file_path[0])


    def btn_plugin_check_click(self):
        for i in range(self.list_plugins.count()):
            self.list_plugins.item(i).setCheckState(Qt.Checked)


    def btn_plugin_uncheck_click(self):
        for i in range(self.list_plugins.count()):
            self.list_plugins.item(i).setCheckState(Qt.Unchecked)

    # def btn_plugin_check_linux_click(self):
    #     for i in range(self.list_plugins_linux.count()):
    #         self.list_plugins_linux.item(i).setCheckState(Qt.Checked)


    # def btn_plugin_uncheck_linux_click(self):
    #     for i in range(self.list_plugins_linux.count()):
    #         self.list_plugins_linux.item(i).setCheckState(Qt.Unchecked)

    def btn_scan_click(self):
        if not is_volatility_exists():
            reply = QMessageBox.question(self, 'No Library', 'Cannot find volatility3.\nWould you like to download it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return
            self.set_enabled(False)
            download_volatility()
            self.set_enabled(True)
            QMessageBox.information(self, 'Downloaded', 'Download Complete!', QMessageBox.Ok, QMessageBox.Ok)

        # Image Path
        image_path = self.txt_image_path.toPlainText()
        if (image_path == ''):
            QMessageBox.warning(self, 'Error', 'Please select an image.', QMessageBox.Ok, QMessageBox.Ok)
            return
        log('[SCAN] Image Path: ' + image_path)

        # Plugin
        selected_plugins = []
        for i in range(self.list_plugins.count()):
            item = self.list_plugins.item(i)
            if (item.checkState() == Qt.Checked):
                selected_plugins.append(item.text())
        if len(selected_plugins) == 0:
            QMessageBox.warning(self, 'Error', 'Please select at least one plugin.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # Case Name
        case_name = fix_file_name(self.txt_case_name.text()).strip()
        self.txt_case_name.setText(case_name)
        if (len(case_name) == 0):
            QMessageBox.warning(self, 'Error', 'Please enter the case name.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # Case Path
        case_path = 'case/' + case_name
        if not os.path.exists(case_path):
            os.makedirs(case_path)
            log_file = open('log.txt', 'w', -1, 'utf-8')
            log_file_path = 'case/' + case_name + '/log.txt'
            print("Log_File_Path : ", log_file_path)
        else:
            reply = QMessageBox.question(self, 'Case Exists', 'The same case name exists.\nWould you like to overwrite it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return
            remove_all_file(case_path)

        # Run Volatility
        self.txt_result.setText('Case: ' + case_name)
        self.txt_result.append('Image: ' + os.path.basename(image_path))
        self.set_enabled(False)
        self.th_scan.set_image_path(image_path)
        self.th_scan.set_case_path(case_path)
        self.th_scan.set_plugin_list(selected_plugins)
        self.th_scan.start()


    def th_scan_result_handler(self, message):
        self.txt_result.append(message)


    def th_scan_status_handler(self, message):
        self.lbl_status.setText(message)


    def th_scan_finish_handler(self):
        self.set_enabled(True)
        QMessageBox.information(self, 'Finished', 'Scan finished!', QMessageBox.Ok, QMessageBox.Ok)


    def set_enabled(self, enabled):
        self.lbl_case_name.setEnabled(enabled)
        self.lbl_date.setEnabled(enabled)
        self.lbl_image.setEnabled(enabled)
        self.txt_case_name.setEnabled(enabled)
        self.txt_date.setEnabled(enabled)
        self.txt_image_path.setEnabled(enabled)
        self.btn_image_open.setEnabled(enabled)
        self.btn_plugin_check.setEnabled(enabled)
        self.btn_plugin_uncheck.setEnabled(enabled)
        # self.btn_plugin_check_linux.setEnabled(enabled)
        # self.btn_plugin_uncheck_linux.setEnabled(enabled)
        self.btn_scan.setEnabled(enabled)
        self.btn_auto_analyze.setEnabled(enabled)
        self.btn_examine.setEnabled(enabled)
        self.btn_exit.setEnabled(enabled)
        self.list_plugins.setEnabled(enabled)
    
    def add_db(self):
        plugin = self.work.toPlainText()
        path = os.getcwd() + "/plugin/init/" + plugin + "/" + plugin + ".py"
        path = pathlib.Path(path)
        print(timestamp() + " > [ADD DB] Plugin : " + plugin, file = log)
        print(timestamp() + " > [ADD DB] Plugin : " + plugin)
        os.system('python ' + str(path))
        print(timestamp() + " > [ADD DB] Added DB!", file = log)
        print(timestamp() + " > [ADD DB] Added DB!")


    def save_log(self):
        txt = self.txt_result.toPlainText()
        savefilename = QFileDialog.getSaveFileName(self, "Save File", filter="*.txt")
        print(timestamp() + " > [SAVE LOG] Save Path " + savefilename[0], file = log)
        print(timestamp() + " > [SAVE LOG] Save Path " + savefilename[0])
        if savefilename[0] == "":
            QMessageBox.information(self, 'Error', 'Does not exist file name!', QMessageBox.Ok, QMessageBox.Ok)
            return
        f = open(savefilename[0],'wb')
        f.write(txt.encode())
        f.close()
        print(timestamp() + " > [SAVE LOG] Saved!", file = log)
        print(timestamp() + " > [SAVE LOG] Saved!")

    def btn_save_click(self) :
        txt = self.txt_result.toPlainText()
        savefilename = QFileDialog.getSaveFileName(self, "Save File", filter="*.txt")
        if savefilename[0] == "" :
            QMessageBox.information(self, 'Error', 'Does not exist file name!', QMessageBox.Ok, QMessageBox.Ok)
            return
        f = open(savefilename[0], 'wb')
        f.write(txt.encode())
        f.close()
        QMessageBox.information(self, 'Success', 'Save log successful!', QMessageBox.Ok, QMessageBox.Ok)


    def btn_exit_click(self):
        log('[EXIT] Exit! Bye')
        QCoreApplication.quit()

 
class ScanThread(QThread):
    evt_result_append = pyqtSignal(str)
    evt_status_changed = pyqtSignal(str)
    evt_scan_finished = pyqtSignal()
 
    def __init__(self, parent=None):
        super().__init__()
        self.plugins = None
        self.image_path = None
        self.case_path = None
        self.main = parent
 
    def set_plugin_list(self, plugins):
        self.plugins = plugins

    def set_image_path(self, path):
        self.image_path = path

    def set_case_path(self, path):
        self.case_path = path

    def run(self):
        start_time = timestamp()
        lib_path = get_volatility_path()

        for plugin_name in self.plugins:
            shell = ['python', lib_path, '-f', self.image_path, plugin_name]
            log('[SCAN] Current Plugin: ' + plugin_name)
            log('[SCAN] Run: ' + ' '.join(shell))
            self.evt_status_changed.emit('Scanning: ' + plugin_name)

            self.evt_result_append.emit('\n\n' + '=' * 80)
            self.evt_result_append.emit(plugin_name)
            self.evt_result_append.emit('=' * 80 + '\n')

            process = subprocess.Popen(shell, stdout=subprocess.PIPE).stdout
            global result
            result = process.read().strip().decode('euc-kr')
            result = result.replace('\r', '')
            result = result.split('\n', 2)[2]
            process.close()

            save_path = self.case_path + '/' + plugin_name + '.txt'
            plugin_log = open(save_path, 'w', -1, 'utf-8')
            print(result, file=plugin_log)

            self.evt_result_append.emit(result)
        
        self.evt_result_append.emit('\n' + '=' * 50)
        self.evt_result_append.emit('Scan started at ' + start_time)
        self.evt_result_append.emit('Scan finished at ' + timestamp() + '\n')

        self.evt_status_changed.emit('SCAN FINISHED!')
        self.evt_scan_finished.emit()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
