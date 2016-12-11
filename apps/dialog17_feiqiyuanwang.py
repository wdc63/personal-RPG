# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog17_feiqiyuanwang.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 341)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        import pickle
        path = open('D:/MyRPG/data.dat','rb')
        global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
        dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
        path.close()
        # print(yuanwang)
        del path
        self.listWidget.setWordWrap(True)
        for i in yuanwang[0]:
            if i == yuanwang[0][0]:
                continue
            else:
                if i[0] == int(i[0]):
                    item = QtWidgets.QListWidgetItem()
                    item.setCheckState(0)
                    value = str(int(i[0]))+' ('+i[5]+')：'+i[3]
                    item.setText(value)
                    item.setToolTip('等级：'+str(i[2])+'<br/>'+i[4])
                    item.setWhatsThis(str(i[0]))
                    self.listWidget.addItem(item)

        def queding():
            import dialog17fujia_jinggao
            Dialog = QtWidgets.QDialog()
            ui = dialog17fujia_jinggao.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(zaiciqueding)

        def zaiciqueding():
            global yuanwang
            add = []
            for i in range(self.listWidget.count()):
                if self.listWidget.item(i).checkState() == 2:
                    for k in yuanwang[0]:
                        if k[0] == int(float(self.listWidget.item(i).whatsThis())):
                            add.append(k)
                        if k[0] > int(float(self.listWidget.item(i).whatsThis())) and k[0] < int(float(self.listWidget.item(i).whatsThis()))+1 :
                            add.append(k)
                else:
                    continue
            for i in add:
                yuanwang[0].remove(i)
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.accept()
            Dialog.destroy()
        def tuichu():
            Dialog.destroy()

        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(tuichu)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "废弃愿望"))
        self.pushButton.setText(_translate("Dialog", "确定废弃"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())