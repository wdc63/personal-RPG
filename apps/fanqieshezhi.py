# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fanqieshizhi.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(312, 180)
        Dialog.setModal(True)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 3, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout.addWidget(self.spinBox_4, 3, 3, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 2, 3, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 3, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.spinBox.setRange(10,60)
        self.spinBox_2.setRange(2,10)
        self.spinBox_3.setRange(5,25)
        self.spinBox_4.setRange(3,8)
        def chushihua():
            global shezhi, fanqielishi
            import pickle
            path = open('D:/MyRPG/fanqie.dat','rb')
            shezhi,fanqielishi = pickle.load(path)
            path.close()
            del path
            self.spinBox.setValue(shezhi[0])
            self.spinBox_2.setValue(shezhi[1])
            self.spinBox_3.setValue(shezhi[2])
            self.spinBox_4.setValue(shezhi[3])

        def queding():
            import pickle
            global shezhi, fanqielishi
            shezhi[0] = self.spinBox.value()
            shezhi[1] = self.spinBox_2.value()
            shezhi[2] = self.spinBox_3.value()
            shezhi[3] = self.spinBox_4.value()
            path = open('D:/MyRPG/fanqie.dat','wb')
            pickle.dump((shezhi,fanqielishi),path)
            path.close()
            del path
            Dialog.destroy()

        def huifumoren():
            self.spinBox.setValue(25)
            self.spinBox_2.setValue(5)
            self.spinBox_3.setValue(15)
            self.spinBox_4.setValue(4)
        def quxiao():
            Dialog.destroy()

        chushihua()
        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(huifumoren)
        self.pushButton_3.clicked.connect(quxiao)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "番茄设置"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "恢复默认"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", "番茄工作时间（分钟）："))
        self.label_2.setText(_translate("Dialog", "短休息时间（分钟）："))
        self.label_3.setText(_translate("Dialog", "长休息时间（分钟）："))
        self.label_4.setText(_translate("Dialog", "连续获得几个番茄后进行长休息？"))
#
# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())
