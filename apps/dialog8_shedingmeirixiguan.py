# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog8_shedingmeirixiguan.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("请选择需要添加的每日习惯，然后确定")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.chongzhixiguan = QtWidgets.QCheckBox(Dialog)
        self.chongzhixiguan.setText('重置每日习惯（谨慎！）')
        self.chongzhixiguan.setToolTip('当出现错误，例如存档时间不对引起的可能大量扣分或提示时间比最后存档还早时才使用，这会重置今日习惯中的内容')
        self.gridLayout.addWidget(self.chongzhixiguan, 1, 2, 1, 1)




        import datetime
        time = str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)
        self.label_2.setText(time)


        #### 初始化装载所有的习惯，和删除习惯是一模一样的
        def chushihua():
            self.listWidget.clear()
            global allcheckbox
            allcheckbox = []
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path
            global count
            count = 1
            for i in xiguanall:
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count)+') '+i[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(10)
                item.setFont(font)
                #######################################
                self.listWidget.addItem(item)
                item1 = QtWidgets.QCheckBox(self.listWidget)
                item1.setText(value)
                item1.setToolTip(i[1])
                if i in xiguangeverday[0]:
                    item1.setEnabled(False)
                self.listWidget.setItemWidget(item,item1)
                allcheckbox.append(item1)
                count += 1

        #### 点选重置时的显示
        global yes
        yes = 0
        #### 点选重置时的显示
        def chongzhixianshi():
            global allcheckbox,yes
            # print(yes)
            if yes == 0:
               for i in allcheckbox:
                   i.setEnabled(False)
                   # print(i)
               yes = 1

               return
            if yes == 1:
               # for i in allcheckbox:
               #     i.setEnabled(True)
               yes = 0
               chushihua()
               return

        self.chongzhixiguan.clicked.connect(chongzhixianshi)


        #### 确定之后的今日习惯变量装载
        def queding():
            global allcheckbox
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            import datetime
            if self.chongzhixiguan.isChecked():
                xiguangeverday = [[datetime.date.today().year,datetime.date.today().month,datetime.date.today().day],'习惯存档时间已经被重置到今天并清空，没有进行任何分数加成。']
                import pickle
                path = open('D:/MyRPG/data.dat','wb')
                pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
                path.close()
                del path
                Dialog.close()
                return
            if xiguangeverday[0][0]==datetime.date.today().year and xiguangeverday[0][1] == datetime.date.today().month and xiguangeverday[0][2]==datetime.date.today().day:
              for i in range(self.listWidget.count()):
                if allcheckbox[i].isChecked():
                    xiguangeverday[0].append(xiguanall[i])
              import pickle
              path = open('D:/MyRPG/data.dat','wb')
              pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
              path.close()
              del path
              # print(xiguangeverday)
              Dialog.close()

            else:
                self.pushButton.setText('存档已经跨天，请重启主程序完成分数加成')
                return

        chushihua()
        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加每日习惯"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())