# text analyzer in python

from readability import Readability
import sys
from PySide6.QtCore import (QSize, Qt)
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QPlainTextEdit, QComboBox, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox)

def read_text(text, metric_type):
    pass

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Analyzer")
        column1 = QVBoxLayout()
        column2 = QVBoxLayout()
        row1 = QHBoxLayout()
        row1.addLayout(column1)
        row1.addLayout(column2)

        self.input_text = QPlainTextEdit()
        column1.addWidget(self.input_text)
        

        self.go_button = QPushButton("Analyze")
        column2.addWidget(self.go_button)

        self.input_metric = QComboBox()
        self.input_metric.addItems(["Flesch-Kinaid Grade Level", "Flesch Reading Ease", "Dale Chall Readability", "Automated Readability Index", "Coleman Liau Index", "Gunning Fog Index", "SMOG Index", "SPACHE Readability Formula", "Linsear Write"])
        column2.addWidget(self.input_metric)



        
        widget = QWidget()
        widget.setLayout(row1)
        self.setCentralWidget(widget)
    
application = QApplication(sys.argv)
window = Window()
window.show()
application.exec()