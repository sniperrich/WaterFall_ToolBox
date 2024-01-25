# coding:utf-8
import configparser

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import InfoBarIcon, InfoBar, PushButton, setTheme, Theme, FluentIcon, InfoBarPosition, \
    InfoBarManager

from UI.settingui import SettingUi


class SettingInterface(QWidget, SettingUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.HyperlinkLabel.setUrl('https://space.bilibili.com/520550931?spm_id_from=333.1007.0.0'
                                   )

        self.ImageLabel.setPixmap(QPixmap('img/wf.png').scaledToHeight(100))

        # 选择主题

        conf = configparser.ConfigParser()
        conf.read('config.ini')
        theme = conf.get('DEFAULT', 'theme')

        self.ThemeBox.addItem('跟随系统')
        self.ThemeBox.addItem('浅色')
        self.ThemeBox.addItem('深色')

        self.ThemeBox.setCurrentIndex(int(theme))
        self.ThemeBox.currentIndexChanged.connect(self.ThemeBoxChanged)

        # 关闭开屏画面



    # 选择主题
    def ThemeBoxChanged(self):
        conf = configparser.ConfigParser()
        conf.read('config.ini')
        conf.set('DEFAULT', 'theme', str(self.ThemeBox.currentIndex()))
        conf.write(open('config.ini', 'w'))

        InfoBar.info(
            title='提示',
            content="主题修改重启应用后生效",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=5000,
            parent=self
        )

    # 关闭开屏画面

