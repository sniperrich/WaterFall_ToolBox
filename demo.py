# coding:utf-8
import os.path
import sys
import configparser
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition)
from qfluentwidgets import FluentIcon as FIF
from home_interface import HomeInterface
from setting_interface import SettingInterface
from dll_interface import DllInterface
from mdown_interface import MdownInterface
from api_interface import ApiInterface
from vdown_interface import VdownInterface
class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface

        self.homeInterface = HomeInterface(self)
        self.musicInterface = DllInterface(self)

        self.folderInterface = ApiInterface(self)
        self.settingInterface = SettingInterface(self)
        self.albumInterface = Widget('Please choose music or video', self)
        self.albumInterface1 = MdownInterface(self)
        self.albumInterface2 = VdownInterface(self)


        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.DEVELOPER_TOOLS, 'DLL Injector')
        self.addSubInterface(self.musicInterface, FIF.UPDATE, 'System Info')


        self.navigationInterface.addSeparator()

        self.addSubInterface(self.albumInterface, FIF.DOWNLOAD, 'Download', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.albumInterface1, FIF.MUSIC, 'Download music', parent=self.albumInterface)

        self.addSubInterface(self.albumInterface2, FIF.BOOK_SHELF, 'Download Video', parent=self.albumInterface)
        self.addSubInterface(self.folderInterface, FIF.STOP_WATCH, 'Plan', NavigationItemPosition.SCROLL)

        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Rich', 'resource/shoko.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        # add badge to navigation item


        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('resource/logo.png'))

        self.setWindowTitle('WaterFall ToolBoxᵈᵉᵛ')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://space.bilibili.com/520550931?spm_id_from=333.1007.0.0"))


if __name__ == '__main__':
    if not os.path.exists("config.ini"):
        with open("config.ini","w") as f:
            f.write("[DEFAULT]\ntheme = 0")
    else:
        pass
    conf = configparser.ConfigParser()

    conf.read('config.ini')
    theme = conf.get('DEFAULT', 'theme')
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    if (theme == '0'):
        setTheme(Theme.AUTO)
    elif (theme == '1'):
        setTheme(Theme.LIGHT)
    elif (theme == '2'):
        setTheme(Theme.DARK)


    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
