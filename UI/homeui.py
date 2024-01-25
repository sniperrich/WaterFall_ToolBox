


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import psutil
from pyinjector import inject
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition)
from qfluentwidgets import FluentIcon as FIF


class Ui_Form(object):

    def opena(self, Filepath):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit.setText(m[0])
        print(m[0])
    def inject(self):
        str1 = self.lineEdit.text()
        str2=self.lineEdit_3.text()
        print(str1,str2)
        self.injecting(str1,str2)
    def setupUi(self, Form):


        Form.setObjectName("Form")
        Form.resize(1250, 809)
        Form.setMinimumSize(QtCore.QSize(700, 500))

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("resource/background.jpg"))
        # self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(360, 0))
        self.widget.setMaximumSize(QtCore.QSize(360, 16777215))
        self.widget.setStyleSheet("QLabel{\n"
"    font: 13px \'Microsoft YaHei\'\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resource/logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = LineEdit(self.widget)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_3 = BodyLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = PrimaryPushButton(self.widget)


        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.clicked.connect(self.opena)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = BodyLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_5 = BodyLabel(self.widget)
        self.label_5.setObjectName("label_5")

        self.verticalLayout_2.addWidget(self.label_5)
        self.lineEdit_3 = LineEdit(self.widget)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pushButton = PrimaryPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda :self.inject())
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)


        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "D:\\Choose\\your\\dll"))
        self.label_3.setText(_translate("Form", "选择"))
        self.lineEdit_2.setText(_translate("Form", "选取dll"))

        self.label_5.setText(_translate("Form", "进程"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "yuanshen.exe"))

        self.pushButton.setText(_translate("Form", "注入！！！！！！！！！！！！！！"))

    def injecting(self,inject_dll, pinject):
        dll_to_inject = inject_dll
        if not dll_to_inject.endswith(".dll"):

            w = MessageBox(
                '主播你的iq呢',
                '注入的不是dll呢 建议玩原神提升智商',
                self
            )
            w.yesButton.setText('原神启动')
            w.cancelButton.setText('还是算了')

            if w.exec():
                os.system("start https://www.yuanshen.com/#/")

            print("not dll")
            return



        process_to_inject = pinject
        if not process_to_inject.endswith(".exe"): process_to_inject = process_to_inject + ".exe"

        process_found = False

        for process in psutil.process_iter(attrs=['pid', 'name']):
            try:
                if process.info['name'] == process_to_inject:
                    process_id = process.info['pid']
                    process_name = process.info['name']
                    process_found = True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if process_found:
            dll_to_inject = os.path.basename(dll_to_inject)

            try:
                inject(process_id, inject_dll)

                w = MessageBox(
                    '主播注入成功',
                    '开飘吊打99%的人 iq999+',
                    self
                )
                w.yesButton.setText('原神启动')
                w.cancelButton.setText('还是算了')

                if w.exec():
                    os.system("start https://www.yuanshen.com/#/")
                print("success")
                return


            except Exception as e:


                print("error")
                w = MessageBox(
                    '主播注入失败',
                    '看error.log查看详细信息',
                    self
                )
                w.yesButton.setText('原神启动')
                w.cancelButton.setText('还是算了')

                if w.exec():
                    os.system("start https://www.yuanshen.com/#/")

                with open("error.log", "w") as errorfile:
                    errorfile.write(str(e))
                return

        else:

            w = MessageBox(
                '主播你的iq呢',
                '找不到游戏进程 请注意iq',
                self
            )
            w.yesButton.setText('原神启动')
            w.cancelButton.setText('还是算了')

            if w.exec():
                os.system("start https://www.yuanshen.com/#/")
            print("no process")
            return


from qfluentwidgets import BodyLabel, CheckBox, HyperlinkButton, LineEdit, PrimaryPushButton

