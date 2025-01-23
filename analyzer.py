# text analyzer in python
from readability import Readability
import sys
import nltk
nltk.download('punkt_tab')

from PySide6.QtCore import (QSize, Qt)
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QPlainTextEdit, QComboBox, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox)

def read_text(text, metric_type):
    
    readability_analyze = Readability(text)

    match metric_type:
        case 'Flesch-Kincaid Grade Level':
            fk = readability_analyze.flesch_kincaid()
            score = fk.score
            grade_level = fk.grade_level
            ease, ages = 'N/A'
        case 'Flesch Reading Ease':
            f = readability_analyze.flesch()
            score = f.score
            ease = f.ease
            grade_level = f.grade_levels
            ages = 'N/A'
        case 'Dale Chall Readability':
            dc = readability_analyze.dale_chall()
            score = dc.score
            grade_level = dc.grade_levels
            ease, ages = 'N/A'
        case 'Automated Readability Index':
            ari = readability_analyze.ari()
            score = ari.score
            ages = ari.ages
            grade_level = ari.grade_levels
            ease = 'N/A'
        case 'Coleman Liau Index':
            cl = readability_analyze.coleman_liau()
            score = cl.score
            grade_level = cl.grade_level
            ease, ages = 'N/A'
        case 'Gunning Fog Index':
            gf = readability_analyze.gunning_fog()
            score = gf.score
            grade_level = gf.grade_level
            ease, ages = 'N/A'
        case 'SMOG Index':
            smog = readability_analyze.smog(all_sentences=True)
            score = smog.score
            grade_level = smog.grade_level
            ease, ages = 'N/A'
        case 'SPACHE Readability Formula':
            spache = readability_analyze.spache()
            score = spache.score
            grade_level = spache.grade_level
            ease, ages = 'N/A'
        case 'Linsear Write':
            lw = readability_analyze.linsear_write()
            score = lw.score
            grade_level = lw.grade_level
            ease, ages = 'N/A'

    word_count = len(text.split())
    char_count = len(text)
    
    print(score)
    print(grade_level)
    print(ease)
    print(ages)
    print(word_count)
    print(char_count)

def change_help_text(type):
       match type:
        case 'Flesch-Kincaid Grade Level':
            pass
        case 'Flesch Reading Ease':
            pass
        case 'Dale Chall Readability':
            pass
        case 'Automated Readability Index':
           pass
        case 'Coleman Liau Index':
            pass
        case 'Gunning Fog Index':
            pass
        case 'SMOG Index':
            pass
        case 'SPACHE Readability Formula':
            pass
        case 'Linsear Write':
            pass
    

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.type_select = QComboBox()
        self.type_select.addItems(['Flesch-Kincaid Grade Level', 'Flesch Reading Ease', 'Dale Chall Readability', 'Automated Readability Index', 'Coleman Liau Index', 'Gunning Fog Index', 'SMOG Index', 'SPACHE Readability Formula', 'Linsear Write'])
        layout.addWidget(self.type_select)
        #self.type_select.currentTextChanged(change_help_text(self.type_select.currentText))

        self.setLayout(layout)
    
    
        

class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle('Text Analyzer')
        column1 = QVBoxLayout()
        column2 = QVBoxLayout()
        row1 = QHBoxLayout()
        row1.addLayout(column1)
        row1.addLayout(column2)

        self.input_text = QPlainTextEdit()
        column1.addWidget(self.input_text)
        

        self.go_button = QPushButton('Analyze')
        column2.addWidget(self.go_button)
        self.go_button.clicked.connect(self.transfer_to_read)

        self.input_metric = QComboBox()
        self.input_metric.addItems(['Flesch-Kincaid Grade Level', 'Flesch Reading Ease', 'Dale Chall Readability', 'Automated Readability Index', 'Coleman Liau Index', 'Gunning Fog Index', 'SMOG Index', 'SPACHE Readability Formula', 'Linsear Write'])
        column2.addWidget(self.input_metric)
        
        self.help_button = QPushButton('Help')
        column2.addWidget(self.help_button)
        self.help_button.clicked.connect(self.show_help_window)
        
        widget = QWidget()
        widget.setLayout(row1)
        self.setCentralWidget(widget)
    
    def transfer_to_read(self):
        self.input_metric.blockSignals(True)
        input_text_transfer = self.input_text.toPlainText()
        input_metric_transfer = self.input_metric.currentText()

        read_text(input_text_transfer, input_metric_transfer)
    
    def show_help_window(self, checked):
        global transfer_window
        transfer_window = HelpWindow()
        transfer_window.show()



application = QApplication(sys.argv)
window = Window()
window.show()
application.exec()