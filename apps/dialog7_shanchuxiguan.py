# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog7_shanchuxiguan.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
global allcheckbox,quedingcishu
allcheckbox = []
quedingcishu = 0
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 330)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ####初始化并装载列表，注意allcheckbox装入了所有的checkbox以在后面验证用户是否点选
        def chushihua():
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
            self.listWidget.setWordWrap(True)
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
                self.listWidget.setItemWidget(item,item1)
                allcheckbox.append(item1)
                count += 1

        def queding():
            global quedingcishu
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            ##第一次确定
            if quedingcishu == 0:
                self.pushButton.setText('请再次确定')
                quedingcishu = 1
                return
            ##第二次确定，删除xiguanall中的所有选中索引
            if quedingcishu == 1:
                import pickle
                global allcheckbox
                shanchuxuhao = []
                for i in range(self.listWidget.count()):
                    if allcheckbox[i].isChecked():
                        shanchuxuhao.append(i)
                shanchuxuhao.reverse()
                for k in  shanchuxuhao:
                    del xiguanall[k]

                #然后重写存档
                path = open('D:/MyRPG/data.dat','wb')
                pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
                path.close()
                del path

                #清空allcheckbox，重置确定次数和确定按钮
                allcheckbox = []
                quedingcishu = 0
                self.pushButton.setText('确定')
                Dialog.destroy()

        def tuichu():
            global quedingcishu
            quedingcishu = 0
            Dialog.destroy()

        chushihua()
        self.pushButton.clicked.connect(queding)
        self.pushButton_2.clicked.connect(tuichu)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "删除习惯"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label.setText(_translate("Dialog", "请选择需要删除的习惯，然后确定"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())