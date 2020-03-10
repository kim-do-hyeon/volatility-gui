from PyQt5.QtWidgets import *

class GUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        Name = QLabel("NAME")
        EditName = QLineEdit()
        ButtonOK = QPushButton("OK")
        ButtonCheck = QCheckBox("a")
        Widget = QListWidget()
        for i in range(5):
            item = QListWidgetItem("List %i" %i)
            Widget.addItem(item)

        layout = QVBoxLayout()
        layout.addWidget(Name)
        layout.addWidget(EditName)
        layout.addWidget(ButtonOK)
        layout.addWidget(ButtonCheck)
        layout.addWidget(Widget)

        self.setLayout(layout)
app = QApplication([])
dialog = GUI()
dialog.show()
app.exec()