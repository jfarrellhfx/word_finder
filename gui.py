import sys
from prototype import tests

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextBrowser

with open("words_alpha.txt", 'r') as g:
    words = g.read().splitlines()
    g.close()
string = ""



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Morgan's Word Finder")

word_length = QLineEdit(placeholderText = "word length")
word_length_min =  QLineEdit(placeholderText = "minimum length")
word_length_max = QLineEdit(placeholderText = "maximum length")
word_starts_with = QLineEdit(placeholderText = "starting letter or phrase")
word_ends_with = QLineEdit(placeholderText = "Ending letter or phrase")
word_contains11 = QLineEdit(placeholderText = "word contains this letter or phrase")
word_contains12 = QLineEdit(placeholderText = "optional, another phrase")


layout = QGridLayout()
layout.addWidget(QLabel("<h2>Options:</h2>"), 0, 0)



layout.addWidget(QLabel("<h3>Length: </h3>"), 1, 0)
layout.addWidget(word_length, 1, 1)

layout.addWidget(QLabel("<h3>Starts With: </h3>"), 2, 0)
layout.addWidget(word_starts_with, 2, 1)

layout.addWidget(QLabel("<h3>                  Ends With: </h3>"), 3, 0)
layout.addWidget(word_ends_with, 3, 1)

layout.addWidget(QLabel("<h3>Contains: </h3>"), 4, 0)
layout.addWidget(word_contains11, 4, 1)

layout.addWidget(QLabel("or"), 4, 2)
layout.addWidget(word_contains12, 4, 3)



browser = QTextBrowser()
def check_words():
    browser.clear()
    global words
    global layout
    global string

    conditions = []
    string = ""

    if word_length.text() != "":
        conditions.append(lambda word: tests.length(word, word_length.text()))

    if word_starts_with.text() != "":
        conditions.append(lambda word: tests.startswith(word, word_starts_with.text()))

    if word_ends_with.text() != "":
        conditions.append(lambda word: tests.endswith(word, word_ends_with.text()))

    if word_contains11.text() != "" and word_contains12.text() == "":
        conditions.append(lambda word: tests.contains(word, word_contains11.text()))

    if word_contains11.text() != "" and word_contains12.text() != "":
        conditions.append(lambda word: tests.contains(word, word_contains11.text()) or tests.contains(word, word_contains12.text()))





    for word in words:
        combined_condition = True
        for condition in conditions:
            combined_condition = combined_condition and condition(word)

        if combined_condition:
            string += "<a href = \"https://www-oed-com.myaccess.library.utoronto.ca/search?searchType=dictionary&q={}&_searchBtn=Search\">{}</a>".format(word, word) + "<br>"

    browser.append(string)







button = QPushButton("Test")
button.clicked.connect(check_words)

layout.addWidget(button, 100, 1)
window.setLayout(layout)

browser.setOpenExternalLinks(True)
layout.addWidget(browser, 6, 1)

window.show()
sys.exit(app.exec_())
