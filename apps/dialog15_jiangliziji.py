# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog15_jiangliziji.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 352)
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
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def dudang():
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path
        dudang()
        self.label_2.setText('娱乐点剩余：'+"<span style=\" font-size:10pt; font-weight:bold;color:#00df00;\">"+str(dianshu['d8'])+"</span>")
        global count7
        count7 = 1
        self.listWidget.clear()
        self.listWidget.setWordWrap(True)
        for i in jiangli:
            item = QtWidgets.QListWidgetItem()
            value = '('+str(count7)+') '+i[0]+'(将消耗'+str(i[2])+'点娱乐点)'
            item.setText(value)
            item.setToolTip(i[1])
            item.setCheckState(0)
            self.listWidget.addItem(item)
            count7 += 1

        def queding():
            import datetime
            time = str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)+' '+str(datetime.datetime.today().time().hour)+':'+str(datetime.datetime.today().time().minute)
            global jiangli,jiangliget,dianshu,add
            add = []
            for i in range(self.listWidget.count()):

                if int(self.listWidget.item(i).checkState()) == 2:
                    import copy
                    s = copy.deepcopy(jiangli[i])
                    s.insert(0,time)
                    jiangliget.insert(0,s)
                    dianshu['d8'] = dianshu['d8']-jiangli[i][2]
                    add.insert(0,s)
            if dianshu['d8']<0:
                self.pushButton.setText('娱乐点不足')
                add = []
                dudang()
                return
            else:
                import pickle
                path = open('D:/MyRPG/data.dat','wb')
                pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
                path.close()
                del path
                Dialog.destroy()

        def tuichu():
            Dialog.destroy()
        def quedingchongzhi():
            self.pushButton.setText('获得奖励')
            fenshu = 0
            for i in range(self.listWidget.count()):
                if int(self.listWidget.item(i).checkState()) == 2:
                    fenshu = fenshu + jiangli[i][2]
            if fenshu == 0:
                self.label_3.setText('')
            else:
                self.label_3.setText('所选娱乐点：'+"<span style=\" font-size:10pt; font-weight:bold;color:#ff0000;\">"+str(fenshu)+"</span>")

        self.pushButton.clicked.connect(queding)
        self.pushButton_3.clicked.connect(tuichu)
        self.listWidget.itemPressed.connect(quedingchongzhi)
        self.listWidget.itemClicked.connect(quedingchongzhi)






    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "奖励自己"))
        self.pushButton.setText(_translate("Dialog", "获得奖励"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", "所有奖励列表"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())