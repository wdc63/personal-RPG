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
        Dialog.resize(535, 422)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 0, 1, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout.addWidget(self.spinBox_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 6, 0, 1, 9)
        self.label_7 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 8, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 6, 1, 2, QtCore.Qt.AlignHCenter)
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
        self.gridLayout.addWidget(self.comboBox, 0, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 9)
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout.addWidget(self.spinBox_6, 0, 4, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout.addWidget(self.spinBox_5, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 7, 1, 1, QtCore.Qt.AlignRight)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 8, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        #### 约束各个spinbox数字规则和按钮的初始显示
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(99999)
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(999)
        self.spinBox_5.setMinimum(0)
        self.spinBox_5.setMaximum(99)
        self.spinBox_6.setMinimum(0)
        self.spinBox_6.setMaximum(99)
        ### 初始化按钮
        self.pushButton.setText('请输入序号')
        self.pushButton.setEnabled(False)
        ### 经验部分
        self.spinBox.setMaximum(500)
        self.spinBox.setMinimum(0)
        self.spinBox.setValue(20)
        self.spinBox_2.setMaximum(50)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setValue(10)

        ###读取变量
        import pickle
        path = open('D:/MyRPG/data.dat','rb')
        global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
        dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
        path.close()
        del path

        ###关键的界面变化部分
        def jiemianguizhe():
            global rizhi,rizhifinish
            # print(rizhi)
            ### 首先控制界面上能够设定部分的开关
            value = round(self.spinBox_3.value()+self.spinBox_4.value()/1000+self.spinBox_5.value()/100000+self.spinBox_6.value()/10000000,7)
            t1 = self.spinBox_3.value()
            t2 = round(self.spinBox_4.value()/1000,3)
            t3 = round(self.spinBox_5.value()/100000,5)
            t4 = round(self.spinBox_6.value()/10000000,7)
            if int(value) == value:
                self.label_6.setEnabled(True)
                self.comboBox.setEnabled(True)
                self.label_3.setEnabled(True)
                self.label_4.setEnabled(True)
                self.label_5.setEnabled(True)
                self.spinBox.setEnabled(True)
                self.spinBox_2.setEnabled(True)
            else:
                self.label_6.setEnabled(False)
                self.comboBox.setEnabled(False)
                self.label_3.setEnabled(False)
                self.label_4.setEnabled(False)
                self.label_5.setEnabled(False)
                self.spinBox.setEnabled(False)
                self.spinBox_2.setEnabled(False)
            ###判断是否是空日志
            if rizhi == [[0,0]]:
                self.spinBox_3.setValue(1)
                self.spinBox_4.setValue(0)
                self.spinBox_5.setValue(0)
                self.spinBox_6.setValue(0)
                self.pushButton.setText('目前只能添加任务1')
                self.pushButton.setEnabled(True)
                return
            ###判断是否是已完成日志，如果太卡，这个可以删除
            for i in rizhifinish:
                if int(value) == i[1]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(i[1])+'已经完成')
                    return
            ####判断是否是根标题，是否是整数t2,t3,t4都=0
            if int(value) == value:
                if value in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(int(value))+'已经创建')
                    return
                if value not in  rizhi[0]:
                    if int(value)-1 in rizhi[0] and int(value)-1 != 0:
                        self.pushButton.setEnabled(True)
                        self.pushButton.setText('确定')
                        return
                    else:
                        self.pushButton.setEnabled(False)
                        self.pushButton.setText('任务'+str(int(value)-1)+'还未创建')
            #### 判断是否是第一层日志
            if t3 == 0 and t4 == 0 and t1 !=0:
                if int(value) not in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(int(value))+'还未创建')
                    return
                if value in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(value)+'已经创建')
                    return
                if round(value - 0.001,3) in rizhi[0]:
                    self.pushButton.setEnabled(True)
                    self.pushButton.setText('确定')
                    return
                else :
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str( round(value - 0.001,3))+'还未创建')
                    return
            ####判断是否是第二层日志
            if t4 == 0 and t3!= 0:
                ###首先如果第二层不为0的化第一层为0是不合法的
                if t2 == 0:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务序号错误')
                    return
                ###开始正式判断
                if int(value) not in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(int(value))+'还未创建')
                    return
                if round(t1+t2,3) not in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(round(t1+t2,3))+'还未创建')
                    return
                if round(t1+t2+t3,5) in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(round(t1+t2+t3,5))+'已经创建')
                    return
                if round(t1+t2+t3-0.00001,5) in rizhi[0]:
                    self.pushButton.setEnabled(True)
                    self.pushButton.setText('确定')
                    return
                else :
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(round(t1+t2+t3-0.00001,5))+'还未创建')
                    return

            ####判断是否是第三层日志
            if  t4 != 0:
                ###首先如果第二层不为0的化第一层为0是不合法的
                if t2 == 0 or t3 == 0:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务序号错误')
                    return
                ### 开始正式判断
                if int(value) not in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(int(value))+'还未创建')
                    return
                if round(t1+t2,3) not in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(round(t1+t2,3))+'还未创建')
                    return
                if round(t1+t2+t3,5) not in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(round(t1+t2+t3,5))+'还未创建')
                    return
                if value in rizhi[0]:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(value)+'已经创建')
                    return
                if round(value-0.0000001,7) in rizhi[0]:
                    self.pushButton.setEnabled(True)
                    self.pushButton.setText('确定')
                    return
                else:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setText('任务'+str(round(value-0.0000001,7))+'还未创建')
                    return

        ### 确定，擦太桑脑筋了
        def queding():
            global rizhi
            add = []
            value = round(self.spinBox_3.value()+self.spinBox_4.value()/1000+self.spinBox_5.value()/100000+self.spinBox_6.value()/10000000,7)
            ##参数1 主线任务和支线任务标签
            if value == int(value):
                add.append(self.comboBox.currentText())
            else:
                add.append('')
            ##参数2 是否变成整数
            if value == int(value):
                add.append(int(value))
            else:
                add.append(value)
            ##参数3和4 名字和备注
            add.append(self.textEdit.toPlainText())
            add.append(self.textEdit_2.toPlainText())
            ##第一个变量装入序号
            rizhi[0].append(value)
            ## 参数5和6 经验和娱乐点，子任务添加0
            if value == int(value):
                add.append(self.spinBox.value())
                add.append(self.spinBox_2.value())
            else:
                add.append(0)
                add.append(0)
            ##末尾装入时间
            import datetime
            jintian = str(datetime.date.today())
            time = str(datetime.datetime.today().hour)+':'+str(datetime.datetime.today().minute)
            now = jintian+' '+time
            add.append(now)
            rizhi.append(add)
            ##对首变量和日志其他变量排序
            rizhi[0].sort()
            rizhi.sort(key = lambda x:x[1])
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.destroy()
        def tuichu():
            Dialog.destroy()

        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(tuichu)

        self.spinBox_3.valueChanged.connect(jiemianguizhe)
        self.spinBox_4.valueChanged.connect(jiemianguizhe)
        self.spinBox_5.valueChanged.connect(jiemianguizhe)
        self.spinBox_6.valueChanged.connect(jiemianguizhe)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "创建日志"))
        self.label_3.setText(_translate("Dialog", "任务奖励"))
        self.label_7.setText(_translate("Dialog", "请输入备注"+"<span style=\" color:#ff0000;\">（请手动换行）</span>"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label_6.setText(_translate("Dialog", "主/支线任务"))
        self.label.setText(_translate("Dialog", "请输入日志内容"))
        self.comboBox.setItemText(0, _translate("Dialog", "支线任务"))
        self.comboBox.setItemText(1, _translate("Dialog", "主线任务"))
        self.label_2.setText(_translate("Dialog", "日志序号"))
        self.label_5.setText(_translate("Dialog", "娱乐点："))
        self.label_4.setText(_translate("Dialog", "经验："))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())