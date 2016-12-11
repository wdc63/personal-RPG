# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\MyRPG\jinruxitong.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
kaiguan = 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 229)
        MainWindow.setMinimumSize(QtCore.QSize(399, 229))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, -1, 20, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 4, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 4, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionWdc63 = QtWidgets.QAction(MainWindow)
        self.actionWdc63.setObjectName("actionWdc63")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.menu_2.addAction(self.actionWdc63)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_6)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        def getandrewrite():
            a = str(self.lineEdit_2.text())
            b = self.lineEdit.text()
            if a == '2224005wdc' and b == 'wdc63':
                import sys
                sys.exit(0)
            else:
                def jingaochuang() :
                    global kaiguan
                    if kaiguan == 0:
                        import dengluxiaoxi
                        global dengluxiaoxi
                        kaiguan = kaiguan +1
                    else:
                        dengluxiaoxi.Dialog.show()

                jingaochuang()

        def changename():
            _translate = QtCore.QCoreApplication.translate
            self.lineEdit.setText(_translate("MainWindow", "wdc63"))

        self.pushButton_4.clicked.connect(getandrewrite)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.action_3.triggered.connect(MainWindow.close)
        self.actionWdc63.triggered.connect(changename)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆"))
        self.pushButton_4.setText(_translate("MainWindow", "确定"))
        self.pushButton_3.setText(_translate("MainWindow", "取消"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>用户名必须是数字和字母组合，且不能以数字开头。</p></body></html>"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>测试按钮</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "用户名"))
        self.pushButton_2.setText(_translate("MainWindow", "密码"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.menu_2.setTitle(_translate("MainWindow", "用户"))
        self.action.setText(_translate("MainWindow", "退出"))
        self.action_3.setText(_translate("MainWindow", "退出"))
        self.actionWdc63.setText(_translate("MainWindow", "wdc63"))
        self.action_6.setText(_translate("MainWindow", "注册用户(未开放)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

