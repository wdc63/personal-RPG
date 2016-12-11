# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog6_tianjiaxiguan.ui'
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
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(373, 281)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 8, 1, 1, 5)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 9, 1, 1, 5)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 5)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setEnabled(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 5)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 4, 1, 1, QtCore.Qt.AlignRight)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 6, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 1, 1, 2, QtCore.Qt.AlignRight)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 3, 1)
        self.label_13 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 7, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 3, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 2, QtCore.Qt.AlignRight)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 5, 3, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 5, 5, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 7, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 9, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 1, 1, 2, QtCore.Qt.AlignRight)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 4, 1, 1, QtCore.Qt.AlignRight)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 4, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 4, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 5, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 6, 5, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 2, QtCore.Qt.AlignRight)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 10, 0, 1, 1)
        self.pushButton_3.setText('换行')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ## 修改界面上数字输入的按钮和输入框一些基本设定
        self.doubleSpinBox.setSingleStep(0.001)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMinimum(-1)
        self.doubleSpinBox.setMaximum(1)
        self.doubleSpinBox_2.setSingleStep(0.001)
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setMinimum(-1)
        self.doubleSpinBox_2.setMaximum(1)
        self.doubleSpinBox_3.setSingleStep(0.001)
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setMinimum(-1)
        self.doubleSpinBox_3.setMaximum(1)
        self.doubleSpinBox_4.setSingleStep(0.001)
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setMinimum(-1)
        self.doubleSpinBox_4.setMaximum(1)
        self.doubleSpinBox_5.setSingleStep(0.001)
        self.doubleSpinBox_5.setDecimals(3)
        self.doubleSpinBox_5.setMinimum(-1)
        self.doubleSpinBox_5.setMaximum(1)
        self.doubleSpinBox_6.setSingleStep(0.001)
        self.doubleSpinBox_6.setDecimals(3)
        self.doubleSpinBox_6.setMinimum(-1)
        self.doubleSpinBox_6.setMaximum(1)
        self.spinBox.setMaximum(0)
        self.spinBox.setMinimum(-20)
        self.spinBox.setValue(-5)
        self.spinBox_2.setMaximum(0)
        self.spinBox_2.setMinimum(-20)
        self.spinBox_2.setValue(-5)
        # self.radioButton.setChecked(True)
        # self.radioButton_3.setChecked(True)

        ## 好习惯难度和坏习惯减益都暂时隐藏掉
        self.label_3.setEnabled(False)
        self.label_4.setEnabled(False)
        self.label_5.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.spinBox_2.setEnabled(False)
        self.label_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)
        self.radioButton_5.setEnabled(False)

        global  panduanxiguan,panduannandu
        panduanxiguan = '判断习惯'
        panduannandu = '判断难度'

        ##点选好习惯时，坏习惯的所有按钮都禁用，好习惯按钮开启
        def panduanxiguanhao():
            self.label_3.setEnabled(False)
            self.label_4.setEnabled(False)
            self.label_5.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.spinBox_2.setEnabled(False)
            self.label_2.setEnabled(True)
            self.radioButton_3.setEnabled(True)
            self.radioButton_4.setEnabled(True)
            self.radioButton_5.setEnabled(True)
            self.pushButton.setText('确定')
        def panduanxiguanhuai():
            self.label_3.setEnabled(True)
            self.label_4.setEnabled(True)
            self.label_5.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.spinBox_2.setEnabled(True)
            self.label_2.setEnabled(False)
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.radioButton_5.setEnabled(False)
            self.pushButton.setText('确定')

        ##点选难度选择时候的一系列变化
        # def jiandan():
        #     global panduannandu
        #     panduannandu = 1
        #     self.pushButton.setText('确定')
        #
        # def zhongdeng():
        #     global panduannandu
        #     panduannandu = 2
        #     self.pushButton.setText('确定')
        #
        # def kunnan():
        #     global panduannandu
        #     panduannandu = 3
        #     self.pushButton.setText('确定')

        ## 判断习惯和习惯难度的信号槽
        self.radioButton.toggled.connect(panduanxiguanhao)
        self.radioButton_2.toggled.connect(panduanxiguanhuai)
        # self.radioButton_3.toggled.connect(jiandan)
        # self.radioButton_4.toggled.connect(zhongdeng)
        # self.radioButton_5.toggled.connect(kunnan)

        ####确定之后的一系列变化
        def queding():
            ###将习惯内容装入add变量
            global add
            add = []
            if self.radioButton.isChecked():
                add.append('好习惯：'+self.lineEdit.text())
                add.append(self.lineEdit_2.text())
                add.append(float(self.doubleSpinBox.text()))
                add.append(float(self.doubleSpinBox_3.text()))
                add.append(float(self.doubleSpinBox_5.text()))
                add.append(float(self.doubleSpinBox_2.text()))
                add.append(float(self.doubleSpinBox_4.text()))
                add.append(float(self.doubleSpinBox_6.text()))
                if self.radioButton_3.isChecked():
                    add.append(5)
                    add.append(1)
                    # print(add)
                elif self.radioButton_4.isChecked():
                    add.append(8)
                    add.append(2)
                    # print(add)
                elif self.radioButton_5.isChecked():
                    add.append(11)
                    add.append(3)
                    # print(add)
                else:
                    self.pushButton.setText('请选择难度')
                    # print(add)
                    add = []
                    return

            elif self.radioButton_2.isChecked():
                add.append('坏习惯：'+self.lineEdit.text())
                add.append(self.lineEdit_2.text())
                add.append(float(self.doubleSpinBox.text()))
                add.append(float(self.doubleSpinBox_3.text()))
                add.append(float(self.doubleSpinBox_5.text()))
                add.append(float(self.doubleSpinBox_2.text()))
                add.append(float(self.doubleSpinBox_4.text()))
                add.append(float(self.doubleSpinBox_6.text()))
                add.append(int(self.spinBox.text()))
                add.append(int(self.spinBox_2.text()))
                # print(add)
            else:
                # print(add)
                self.pushButton.setText('请选择种类')
                return


            ###初始化xiguanall变量并装入
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path
            if self.radioButton.isChecked():
                xiguanall.insert(0,add)
            if self.radioButton_2.isChecked():
                xiguanall.append(add)

            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            # print(add)
            Dialog.destroy()

        def tuichu():
            Dialog.destroy()
        def huanhang():
            self.lineEdit_2.insert('<br/>')
        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(tuichu)
        self.pushButton_3.clicked.connect(huanhang)






    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加习惯"))
        self.radioButton_3.setToolTip(_translate("Dialog", "<html><head/><body><p>简单习惯，你将获得<span style=\" font-weight:600; color:#ff0000;\">5</span>经验和<span style=\" font-weight:600; color:#ff0000;\">1</span>点娱乐点。</p></body></html>"))
        self.radioButton_3.setText(_translate("Dialog", "简单"))
        self.radioButton_4.setToolTip(_translate("Dialog", "<html><head/><body><p>中等习惯，你将获得<span style=\" font-weight:600; color:#ff0000;\">8</span>经验和<span style=\" font-weight:600; color:#ff0000;\">2</span>点娱乐点。</p></body></html>"))
        self.radioButton_4.setText(_translate("Dialog", "中等"))
        self.radioButton_5.setToolTip(_translate("Dialog", "<html><head/><body><p>困难习惯，你将获得<span style=\" font-weight:600; color:#ff0000;\">11</span>经验和<span style=\" font-weight:600; color:#ff0000;\">3</span>点娱乐点。</p></body></html>"))
        self.radioButton_5.setText(_translate("Dialog", "困难"))
        self.radioButton.setText(_translate("Dialog", "好习惯"))
        self.radioButton_2.setText(_translate("Dialog", "坏习惯"))
        self.label_10.setText(_translate("Dialog", "智力："))
        self.label_7.setText(_translate("Dialog", "体质："))
        self.label_6.setText(_translate("Dialog", "设定点数加成/减益"))
        self.label_13.setText(_translate("Dialog", "名称"))
        self.label_2.setText(_translate("Dialog", "好习惯难度"))
        self.label_4.setText(_translate("Dialog", "经验："))
        self.label_14.setText(_translate("Dialog", "描述"))
        self.label_11.setText(_translate("Dialog", "耐力："))
        self.label_8.setText(_translate("Dialog", "专注："))
        self.label_5.setText(_translate("Dialog", "娱乐点："))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label_12.setText(_translate("Dialog", "知识量："))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", "习惯种类"))
        self.label_3.setText(_translate("Dialog", "坏习惯减益"))
        self.label_9.setText(_translate("Dialog", "体重："))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())