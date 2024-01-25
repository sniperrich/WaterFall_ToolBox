# coding:utf-8
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QFileDialog
from qfluentwidgets import InfoBarIcon, InfoBar, PushButton, setTheme, Theme, FluentIcon, InfoBarPosition, \
    InfoBarManager, BodyLabel
from functools import partial
import os
from threading import Thread

from UI.vdownui import Ui_Vdown


class VdownInterface(QWidget, Ui_Vdown):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
