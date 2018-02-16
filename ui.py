from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *

import sys, os

from query import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('bing dictionary')

        layout = QVBoxLayout()

        line = QLineEdit()
        line.returnPressed.connect(lambda : self.lookupEntry(self.line.text()))
        layout.addWidget(line)
        self.line = line

        web = QWebView()
        layout.addWidget(web)
        self.web = web

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def lookupEntry(self, word):
        word, html = getEntry(word)
        with open(os.path.expanduser('~/Documents/vocabulary.txt'),'a') as fo:
            fo.write(word + '\n')
        self.line.setText(word)
        self.web.setHtml(html, QUrl('about:blank'))

app = QApplication(sys.argv)
app.setApplicationName('online-dictionary')
window = MainWindow()

def run():
    window.show()
    app.exec_()
