# coding:utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

from UI.apiui import Ui_Api


class ApiInterface(Ui_Api, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

