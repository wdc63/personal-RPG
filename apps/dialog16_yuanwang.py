# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog16_yuanwang.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 464)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 2, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 1, 1, 4)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 3, 1, 1, 4)
        self.retranslateUi(Dialog)

        def yuanwangwancheng():
            if self.horizontalSlider.value() == 100:
                self.pushButton.setText('愿望完成！！')
            else:
                self.pushButton.setText('确定')
        self.horizontalSlider.valueChanged['int'].connect(self.progressBar.setValue)
        self.horizontalSlider.valueChanged['int'].connect(yuanwangwancheng)

        ###初始化变量
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.progressBar.setValue(0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMinimum(1)
        self.doubleSpinBox.setMaximum(99999)
        self.doubleSpinBox.clear()
        self.progressBar.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        ##读取变量
        import pickle
        path = open('D:/MyRPG/data.dat','rb')
        global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
        dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
        path.close()
        del path
        self.pushButton.setEnabled(False)
        self.pushButton.setText('请输入序号')
        if yuanwang == [[[0]],[[0]]]:
              self.doubleSpinBox.setValue(1)
              self.pushButton.setEnabled(True)
              self.pushButton.setText('目前只能添加愿望1')
              self.horizontalSlider.setEnabled(False)
              self.doubleSpinBox.setEnabled(False)

        ### 当滑动序号时，界面所做的一系列改变，禁止创建不合法的序号
        def jiemianxiaoyin():
            global yuanwang
            shuzi =  round(self.doubleSpinBox.value(),2)
            i = yuanwang
            if int(shuzi) in i[1][0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('愿望'+str(int(shuzi))+'已经完成')
                    self.progressBar.setValue(100)
                    self.progressBar.setEnabled(False)
                    self.horizontalSlider.setEnabled(False)
                    # self.horizontalSlider.setValue(0)
                    # self.horizontalSlider.setMinimum(0)
                    return

            if shuzi in i[0][0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('存在相同序号')
                    for k in i[0]:
                        if k == i[0][0]:
                            continue
                        if k[0] == shuzi:
                            self.progressBar.setValue(k[1])
                            self.progressBar.setEnabled(False)
                            self.horizontalSlider.setEnabled(False)
                            # self.horizontalSlider.setMinimum(k[1])
                            # self.horizontalSlider.setValue(k[1])
                            break
                    return

            if int(shuzi) == shuzi:
                    shuzi = int(shuzi)
                    if shuzi-1 in i[0][0] or shuzi-1 in i[1][0]:
                        self.pushButton.setEnabled(True)
                        self.pushButton.setText('确定')
                        self.progressBar.setValue(0)
                        self.horizontalSlider.setMinimum(0)
                        self.horizontalSlider.setValue(0)
                        self.progressBar.setEnabled(True)
                        self.horizontalSlider.setEnabled(False)
                        self.spinBox.setEnabled(True)
                        self.spinBox.setValue(0)
                        return
                    else:
                        self.pushButton.setEnabled(False)
                        self.pushButton.setText(str(shuzi-1)+'还未创建')
                        self.progressBar.setValue(0)
                        self.progressBar.setEnabled(False)
                        self.horizontalSlider.setEnabled(False)
                        # self.horizontalSlider.setMinimum(0)
                        # self.horizontalSlider.setValue(0)
                        return

            if round(shuzi-0.01,2) in i[0][0]:
                    self.pushButton.setEnabled(True)
                    self.pushButton.setText('确定')
                    self.spinBox.setEnabled(False)
                    self.spinBox.clear()
                    for k in i[0]:
                        if k == i[0][0]:
                            continue
                        if k[0] == round(shuzi-0.01,2):
                            self.progressBar.setValue(k[1])
                            self.progressBar.setEnabled(True)
                            self.horizontalSlider.setEnabled(True)
                            self.horizontalSlider.setValue(k[1])
                            self.horizontalSlider.setMinimum(k[1])
                            break
                    return
            if int(shuzi) in i[0][0] and (round(shuzi-0.01,2) not in i[0][0]):
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('愿望'+str(round(shuzi-0.01,2))+'还未创建')
                    self.progressBar.setValue(0)
                    self.progressBar.setEnabled(False)
                    self.horizontalSlider.setEnabled(False)

                    return
            else:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText(str(int(shuzi))+'还未创建')
                    self.progressBar.setValue(0)
                    self.progressBar.setEnabled(False)
                    self.horizontalSlider.setEnabled(False)
                    # self.horizontalSlider.setValue(0)
                    # self.horizontalSlider.setMinimum(0)

        def queding():
            import datetime
            time = str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)+' '+str(datetime.datetime.today().hour)+':'+str(datetime.datetime.today().minute)
            global yuanwang,dianshu
            add = []
            zhuangru = []
            add.append(round(self.doubleSpinBox.value(),2))
            add.append(self.progressBar.value())
            if round(self.doubleSpinBox.value(),2) == int(round(self.doubleSpinBox.value(),2)):
                add.append(self.spinBox.value())
            else:
                add.append(0)
            add.append(self.plainTextEdit.toPlainText())
            add.append(self.plainTextEdit_2.toPlainText())
            add.append(time)
            yuanwang[0].append(add)
            yuanwang[0][0].append(add[0])

            if add[1] == 100:
                for i in yuanwang[0]:
                    if i == yuanwang[0][0]:
                        continue
                    if i[0] >= int(add[0]) and i[0]< int(add[0])+1:
                        zhuangru.append(i)
                for k in zhuangru:
                    if k[2]>0:
                        dianshu['d7']=int(dianshu['d7']+(50*(1.1**k[2])))
                    yuanwang[0].remove(k)
                    yuanwang[1].append(k)
                    yuanwang[0][0].remove(k[0])
                    yuanwang[1][0].append(k[0])

            yuanwang[0].sort(key= lambda x:x[0])
            yuanwang[1].sort(key= lambda x:x[0])

            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.destroy()

        def tuichu():
            Dialog.destroy()


        self.pushButton.clicked.connect(queding)
        self.doubleSpinBox.valueChanged.connect(jiemianxiaoyin)
        self.pushButton_2.clicked.connect(tuichu)








    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "请添加一个愿望或进度"))
        self.label_2.setText(_translate("Dialog", "愿望"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label.setText(_translate("Dialog", "请拖动滑块设定进度"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.label_3.setText(_translate("Dialog", "备注"))
        self.label_4.setText(_translate("Dialog", "序号"))
        self.label_5.setText(_translate("Dialog", "等级"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())