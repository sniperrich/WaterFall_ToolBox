# coding:utf-8
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QFileDialog
from qfluentwidgets import InfoBarIcon, InfoBar, PushButton, setTheme, Theme, FluentIcon, InfoBarPosition, \
    InfoBarManager
from functools import partial
import os
from PyQt5.QtCore import Qt, QTranslator, QLocale
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication
from qframelesswindow import FramelessWindow, StandardTitleBar, AcrylicWindow
from qfluentwidgets import setThemeColor, FluentTranslator, setTheme, Theme, SplitTitleBar
from threading import Thread

from UI.homeui import Ui_Form


class HomeInterface(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        setThemeColor('#28afe9')




        self.label.setScaledContents(False)

        self.setWindowIcon(QIcon(":/images/logo.png"))
        self.resize(1000, 650)

        self.setStyleSheet("LoginWindow{background: rgba(242, 242, 242, 0.8)}")


        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("resource\\background.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)