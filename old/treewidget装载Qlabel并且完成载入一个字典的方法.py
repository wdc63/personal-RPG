# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(939, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setToolTip("")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "任务日志-进行中")



        #####字典读取并显示到界面上的方法
        kaishiceshi =  {1:'水电费撒的的算法啊啊啊啊啊啊啊啊啊啊啊啊阿斯顿飞凤飞飞凤飞的撒范德萨发撒的发顺丰撒发生飞洒安顺是十三十四是十三十四飞凤飞飞凤飞飞发顺丰', 1.1:'但是发生范德萨多发点十分发达',2:'说的发生发疯的萨法',2.1:'''都舒服撒地方撒范德萨发撒分
       的撒发多少''',2.2:'yessdf',2.21:'adsfadsfasdf', 3:'dsafsafsdfa说的分手大法师地方'}
        list1 = []
        list2 = []
        for k,v in kaishiceshi.items():
            list1.append(k)
            list2.append(v)
        paixurizhi = list(zip(list1,list2))
        paixurizhi.sort()
        self.treeWidget.clear()
        print(paixurizhi)
        self.treeWidget.setIndentation(10)
        for i in paixurizhi:
             if i[0] == int(i[0]):
                item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                item_0.setFont(2,font)
                neirong = QtWidgets.QLabel(self.treeWidget)
                neirong.setText(str(i[0])+'：'+i[1])
                neirong.setWordWrap(True)
                neirong.setFixedHeight(30)  ##类似于之前的font尺寸，我牛逼吧
                neirong.setFont(font)
                neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                self.treeWidget.setItemWidget(item_0,0,neirong)
                continue
             if i[0]*10 == int(i[0]*10):
                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                neirong = QtWidgets.QLabel(self.treeWidget)
                neirong.setText(str(i[0])+'：'+i[1])
                neirong.setWordWrap(True)
                neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                self.treeWidget.setItemWidget(item_1,0,neirong)
                continue
             if i[0]*100 == int(i[0]*100):
                item_2 = QtWidgets.QTreeWidgetItem(item_1)
                neirong = QtWidgets.QLabel(self.treeWidget)
                neirong.setText(str(i[0])+'：'+i[1])
                neirong.setWordWrap(True)
                neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                self.treeWidget.setItemWidget(item_2,0,neirong)
                continue
             else:
                continue

        #在treewiget中建立一个qlable的例子###
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        nimabi = QtWidgets.QLabel(self.treeWidget)
        nimabi.setText('sdvsdf到到发fafa都舒服撒到发ffsdafads是对方的萨法娃儿额外热温柔体育图样图用途撒到发fgghj')
        nimabi.setWordWrap(True)
        self.treeWidget.setItemWidget(item_0,0,nimabi)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        nimab2 = QtWidgets.QLabel(self.treeWidget)
        nimab2.setText('sdv撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fgghj')
        nimab2.setWordWrap(True)
        nimab2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.treeWidget.setItemWidget(item_1,0,nimab2)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        nimab2 = QtWidgets.QLabel(self.treeWidget)
        nimab2.setText('sdvsdfsdfffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fgghj')
        nimab2.setWordWrap(True)
        self.treeWidget.setItemWidget(item_1,0,nimab2)

        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        nimab2 = QtWidgets.QLabel(self.treeWidget)
        nimab2.setText('sdv舒服撒到发f都舒服发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fffa都舒服撒到发fgghj')
        nimab2.setWordWrap(True)
        self.treeWidget.setItemWidget(item_2,0,nimab2)
        #在treewiget中建立一个qlable的例子###









        self.horizontalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())