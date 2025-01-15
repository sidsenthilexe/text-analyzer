# text analyzer in python

from readability import Readability
import sys
from PySide6.QtCore import (QSize, Qt)
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QPlainTextEdit, QComboBox, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Analyzer")
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()

        self.input_text = QPlainTextEdit()
        layout1.addWidget(self.input_text)
        layout2.addLayout(layout1)

        self.go_button = QPushButton("Analyze")
        layout2.addWidget(self.go_button)


        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)
    
application = QApplication(sys.argv)
window = Window()
window.show()
application.exec()