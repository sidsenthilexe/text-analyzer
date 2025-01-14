# text analyzer in python

from readability import Readability
import sys
from PySide6.QtCore import (QSize, Qt)
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QPlainTextEdit, QComboBox, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Analyzer")
        layout = QHBoxLayout()

        self.input_text = QPlainTextEdit()
        layout.addWidget(self.input_text)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
application = QApplication(sys.argv)
window = Window()
window.show()
application.exec()