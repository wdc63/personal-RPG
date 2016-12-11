# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog13wanchengrenwu.ui'
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
        Dialog.resize(468, 395)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 4)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        import pickle
        path = open('D:/MyRPG/data.dat','rb')
        global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
        dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
        path.close()
        del path
        self.treeWidget.clear()
        self.treeWidget.setIndentation(10)
        self.treeWidget.setWordWrap(True)
        for i in rizhi:
                if i == rizhi[0]:
                    continue
                else:
                    if i[1] == int(i[1]):
                        ##添加一个主任务显示对象，并添加背景，装载Qlabel对象
                        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                        item_0.setCheckState(0,0)
                        brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        brush2 = QtGui.QBrush(QtGui.QColor(180, 250, 251))
                        brush2.setStyle(QtCore.Qt.SolidPattern)
                        value = str(i[1])+'.'+i[0]+'：'+i[2]
                        font = QtGui.QFont()
                        font.setBold(True)
                        font.setPointSize(10)
                        item_0.setFont(0,font)
                        if i[0] =='主线任务':
                            item_0.setBackground(0, brush)
                            item_0.setText(0,value)
                        else:
                            item_0.setBackground(0, brush2)
                            item_0.setText(0,value)
                        item_0.setWhatsThis(0,str(i[1]))
                        item_0.setToolTip(0,'添加时间：'+i[6]+'；'+'奖励经验：'+str(i[4])+'，娱乐点：'+str(i[5])+'\n'+'备注：'+i[3])
                        continue

        def queding():
            ## add 新增对象，只新增了日志的标题一级
            global dianshu, rizhi,rizhifinish,add
            import datetime
            time = '完成时间：'+str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)+' '+str(datetime.datetime.today().hour)+':'+str(datetime.datetime.today().minute)
            add2 = [] ###用于删除日志中的对象
            for i in range(self.treeWidget.topLevelItemCount()):
                ###第二次循环这里没有错误
                if self.treeWidget.topLevelItem(i).checkState(0) == 2:
                    for k in rizhi:
                        if k[1]==int(self.treeWidget.topLevelItem(i).whatsThis(0)) :
                            import copy
                            add2.append(k)
                            s = copy.deepcopy(k)
                            s.append(time)
                            add.insert(0,s)
                            dianshu['d7'] = dianshu['d7']+k[4]
                            dianshu['d8'] = dianshu['d8']+k[5]
                            rizhifinish.insert(0,s)
                        if k[1]> int(self.treeWidget.topLevelItem(i).whatsThis(0))  and  k[1]<(int(self.treeWidget.topLevelItem(i).whatsThis(0))+1):
                            add2.append(k)
                            rizhifinish[0].append(k)
            for i in add2:
                rizhi.remove(i)
            # print(rizhifinish)
            # print(rizhi)
            # print(add)
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.destroy()

        def feiqirenwu1():
            import dialog13fujia_jinggao
            Dialog = QtWidgets.QDialog()
            ui = dialog13fujia_jinggao.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(feiqirenwu)

        def feiqirenwu():
            global rizhi
            add2 = []
            for i in range(self.treeWidget.topLevelItemCount()):
                if self.treeWidget.topLevelItem(i).checkState(0) == 2:
                    for k in rizhi:
                        if k[1]==int(self.treeWidget.topLevelItem(i).whatsThis(0)) :
                            add2.append(k)
                        if k[1]> int(self.treeWidget.topLevelItem(i).whatsThis(0))  and  k[1]<(int(self.treeWidget.topLevelItem(i).whatsThis(0))+1):
                            add2.append(k)
            for i in add2:
                rizhi.remove(i)
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
        self.pushButton_2.clicked.connect(feiqirenwu1)
        self.pushButton_3.clicked.connect(tuichu)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "任务日志完成"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.pushButton_2.setText(_translate("Dialog", "无法完成"))
        self.pushButton.setText(_translate("Dialog", "完成任务"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "所有进行中任务"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())