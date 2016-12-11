# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        point = QtGui.QCursor.pos()
        x = QtCore.QPoint.x(point)
        y = QtCore.QPoint.y(point)
        # x = QtGui.QMouseEvent.globalX()
        # y = QtGui.QMouseEvent.globalY()
        # print(x)
        # print(y)
        # Form.resize(293, 210)
        Form.setGeometry(x-20,y+10,300,190)

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.SubWindow|QtCore.Qt.WA_TranslucentBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        def nouse():
            if False:
              Form.destroyed()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.listWidget.itemPressed.connect(Form.destroy)
        self.listWidget.itemPressed.connect(nouse)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "dsafsafasdfsaf"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "dsfasf的算法啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "阿斯顿飞凤飞飞飞凤飞飞凤飞飞凤飞飞"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "倒萨飞凤飞飞飞凤飞飞凤飞飞凤飞飞"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
class window(QtWidgets.QDial,Ui_Form):
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.globalPos = event.globalPos() - self.dragPosition
            self.move(self.globalPos)
            event.accept()
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QDial()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

