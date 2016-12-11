# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog12_chuangjianrizhi.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 356)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 5, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 7)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 2, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 6, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 6, 0, 1, 7)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setText("请输入备注<span style=\" color:#ff0000;\">"+'（请手动换行）'+"</span>")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 5, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 6, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ####读取变量
        import pickle
        path = open('D:/MyRPG/data.dat','rb')
        global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
        dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
        path.close()
        del path


        #### 按键的基本条件控制，包括加点限定，时间设定，过程任务开关等
        self.doubleSpinBox.setSingleStep(0.0001)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMinimum(1)
        self.doubleSpinBox.setMaximum(99999)
        self.doubleSpinBox.clear()

        self.pushButton.setEnabled(False)
        self.pushButton.setText('请输入序号')

        self.spinBox.setMaximum(500)
        self.spinBox.setMinimum(0)
        self.spinBox.setValue(20)
        self.spinBox_2.setMaximum(50)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setValue(10)
        if rizhi == [[0,0]]:
                    self.doubleSpinBox.setValue(1)
                    self.pushButton.setEnabled(True)
                    self.pushButton.setText('目前只能添加任务1')


        def jiemianxiaoyin():
            global rizhi,rizhifinish
            shuzi = round(self.doubleSpinBox.value(),4)
            for i in rizhifinish:
                if int(shuzi) == i[1]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(i[1])+'已经完成')
                    return
            ### 需要纂写当任务日志中存在冲突条目的时候，pushbutton消隐掉

            else:
                shuzi = round(self.doubleSpinBox.value(),4)
                if shuzi == int(shuzi):
                    shuzi = int(shuzi)
                if shuzi in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('存在相同序号')
                # elif  '0' in str(shuzi-int(shuzi))[:-1]:
                elif  shuzi!=int(shuzi) and  '0' in str(shuzi).split('.')[1]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('序号不正确')
                elif shuzi == int(shuzi):
                    if shuzi-1 in rizhi[0]:
                         self.pushButton.setEnabled(True)
                         self.pushButton.setText('确定')
                    else:
                         self.pushButton.setEnabled(False)
                         self.pushButton.setText(str(shuzi-1)+'还未创建')
                elif round(float(str(shuzi)[:-1]),4) in rizhi[0]:
                    if round(float(str(shuzi)[:-1]+str(int(str(shuzi)[-1])-1)),4) in rizhi[0]:
                        self.pushButton.setEnabled(True)
                        self.pushButton.setText('确定')
                    else:
                        self.pushButton.setEnabled(False)
                        self.pushButton.setText('任务'+(str(shuzi)[:-1]+str(int(str(shuzi)[-1])-1))+'还未创建')
                else:
                        a = round(float(str(round(self.doubleSpinBox.value(),4))[:-1]),4)
                        self.pushButton.setEnabled(False)
                        self.pushButton.setText('任务'+str(a)+'还未创建')

            if self.doubleSpinBox.value() == int(self.doubleSpinBox.value()):
                self.label_6.setEnabled(True)
                self.comboBox.setEnabled(True)
                self.label_3.setEnabled(True)
                self.label_4.setEnabled(True)
                self.label_5.setEnabled(True)
                self.spinBox.setEnabled(True)
                self.spinBox_2.setEnabled(True)
            else :
                self.label_6.setEnabled(False)
                self.comboBox.setEnabled(False)
                self.label_3.setEnabled(False)
                self.label_4.setEnabled(False)
                self.label_5.setEnabled(False)
                self.spinBox.setEnabled(False)
                self.spinBox_2.setEnabled(False)

        def queding():
            global rizhi
            add = []
            if round(self.doubleSpinBox.value(),4) == int(self.doubleSpinBox.value()):
                add.append(self.comboBox.currentText())
            else:
                add.append('')
            if round(self.doubleSpinBox.value(),4) == int(self.doubleSpinBox.value()):
                add.append(int(round(self.doubleSpinBox.value(),4)))
            else:
                add.append(round(self.doubleSpinBox.value(),4))

            add.append(self.textEdit.toPlainText())
            add.append(self.textEdit_2.toPlainText())
            rizhi[0].append(round(self.doubleSpinBox.value(),4))
            if round(self.doubleSpinBox.value(),4) == int(self.doubleSpinBox.value()):
                add.append(self.spinBox.value())
                add.append(self.spinBox_2.value())
            else:
                add.append(0)
                add.append(0)
            import datetime
            jintian = str(datetime.date.today())
            time = str(datetime.datetime.today().hour)+':'+str(datetime.datetime.today().minute)
            now = jintian+' '+time
            add.append(now)
            rizhi.append(add)
            rizhi[0].sort()
            rizhi.sort(key = lambda x:x[1])
            # print(rizhi)
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.destroy()

        def tuichu():
            Dialog.destroy()


        self.doubleSpinBox.valueChanged.connect(jiemianxiaoyin)
        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(tuichu)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加日志"))
        self.label_3.setText(_translate("Dialog", "任务奖励"))
        self.label_5.setText(_translate("Dialog", "娱乐点："))
        self.label_6.setText(_translate("Dialog", "主/支线任务"))
        self.label.setText(_translate("Dialog", "请输入日志内容"))
        self.comboBox.setItemText(0, _translate("Dialog", "支线任务"))
        self.comboBox.setItemText(1, _translate("Dialog", "主线任务"))
        self.label_2.setText(_translate("Dialog", "日志序号"))
        self.label_4.setText(_translate("Dialog", "经验："))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())