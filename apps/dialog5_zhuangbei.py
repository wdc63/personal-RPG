# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog5_zhuangbei.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
global add
add = []
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 218)
        # Dialog.setModal(True)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 4)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 2, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 0, 4, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 1, 2, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 1, 4, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 2, 2, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 2, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_3.setText('换行')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ## 修改界面上的按钮和输入框一些基本设定
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setMinimum(-10)
        self.doubleSpinBox.setMaximum(10)

        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setMinimum(-10)
        self.doubleSpinBox_2.setMaximum(10)

        self.doubleSpinBox_3.setSingleStep(0.01)
        self.doubleSpinBox_3.setMinimum(-10)
        self.doubleSpinBox_3.setMaximum(10)

        self.doubleSpinBox_4.setSingleStep(0.01)
        self.doubleSpinBox_4.setMinimum(-10)
        self.doubleSpinBox_4.setMaximum(10)

        self.doubleSpinBox_5.setSingleStep(0.01)
        self.doubleSpinBox_5.setMinimum(-10)
        self.doubleSpinBox_5.setMaximum(10)

        self.doubleSpinBox_6.setSingleStep(0.01)
        self.doubleSpinBox_6.setMinimum(-10)
        self.doubleSpinBox_6.setMaximum(10)

        ##确定按钮后的行为
        def queding():
        ##确定之后的增量变量创建
            global add
            add = []
            add.append('装备：'+self.lineEdit.text())
            add.append(self.lineEdit_2.text())
            add.append(float(self.doubleSpinBox.text()))
            add.append(float(self.doubleSpinBox_3.text()))
            add.append(float(self.doubleSpinBox_5.text()))
            add.append(float(self.doubleSpinBox_2.text()))
            add.append(float(self.doubleSpinBox_4.text()))
            add.append(float(self.doubleSpinBox_6.text()))

        ##初始化变量
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path

        ##装备加成并写入存档
            zhuangbei.append(add)
            dianshu['d1'] = round(dianshu['d1'] + add[2],3)
            dianshu['d2'] = round(dianshu['d2'] + add[3],3)
            dianshu['d3'] = round(dianshu['d3'] + add[4],3)
            dianshu['d4'] = round(dianshu['d4'] + add[5],3)
            dianshu['d5'] = round(dianshu['d5'] + add[6],3)
            dianshu['d6'] = round(dianshu['d6'] + add[7],3)
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.destroy()
        def tuichu():
            Dialog.destroy()
        def huanhang():
            self.lineEdit_2.insert('<br/>')
            self.lineEdit_2.setMouseTracking(True)
        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(tuichu)
        self.pushButton_3.clicked.connect(huanhang)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加装备"))
        self.label_9.setText(_translate("Dialog", "装备说明"))
        self.label_6.setText(_translate("Dialog", "专注："))
        self.label.setText(_translate("Dialog", "设定点数加成"))
        self.label_2.setText(_translate("Dialog", "装备名称"))
        self.label_5.setText(_translate("Dialog", "耐力："))
        self.label_7.setText(_translate("Dialog", "智力："))
        self.label_8.setText(_translate("Dialog", "知识量："))
        self.label_3.setText(_translate("Dialog", "体质："))
        self.label_4.setText(_translate("Dialog", "体重："))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.pushButton.setText(_translate("Dialog", "确定"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())