import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(app.quit)
        self.submit.clicked.connect(self.submit_btn)
    
    def submit_btn(self):
        # QMessageBox.about(self, "Submit", "Sumbit Wait")
        self.command.setText("Submit Message Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()