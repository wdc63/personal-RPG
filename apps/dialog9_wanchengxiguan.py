# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog9_wanchengxiguan.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 372)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 1, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def chushihua():
            self.listWidget.clear()
            self.listWidget_2.clear()
            global checkboxjinri,checkboxall
            checkboxjinri = []
            checkboxall = []
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path
            global count1,count2
            count1 = 1
            count2 = 1

            #### 初始化把今日习惯和所有习惯装载到两个列表当中，用checkbox的模式
            ###通过两个checkbox来获取它们是否勾选的值
            for i in xiguangeverday[0]:
                    if type(i) == int:
                        continue
                    if i ==[]:
                        continue
                    item = QtWidgets.QListWidgetItem()
                    value = '('+str(count1)+') '+i[0]
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    font = QtGui.QFont()
                    font.setPointSize(10)
                    item.setFont(font)
                    self.listWidget.addItem(item)
                    item1 = QtWidgets.QCheckBox(self.listWidget)
                    item1.setText(value)
                    item1.setToolTip(i[1])
                    self.listWidget.setItemWidget(item,item1)
                    checkboxjinri.append(item1)
                    count1 += 1

            for i in xiguanall:
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count2)+') '+i[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(10)
                item.setFont(font)
                #######################################
                self.listWidget_2.addItem(item)
                item1 = QtWidgets.QCheckBox(self.listWidget_2)
                item1.setText(value)
                item1.setToolTip(i[1])
                self.listWidget_2.setItemWidget(item,item1)
                if i in xiguangeverday[0]:
                    item1.setEnabled(False)
                checkboxall.append(item1)
                count2 += 1



        def queding():
            global checkboxjinri,checkboxall
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang

            ##今日习惯进行点数加成,并删掉已经加成的部分
            jinrishanchuxuhao = []
            for i in range(self.listWidget.count()):
                if checkboxjinri[i].isChecked():
                    jinrishanchuxuhao.append(i+3)
            jinrishanchuxuhao.reverse()
            for k in jinrishanchuxuhao:
                dianshu['d1'] = round(dianshu['d1'] + xiguangeverday[0][k][2],3)
                dianshu['d2'] = round(dianshu['d2'] + xiguangeverday[0][k][3],3)
                dianshu['d3'] = round(dianshu['d3'] + xiguangeverday[0][k][4],3)
                dianshu['d4'] = round(dianshu['d4'] + xiguangeverday[0][k][5],3)
                dianshu['d5'] = round(dianshu['d5'] + xiguangeverday[0][k][6],3)
                dianshu['d6'] = round(dianshu['d6'] + xiguangeverday[0][k][7],3)
                dianshu['d7'] = int(dianshu['d7'] + xiguangeverday[0][k][8])
                dianshu['d8'] = int(dianshu['d8'] + xiguangeverday[0][k][9])
                del  xiguangeverday[0][k]

            ##所有习惯进行点数加成,并删掉已经加成的部分
            for v in range(self.listWidget_2.count()):
                if checkboxall[v].isChecked():
                    dianshu['d1'] = round(dianshu['d1'] + xiguanall[v][2],3)
                    dianshu['d2'] = round(dianshu['d2'] + xiguanall[v][3],3)
                    dianshu['d3'] = round(dianshu['d3'] + xiguanall[v][4],3)
                    dianshu['d4'] = round(dianshu['d4'] + xiguanall[v][5],3)
                    dianshu['d5'] = round(dianshu['d5'] + xiguanall[v][6],3)
                    dianshu['d6'] = round(dianshu['d6'] + xiguanall[v][7],3)
                    dianshu['d7'] = int(dianshu['d7'] + xiguanall[v][8])
                    dianshu['d8'] = int(dianshu['d8'] + xiguanall[v][9])
            ##然后重写存档
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            if dianshu['d7']<0:
                dianshu['d7']=0
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            # print('yes')
            Dialog.close()


        chushihua()
        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(Dialog.close)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "完成习惯"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label.setText(_translate("Dialog", "完成每日习惯"))
        self.label_2.setText(_translate("Dialog", "完成额外其他习惯"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())