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

        del path
        self.listWidget.setWordWrap(True)
        count = 1
        for i in nengli:
                    item = QtWidgets.QListWidgetItem()
                    item.setCheckState(0)
                    value = '('+str(count)+') '+i[0]
                    item.setText(value)
                    item.setToolTip(i[1])
                    self.listWidget.addItem(item)
                    count +=1

        def queding():
            # print(jiangli)
            global nengli,dianshu
            add = []
            for i in range(self.listWidget.count()):
                if self.listWidget.item(i).checkState() == 2:
                    add.append(i)
            add.reverse()
            for i in add:
                dianshu['d1'] = round(dianshu['d1'] - nengli[i][2],3)
                dianshu['d2'] = round(dianshu['d2'] - nengli[i][3],3)
                dianshu['d3'] = round(dianshu['d3'] - nengli[i][4],3)
                dianshu['d4'] = round(dianshu['d4'] - nengli[i][5],3)
                dianshu['d5'] = round(dianshu['d5'] - nengli[i][6],3)
                dianshu['d6'] = round(dianshu['d6'] - nengli[i][7],3)
                del nengli[i]
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


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "删除能力"))
        self.pushButton.setText(_translate("Dialog", "确定删除"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
#
# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())