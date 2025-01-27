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
        case 'Spache Readability Formula':
            spache = readability_analyze.spache()
            score = spache.score
            grade_level = spache.grade_level
            ease, ages = 'N/A'
        case 'Linsear Write':
            lw = readability_analyze.linsear_write()
            score = lw.score
            grade_level = lw.grade_level
            ease, ages = 'N/A'
        case _:
            score. grade_level, ease, ages = 'N/A'

    word_count = len(text.split())
    char_count = len(text)

    print(score)
    print(grade_level)
    print(ease)
    print(ages)
    print(word_count)
    print(char_count)

    output = [score, grade_level, ease, ages, word_count, char_count]

    return output

    

def change_help_text(type):
    match type:
        case 'Flesch-Kincaid Grade Level':
            help_text = 'Flesch-Kincaid is based on the length of words and sentences in the text.\nIt is based off grade levels in terms of the American education system.'
        case 'Flesch Reading Ease':
            help_text = 'Flesch Reading Ease scores a text from 1-100 based on sentence and word lengths.\nScoring between 70 and 80 is roughly equivalent to an 8th grade level.'
        case 'Dale Chall Readability':
            help_text = 'Dale Chall Readability utilises a list of 3,000 common words to calculate\nthe amount of difficult words in a text. A score of 6-7 is easily understood\nby a 7th or 8th grader.'
        case 'Automated Readability Index':
            help_text = 'The ARI uses a factor of characters per word, and the score is approximately\nthe grade level needed to understand the text.'
        case 'Coleman Liau Index':
            help_text = 'The Coleman Liau Index uses the average number of letters and sentences per 100\nwords to approximate the grade level needed to understand the text.'
        case 'Gunning Fog Index':
            help_text = 'The Gunning Fog Index attempts to estimate the number of years of education\nnecessary to understand a text based on average sentence length and the number\nof complex words.'
        case 'SMOG Index':
            help_text = 'The SMOG Index estimates the number of years of education necessary to understand\na text based on the number of words with more than 2 syllables.'
        case 'Spache Readability Formula':
            help_text = 'The Spache Readability Formula compares a set of common words to\nthe words in a text. The score is calculated based on the number of words per sentence\nand the percentage of unfamiliar words.'
        case 'Linsear Write':
            help_text = 'Linsear Write estimates the grade level of a text based on sentence length and the\nnumber of words with 2 or more syllables.'
        case _ :
            help_text = 'hi'
    return help_text

class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Analyzer Help')

        layout = QVBoxLayout()
        self.type_select = QComboBox()
        self.type_select.addItems(['Flesch-Kincaid Grade Level', 'Flesch Reading Ease', 'Dale Chall Readability', 'Automated Readability Index', 'Coleman Liau Index', 'Gunning Fog Index', 'SMOG Index', 'Spache Readability Formula', 'Linsear Write'])
        layout.addWidget(self.type_select)
        
        help_output = change_help_text(self.type_select.currentText)
        self.help_output_text = QLabel()
        self.help_output_text.setText('Flesch-Kincaid is based on the length of words and sentences in the text.\nIt is based off grade levels in terms of the American education system.')
        layout.addWidget(self.help_output_text)

        self.setLayout(layout)
        self.type_select.currentTextChanged.connect(self.help_text_update)

    def help_text_update(self):
        help_input = self.type_select.currentText()
        help_output = change_help_text(help_input)
        self.help_output_text.setText(str(help_output))
    
    
        

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

        self.input_metric = QComboBox()
        self.input_metric.addItems(['Flesch-Kincaid Grade Level', 'Flesch Reading Ease', 'Dale Chall Readability', 'Automated Readability Index', 'Coleman Liau Index', 'Gunning Fog Index', 'SMOG Index', 'SPACHE Readability Formula', 'Linsear Write'])
        column2.addWidget(self.input_metric)

        self.go_button = QPushButton('Analyze')
        column2.addWidget(self.go_button)
        self.go_button.clicked.connect(self.outputs_update)
        
        self.score_output = QLabel('Score Output: N/A')
        column2.addWidget(self.score_output)

        self.grade_level_output = QLabel('Grade Level: N/A')
        column2.addWidget(self.grade_level_output)
        
        self.ease_output = QLabel('Ease: N/A')
        column2.addWidget(self.ease_output)

        self.ages_output = QLabel('Ages: N/A')
        column2.addWidget(self.ages_output)

        self.word_count_output = QLabel('Word Count: N/A')
        column2.addWidget(self.word_count_output)

        self.char_count_output = QLabel('Character Count: N/A')
        column2.addWidget(self.char_count_output)

        self.help_button = QPushButton('Help')
        column2.addWidget(self.help_button)
        self.help_button.clicked.connect(self.show_help_window)

        widget = QWidget()
        widget.setLayout(row1)
        self.setCentralWidget(widget)
    
    def outputs_update(self):
        read_text_metric = self.input_metric.currentText()
        read_text_input = self.input_text.toPlainText()
        update_result = read_text(read_text_input, read_text_metric)

    def show_help_window(self, checked):
        global transfer_window
        transfer_window = HelpWindow()
        transfer_window.show()



application = QApplication(sys.argv)
window = Window()
window.show()
application.exec()