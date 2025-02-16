# text analyzer in python
# github.com/sidsenthilexe/text-analyzer

# imports
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPlainTextEdit, QComboBox, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from nltk.tokenize import sent_tokenize
import sys
from readability import Readability
from textblob import TextBlob
import nltk
nltk.download('punkt_tab')
nltk.download('punkt')

# function to read and analyze text
def read_text(text, metric_type):

    # try to analyze the text, skip if not possible (if there are less than 100 words)
    try:
        readability_analyze = Readability(text)
        match metric_type:
            case 'Flesch-Kincaid Grade Level':
                fk = readability_analyze.flesch_kincaid()
                score = round(fk.score, 3)
                grade_level = fk.grade_level
                ease, ages = 'N/A', 'N/A'
            case 'Flesch Reading Ease':
                f = readability_analyze.flesch()
                score = round(f.score, 3)
                ease = f.ease
                grade_level = f.grade_levels
                ages = 'N/A'
            case 'Dale Chall Readability':
                dc = readability_analyze.dale_chall()
                score = round(dc.score, 3)
                grade_level = dc.grade_levels
                ease, ages = 'N/A', 'N/A'
            case 'Automated Readability Index':
                ari = readability_analyze.ari()
                score = round(ari.score, 3)
                ages = ari.ages
                grade_level = ari.grade_levels
                ease = 'N/A'
            case 'Coleman Liau Index':
                cl = readability_analyze.coleman_liau()
                score = round(cl.score, 3)
                grade_level = cl.grade_level
                ease, ages = 'N/A', 'N/A'
            case 'Gunning Fog Index':
                gf = readability_analyze.gunning_fog()
                score = round(gf.score, 3)
                grade_level = gf.grade_level
                ease, ages = 'N/A', 'N/A'
            case 'SMOG Index':
                smog = readability_analyze.smog(all_sentences=True)
                score = round(smog.score, 3)
                grade_level = smog.grade_level
                ease, ages = 'N/A', 'N/A'
            case 'Spache Readability Formula':
                spache = readability_analyze.spache()
                score = round(spache.score, 3)
                grade_level = spache.grade_level
                ease, ages = 'N/A', 'N/A'
            case 'Linsear Write':
                lw = readability_analyze.linsear_write()
                score = round(lw.score, 3)
                grade_level = lw.grade_level
                ease, ages = 'N/A', 'N/A'
            case _ :
                score, grade_level, ease, ages = 'N/A', 'N/A', 'N/A', 'N/A'
    except:
        score, grade_level, ease, ages = 'N/A', 'N/A', 'N/A', 'N/A'

    # get the number of words, characters and sentences
    word_count = len(text.split())
    char_count = len(text)
    sentence_count = len(sent_tokenize(text))

    # get the sentiment
    textblob_analyze = TextBlob(text)
    sentiment_polarity = round(textblob_analyze.polarity, 3)
    sentiment_subjectivity = round(textblob_analyze.subjectivity, 3)

    # output everything as a list
    output = [score, grade_level, ease, ages, word_count, char_count, sentence_count, sentiment_polarity, sentiment_subjectivity]

    return output
    
# function to change the help text based on the selected index
def change_help_text(type):
    match type:
        case 'Flesch-Kincaid Grade Level':
            help_text = 'Flesch-Kincaid is based on the length of words and sentences in the text.\nIt is based off grade levels in terms of the American education system.\nAll Readability Analyses require 100+ words.'
        case 'Flesch Reading Ease':
            help_text = 'Flesch Reading Ease scores a text from 1-100 based on sentence and word lengths.\nScoring between 70 and 80 is roughly equivalent to an 8th grade level.'
        case 'Dale Chall Readability':
            help_text = 'Dale Chall Readability utilises a list of 3,000 common words to calculate\nthe amount of difficult words in a text. A score of 6-7 is easily understood\nby a 7th or 8th grader.\nAll Readability Analyses require 100+ words.'
        case 'Automated Readability Index':
            help_text = 'The ARI uses a factor of characters per word, and the score is approximately\nthe grade level needed to understand the text.'
        case 'Coleman Liau Index':
            help_text = 'The Coleman Liau Index uses the average number of letters and sentences per 100\nwords to approximate the grade level needed to understand the text.\nAll Readability Analyses require 100+ words.'
        case 'Gunning Fog Index':
            help_text = 'The Gunning Fog Index attempts to estimate the number of years of education\nnecessary to understand a text based on average sentence length and the number\nof complex words.\nAll Readability Analyses require 100+ words.'
        case 'SMOG Index':
            help_text = 'The SMOG Index estimates the number of years of education necessary to understand\na text based on the number of words with more than 2 syllables.\nAll Readability Analyses require 100+ words.'
        case 'Spache Readability Formula':
            help_text = 'The Spache Readability Formula compares a set of common words to\nthe words in a text. The score is calculated based on the number of words per sentence\nand the percentage of unfamiliar words.\nAll Readability Analyses require 100+ words.'
        case 'Linsear Write':
            help_text = 'Linsear Write estimates the grade level of a text based on sentence length and the\nnumber of words with 2 or more syllables.\nAll Readability Analyses require 100+ words.'
        case 'Polarity':
            help_text = 'Polarity measures the sentiment of a text on a scale from -1 (very negative)\nto 1 (very positive).'
        case 'Subjectivity':
            help_text = 'Subjectivity measures how a statement expresses opinions, rather than objective facts.\nIt ranges from 0 (completely objective) to 1 (completely subjective).'
        case _ :
            help_text = 'Error'
    return help_text

