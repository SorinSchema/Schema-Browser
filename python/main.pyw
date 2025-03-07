import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QToolBar, QAction, QLineEdit, QPushButton
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

import stylesheet

class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fullScreenRequested.connect(self.handle_fullscreen)

    def handle_fullscreen(self, request):
        request.accept()
        if request.toggleOn():
            self.view().setWindowFlags(self.view().windowFlags() | Qt.Window)
            self.view().showFullScreen()
        else:
            self.view().setWindowFlags(self.view().windowFlags() & ~Qt.Window)
            self.view().showNormal()

class CustomWebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPage(CustomWebEnginePage(self))

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.new_tab_button = QPushButton("+")
        self.new_tab_button.clicked.connect(self.add_new_tab)
        self.tabs.setCornerWidget(self.new_tab_button, corner=Qt.TopRightCorner)

        self.setCentralWidget(self.tabs)

        self.setup_toolbar()

        self.setWindowTitle("Schema Browser")
        self.setGeometry(100, 100, 800, 600)

        self.add_new_tab()

    def add_tab(self, url, label="New Tab"):
        browser = CustomWebEngineView()
        browser.setUrl(url)
        index = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(index)

        browser.titleChanged.connect(lambda title, index=index: self.tabs.setTabText(index, title))
        browser.urlChanged.connect(lambda url, browser=browser: self.update_url(url, browser))

    def add_new_tab(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        last_dir = os.path.dirname(current_dir)
        html_path = os.path.join(last_dir, "web/index.html")

        self.add_tab(QUrl.fromLocalFile(html_path), "New Tab")

    def close_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)

    def setup_toolbar(self):
        toolbar = QToolBar()

        back_button = QAction(QIcon(os.path.join("images/prev.png")), "Back", self)
        back_button.triggered.connect(lambda: self.current_browser().back())
        toolbar.addAction(back_button)

        forward_button = QAction(QIcon(os.path.join("images/next.png")), "Forward", self)
        forward_button.triggered.connect(lambda: self.current_browser().forward())
        toolbar.addAction(forward_button)

        reload_button = QAction(QIcon(os.path.join("images/loading.gif")), "Reload", self)
        reload_button.triggered.connect(lambda: self.current_browser().reload())
        toolbar.addAction(reload_button)

        self.nav_bar = QLineEdit()
        self.nav_bar.returnPressed.connect(self.navigate_url)
        toolbar.addWidget(self.nav_bar)

        self.addToolBar(toolbar)

    def navigate_url(self):
        url = QUrl(self.nav_bar.text())
        if url.scheme() == "":
            url.setScheme("https")
        self.current_browser().setUrl(url)

    def update_url(self, url, browser=None):
        if browser == self.current_browser():
            self.nav_bar.setText(url.toString())

    def current_browser(self):
        return self.tabs.currentWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()

    window.setStyleSheet(stylesheet.stylesheet)

    window.show()
    sys.exit(app.exec_())
