import keyboard
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        Back_button = QAction('<-', self)
        Back_button.triggered.connect(self.browser.back)
        navbar.addAction(Back_button)

        Forward_button = QAction('->', self)
        Forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_button)

        Reload_button = QAction('Reload', self)
        Reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(Reload_button)

        Home_button = QAction("Home", self)
        Home_button.triggered.connect(self.open_url)
        navbar.addAction(Home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        Url1_button = QAction("History", self)
        Url1_button.triggered.connect(self.url1)
        navbar.addAction(Url1_button)

        Url2_button = QAction("Gmail", self)
        Url2_button.triggered.connect(self.url2)
        navbar.addAction(Url2_button)

        Url3_button = QAction("Roblox", self)
        Url3_button.triggered.connect(self.url3)
        navbar.addAction(Url3_button)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def open_url(self):
        url = QUrl("https://duckduckgo.com")
        self.browser.setUrl(url)

    def url1(self):
        url = QUrl("chrome://history/")
        self.browser.setUrl(url)

    def url2(self):
        url = QUrl("http://gmail.com")
        self.browser.setUrl(url)

    def url3(self):
            url = QUrl("http://roblox.com")
            self.browser.setUrl(url)




app = QApplication(sys.argv)
QApplication.setApplicationName('Bad Browser')
Window = MainWindow()
app.exec_()