# help window class
class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Analyzer Help')

        layout = QVBoxLayout()

        # list of readability indexes and other output metrics, run help_text_update when changed
        self.type_select = QComboBox()
        self.type_select.addItems(['Polarity', 'Subjectivity', 'Flesch-Kincaid Grade Level', 'Flesch Reading Ease', 'Dale Chall Readability', 'Automated Readability Index', 'Coleman Liau Index', 'Gunning Fog Index', 'SMOG Index', 'Spache Readability Formula', 'Linsear Write'])
        layout.addWidget(self.type_select)
        self.type_select.currentTextChanged.connect(self.help_text_update)

        # label for the help text output
        self.help_output_text = QLabel()
        self.help_output_text.setText('Polarity measures the sentiment of a text on a scale from -1 (very negative)\nto 1 (very positive).')
        layout.addWidget(self.help_output_text)

        self.setLayout(layout)

    # function to update the help text
    def help_text_update(self):
        help_input = self.type_select.currentText()
        help_output = change_help_text(help_input)
        self.help_output_text.setText(str(help_output))
    
# main window class
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Analyzer')

        # layout stuff
        column1 = QVBoxLayout()
        column2 = QVBoxLayout()
        row1 = QHBoxLayout()
        row1.addLayout(column1)
        row1.addLayout(column2)

        # input text box
        self.input_text = QPlainTextEdit()
        column1.addWidget(self.input_text)

        # open dialog to choose file
        self.open_button = QPushButton("Open .txt file", self)
        column1.addWidget(self.open_button)
        self.open_button.clicked.connect(self.open_file)

        # choose analysis metric
        self.input_metric = QComboBox()
        self.input_metric.addItems(['Flesch-Kincaid Grade Level', 'Flesch Reading Ease', 'Dale Chall Readability', 'Automated Readability Index', 'Coleman Liau Index', 'Gunning Fog Index', 'SMOG Index', 'SPACHE Readability Formula', 'Linsear Write'])
        column2.addWidget(self.input_metric)

        # update the outputs with the analysis
        self.go_button = QPushButton('Analyze')
        column2.addWidget(self.go_button)
        self.go_button.clicked.connect(self.outputs_update)
        
        # outputs
        self.word_count_output = QLabel('Word Count: N/A')
        column2.addWidget(self.word_count_output)

        self.char_count_output = QLabel('Character Count: N/A')
        column2.addWidget(self.char_count_output)

        self.sentence_count_output = QLabel('Sentence Count: N/A')
        column2.addWidget(self.sentence_count_output)

        
        self.polarity_output = QLabel('Polarity: N/A')
        column2.addWidget(self.polarity_output)

        self.subjectivity_output = QLabel('Subjectivity: N/A')
        column2.addWidget(self.subjectivity_output)

        self.score_output = QLabel('Score: N/A')
        column2.addWidget(self.score_output)

        self.grade_level_output = QLabel('Grade Level: N/A')
        column2.addWidget(self.grade_level_output)
        
        self.ease_output = QLabel('Ease: N/A')
        column2.addWidget(self.ease_output)

        self.ages_output = QLabel('Ages: N/A')
        column2.addWidget(self.ages_output)

        # help button, connected to show_help_window
        self.help_button = QPushButton('Help')
        column2.addWidget(self.help_button)
        self.help_button.clicked.connect(self.show_help_window)

        widget = QWidget()
        widget.setLayout(row1)
        self.setCentralWidget(widget)
        
    # function to open a .txt file
    def open_file(self):

        # get the file path, ignore the .txt filter
        file_path, _ = QFileDialog.getOpenFileName(self, "Open .txt file", "", "Text Files (*.txt)")

        # if the file path exists
        if file_path:

            # try used for error handling
            try:
                # read the file and set the text
                with open(file_path, "r") as file:
                    self.input_text.setPlainText(file.read())
            except:
                self.input_text.setPlainText('Error reading file')

    # update all outputs based on the current inputs
    def outputs_update(self):

        # get the current requested metric
        read_text_metric = self.input_metric.currentText()

        # get the current input text
        read_text_input = self.input_text.toPlainText()

        # analyze the text
        update_result = read_text(read_text_input, read_text_metric)

        # format the output (list)
        score, grade_level, ease, ages, word_count, char_count, sentence_count, sentiment_polarity, sentiment_subjectivity = update_result

        # set all the labels to the outputs (not in order what did you expect)
        self.score_output.setText('Score: '+str(score))
        self.grade_level_output.setText('Grade Level: '+str(grade_level))
        self.ease_output.setText('Ease: '+str(ease))
        self.ages_output.setText('Ages: '+str(ages))
        self.word_count_output.setText('Word Count: '+str(word_count))
        self.char_count_output.setText('Character Count: '+str(char_count))
        self.sentence_count_output.setText('Sentence Count: '+str(sentence_count))
        self.polarity_output.setText('Polarity: '+str(sentiment_polarity))
        self.subjectivity_output.setText('Subjectivity: '+str(sentiment_subjectivity))

    # function to show the help window
    def show_help_window(self, checked):
        global transfer_window
        transfer_window = HelpWindow()
        transfer_window.show()

# window init stuff
application = QApplication(sys.argv)
window = Window()
window.show()
application.exec()
