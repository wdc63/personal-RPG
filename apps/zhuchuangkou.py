# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuchuangkou.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
global zengliangnengli,zengliangzhuangbei,zengliangxiguanall,countrizhizhuxian,countrizhizhixian,zengliangwanchengrizhi,dayyourenwu2,zengliangjiangli
countrizhizhuxian = 0
countrizhizhixian = 0
zengliangnengli = []
zengliangzhuangbei = []
zengliangxiguanall = []
zengliangwanchengrizhi = []
dayyourenwu2 = []
zengliangjiangli = []
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        #####最外层的主窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 546)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        ####第一个页面，新增的作息安排
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_14)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.tab_14)
        self.label_15.setObjectName("label_15")
        self.label_15.setText('今日作息安排')
        self.verticalLayout_3.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_14)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.setText('编辑')
        self.verticalLayout_3.addWidget(self.pushButton_21)
        self.tabWidget.addTab(self.tab_14, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14),'今日作息')

        #### 开始第一个tab页面
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 311, 210))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_10.addWidget(self.scrollArea_4, 1, 0, 1, 2)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_10.addWidget(self.pushButton_13, 2, 0, 1, 1)
        self.zhuangbei = QtWidgets.QLabel(self.tab)
        self.zhuangbei.setObjectName("zhuangbei")
        self.gridLayout_10.addWidget(self.zhuangbei, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab)
        self.pushButton_16.setText("卸下")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_10.addWidget(self.pushButton_16, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_10, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.jingyanheyuledian = QtWidgets.QLabel(self.tab)
        self.jingyanheyuledian.setObjectName("jingyanheyuledian")
        self.verticalLayout_2.addWidget(self.jingyanheyuledian, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 311, 115))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setToolTip("")
        self.label_13.setText("经验：")
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setToolTip("")
        self.label_14.setText("娱乐点：")
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.jibenshuxingdian = QtWidgets.QLabel(self.tab)
        self.jibenshuxingdian.setObjectName("jibenshuxingdian")
        self.verticalLayout.addWidget(self.jibenshuxingdian, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 312, 115))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setToolTip("")
        self.label_3.setText("体质：")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setToolTip("")
        self.label_4.setText("体重：")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setToolTip("")
        self.label_5.setText("耐力：")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.gridLayout_4.addLayout(self.verticalLayout_11, 0, 0, 4, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_13.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addLayout(self.verticalLayout_13, 3, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setToolTip("")
        self.label_2.setText("专注：")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setToolTip("")
        self.label.setText("智力：")
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setToolTip("")
        self.label_12.setText("知识量：")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 1, 3, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_11.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 312, 210))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_4)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.addWidget(self.scrollArea_3, 1, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_11.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.tianfuhenengli = QtWidgets.QLabel(self.tab)
        self.tianfuhenengli.setObjectName("tianfuhenengli")
        self.gridLayout_11.addWidget(self.tianfuhenengli, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab)
        self.pushButton_17.setText("删除")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_11.addWidget(self.pushButton_17, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_11, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")

        ####开始第二个tab页面
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_shanxiguan = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_shanxiguan.setObjectName("pushButton_shanxiguan")
        self.pushButton_shanxiguan.setText("删除习惯")
        self.gridLayout_7.addWidget(self.pushButton_shanxiguan, 2, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_7.addWidget(self.pushButton_5, 2, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_7.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_4.setObjectName("listWidget_4")
        self.gridLayout_7.addWidget(self.listWidget_4, 1, 3, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_7.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_7.addWidget(self.listWidget_3, 1, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        ####开始第三个tab页面
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_6.addWidget(self.calendarWidget, 0, 3, 2, 2)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 12))
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 2, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "最近200条（默认）")
        self.comboBox.addItem("")
        self.comboBox.setItemText(1, "显示全部")
        self.gridLayout_6.addWidget(self.comboBox, 2, 4, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_6.addWidget(self.pushButton_7, 4, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_6.addWidget(self.pushButton_10, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 12))
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.listWidget_5 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_5.setObjectName("listWidget_5")
        self.gridLayout_6.addWidget(self.listWidget_5, 1, 0, 3, 3)
        self.listWidget_6 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_6.setObjectName("listWidget_6")
        self.gridLayout_6.addWidget(self.listWidget_6, 3, 3, 2, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.radioButton = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_6.addWidget(self.radioButton, 0, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton.setText('按重要性排序')
        self.radioButton_2.setText('按类型排序')
        self.gridLayout_6.addWidget(self.radioButton_2, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        ####开始第四个tab页面
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setObjectName("label_15")
        self.label_15.setText('按钮')
        self.gridLayout_2.addWidget(self.label_15, 0, 3, 1, 1)
        self.comboBoxrizhi = QtWidgets.QComboBox(self.tab_4)
        self.comboBoxrizhi.addItem('')
        self.comboBoxrizhi.setItemText(0, "200条")
        self.comboBoxrizhi.addItem('')
        self.comboBoxrizhi.setItemText(1, "全部")
        self.gridLayout_2.addWidget(self.comboBoxrizhi, 0, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 4, 1, 1)
        self.listrizhiwancheng = QtWidgets.QListWidget(self.tab_4)
        self.listrizhiwancheng.setObjectName("rizhiwancheng")
        self.listrizhiwancheng.setFixedWidth(267)
        self.gridLayout_2.addWidget(self.listrizhiwancheng, 1, 3, 1, 2)
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_4)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_2.addWidget(self.treeWidget, 0, 1, 4, 1)
        self.treeWidget.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.listrizhiwancheng.raise_()
        self.tabWidget.addTab(self.tab_4, "")

        ####开始第五个tab页面
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "最近200条（默认）")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(1, "显示全部")
        self.gridLayout_8.addWidget(self.comboBox_3, 0, 6, 1, 1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_8.addWidget(self.pushButton_12, 2, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 0, 5, 1, 1, QtCore.Qt.AlignLeft)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_8.addWidget(self.pushButton_11, 2, 0, 1, 1)
        self.listWidget_7 = QtWidgets.QListWidget(self.tab_5)
        self.listWidget_7.setObjectName("listWidget_7")
        self.gridLayout_8.addWidget(self.listWidget_7, 1, 0, 1, 2)
        self.listWidget_8 = QtWidgets.QListWidget(self.tab_5)
        self.listWidget_8.setObjectName("listWidget_8")
        self.gridLayout_8.addWidget(self.listWidget_8, 1, 5, 1, 2)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_8.addWidget(self.pushButton_15, 2, 1, 1, 1)
        self.pushButton_15.setText('删除奖励')
        self.tabWidget.addTab(self.tab_5, "")

        ####开始第六个tab页面
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.tab_6)
        self.treeWidget_3.setObjectName("treeWidget_3")
        self.treeWidget_3.headerItem().setText(0, "列表")
        self.gridLayout_9.addWidget(self.treeWidget_3, 0, 0, 1, 3)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_9.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(160, 0))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "已完成显示100条（默认）")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(1, "显示全部")
        self.gridLayout_9.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_14.setText("废弃愿望")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_9.addWidget(self.pushButton_14, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")

        ####工具集的tab页面
        self.tab_fujia = QtWidgets.QWidget()
        self.tab_fujia.setObjectName("tab_fujia")
        self.tabWidget.addTab(self.tab_fujia, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fujia),'附加工具')
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_fujia)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_fujia)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setText("番茄工作法")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_12.addWidget(self.pushButton_18, 0, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_fujia)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setText("今日信息")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_12.addWidget(self.pushButton_19, 0, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_fujia)
        self.pushButton_20.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setText("桌面便签")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_12.addWidget(self.pushButton_20, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem1, 1, 0, 1, 1)

        def dakaifanqie():
            import fanqie
            fanqie.Dialog.show()
        self.pushButton_18.clicked.connect(dakaifanqie)

        def dakairili():
            import subprocess
            subprocess.Popen('1.bat')
        self.pushButton_19.clicked.connect(dakairili)

        def openbianqian():
            import subprocess
            subprocess.Popen('StikyNot.exe')
        self.pushButton_20.clicked.connect(openbianqian)

        ####界面的菜单栏等剩余其他部分
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #### 初始化读取所有变量档案，如果不存在档案就新建档案#
        def chushihua():
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            import os
            import pickle
            if os.path.exists('D:/MyRPG/data.dat'):
                path = open('D:/MyRPG/data.dat','rb')
                try:
                    dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
                except:
                    import dialog1_cundangbucunzai
                    dialog1_cundangbucunzai.Dialog.show()
                    dianshu={'d1':0,'d2':0,'d3':0,'d4':0,'d5':0,'d6':0,'d7':0,'d8':0}
                    nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,jiangli,jiangliget = [],[],[],[],[],[],[],[]
                    rizhi,rizhifinish,yuanwang = [[0,0]],[],[[[0]],[[0]]]
                    try:
                       os.mkdir('D:/MyRPG')
                    except:
                       pass
                    path = open('D:/MyRPG/data.dat','wb')
                    pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
                    path.close()
                    del path
                    return
                path.close()
                del path
            else:
                import dialog1_cundangbucunzai
                dialog1_cundangbucunzai.Dialog.show()
                dianshu={'d1':0,'d2':0,'d3':0,'d4':0,'d5':0,'d6':0,'d7':0,'d8':0}
                nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,jiangli,jiangliget = [],[],[],[],[],[],[],[]
                rizhi,rizhifinish,yuanwang = [[0,0]],[],[[[0]],[[0]]]
                try:
                  os.mkdir('D:/MyRPG')
                except:
                    pass
                path = open('D:/MyRPG/data.dat','wb')
                pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
                path.close()
                del path


        #### 今日习惯的重载显示，由于比较麻烦，因此单独设定函数
        def jinrixiguanxianshi():
            ## 直接装载存档内容
                import time
                time.sleep(0.1)
                global xiguangeverday
                self.listWidget_3.clear()
                time = str(xiguangeverday[0][0])+'-'+str(xiguangeverday[0][1])+'-'+str(xiguangeverday[0][2])
                item = QtWidgets.QListWidgetItem()
                self.listWidget_3.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_3)
                item1.setText(time)
                font2 = QtGui.QFont()
                font2.setBold(True)
                item1.setFont(font2)
                self.listWidget_3.setItemWidget(item,item1)
                global  count4
                count4 = 1
                #装载今日习惯到其中
                # print(xiguangeverday)
                for i in xiguangeverday[0]:
                    if type(i) == int:
                        continue
                    if i ==[]:
                        continue
                    item = QtWidgets.QListWidgetItem()
                    value = '('+str(count4)+') '+i[0]+'(你将获得'+str(i[8])+'的经验和'+str(i[9])+'点娱乐点)'
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    font = QtGui.QFont()
                    font.setPointSize(int(length/51+1)*11)
                    item.setFont(font)
                    self.listWidget_3.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget_3)
                    if i[8]>0:
                        item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#0e9000;\">"+value+"</span>")
                    else:
                        item1.setText("<span style=\" font-size:10pt;font-weight:bold;color:#a20000;\">"+value+"</span>")
                    item1.setToolTip(i[1])
                    item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                    item1.setWordWrap(True)
                    self.listWidget_3.setItemWidget(item,item1)
                    count4 += 1
                item = QtWidgets.QListWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(30)
                item.setFont(font)
                self.listWidget_3.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_3)
                item1.setText(xiguangeverday[1])
                item1.setWordWrap(True)
                item1.setFont(font2)
                self.listWidget_3.setItemWidget(item,item1)

        #### 目前任务的重载显示，由于比较麻烦，所以单独设定函数，第一种是按类型，第二种是按重要性
        def renwuxianshi():
            global renwu
            import datetime
            jinrirenwu = []
            mingrirenwu = []
            yiqianrenwu = []
            daynow = datetime.date.today().year*365+datetime.date.today().month*30+datetime.date.today().day
            for i in renwu:
                if i[0] == daynow:
                    jinrirenwu.append(i)
                elif i[0] > daynow:
                    mingrirenwu.append(i)
                elif i[0] < daynow:
                    yiqianrenwu.append(i)
            self.listWidget_5.clear()
            time = str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)
            ji = datetime.date.today().weekday()
            xingqi = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']

            ###装载表头，今天日期星期，12号粗体，如果没有任务显示（没有任务）
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(12)
            item.setFont(font)
            self.listWidget_5.addItem(item)
            a = str(time)+'  '+xingqi[ji]+'今日任务：（没有任务）'
            b = str(time)+'  '+xingqi[ji]+'  '+'今日任务：'
            item1 = QtWidgets.QLabel(self.listWidget_5)
            item1.setFont(font)
            if jinrirenwu == []:
                item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+a+"</span></p></body></html>")
            else :
                item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+b+"</span></p></body></html>")
            self.listWidget_5.setItemWidget(item,item1)


            ### 开始对每个进行分类
            jinrigongzuo,jinrishenghuo,jinrilicai,jinrisuoshi,jinritisheng,jinriqita = [],[],[],[],[],[]
            mingrigongzuo,mingrishenghuo,mingrilicai,mingrisuoshi,mingritisheng,mingriqita =  [],[],[],[],[],[]
            zuorigongzuo,zuorishenghuo,zuorilicai,zuorisuoshi,zuoritisheng,zuoriqita = [],[],[],[],[],[]
            def fenlei():
             for i in jinrirenwu:
                if i[3] == 1:
                    jinrigongzuo.append(i)
                elif i[3] == 2:
                    jinrishenghuo.append(i)
                elif i[3] == 3:
                    jinrilicai.append(i)
                elif i[3] == 4:
                    jinrisuoshi.append(i)
                elif i[3] == 5:
                    jinritisheng.append(i)
                elif i[3] == 6:
                    jinriqita.append(i)
             for i in mingrirenwu:
                if i[3] == 1:
                    mingrigongzuo.append(i)
                elif i[3] == 2:
                    mingrishenghuo.append(i)
                elif i[3] == 3:
                    mingrilicai.append(i)
                elif i[3] == 4:
                    mingrisuoshi.append(i)
                elif i[3] == 5:
                    mingritisheng.append(i)
                elif i[3] == 6:
                    mingriqita.append(i)
             for i in yiqianrenwu:
                if i[3] == 1:
                    zuorigongzuo.append(i)
                elif i[3] == 2:
                    zuorishenghuo.append(i)
                elif i[3] == 3:
                    zuorilicai.append(i)
                elif i[3] == 4:
                    zuorisuoshi.append(i)
                elif i[3] == 5:
                    zuoritisheng.append(i)
                elif i[3] == 6:
                    zuoriqita.append(i)
            fenlei()

            ### 开始装载每个部分
            def kaishizhuangzai():
                global count5
                count5 = 1
                ## 前六个是类别装载，第七个是类别中项目装载
                def shengchenggongzuo():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('工作：')
                    self.listWidget_5.addItem(item)
                def shengchengshenghuo():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('生活：')
                    self.listWidget_5.addItem(item)
                def shengchenglicai():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('理财：')
                    self.listWidget_5.addItem(item)
                def shengchengsuoshi():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('琐事：')
                    self.listWidget_5.addItem(item)
                def shengchengtisheng():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('自我提升：')
                    self.listWidget_5.addItem(item)
                def shengchengqita():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('其他：')
                    self.listWidget_5.addItem(item)
                def zixiangmuzhuangzai(i):
                        global count5
                        item = QtWidgets.QListWidgetItem()
                        value = ' ('+str(count5)+') '+i[2]+'：'+i[5]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        font = QtGui.QFont()
                        font.setPointSize(int(length/69+1)*11)
                        item.setFont(font)
                        item.setWhatsThis(i[15])
                        self.listWidget_5.addItem(item)
                        item1 = QtWidgets.QLabel(self.listWidget_5)
                        item1.setText(value)
                        item1.setToolTip(i[1])
                        item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
                        item1.setWordWrap(True)
                        self.listWidget_5.setItemWidget(item,item1)
                        app.processEvents()
                        count5 += 1

                ##装载每个小项目后面的子项目
                def zhuangzaixiaoxiangmu(jinrigongzuo,jinrishenghuo,jinrilicai,jinrisuoshi,jinritisheng,jinriqita):
                    if jinrigongzuo == []:
                        pass
                    else:
                        shengchenggongzuo()
                        for i in jinrigongzuo:
                            zixiangmuzhuangzai(i)
                    if jinrishenghuo == []:
                        pass
                    else:
                        shengchengshenghuo()
                        for i in jinrishenghuo:
                            zixiangmuzhuangzai(i)
                    if jinrilicai == []:
                        pass
                    else:
                        shengchenglicai()
                        for i in jinrilicai:
                            zixiangmuzhuangzai(i)
                    if jinrisuoshi == []:
                        pass
                    else:
                        shengchengsuoshi()
                        for i in jinrisuoshi:
                            zixiangmuzhuangzai(i)
                    if jinritisheng == []:
                        pass
                    else:
                        shengchengtisheng()
                        for i in jinritisheng:
                            zixiangmuzhuangzai(i)
                    if jinriqita == []:
                        pass
                    else:
                        shengchengqita()
                        for i in jinriqita:
                            zixiangmuzhuangzai(i)

                ### 装载今日项目
                zhuangzaixiaoxiangmu(jinrigongzuo,jinrishenghuo,jinrilicai,jinrisuoshi,jinritisheng,jinriqita)

                ### 装载明日项目
                if mingrirenwu == []:
                    pass
                else:
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(12)
                    item.setFont(font)
                    self.listWidget_5.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget_5)
                    item1 .setFont(font)
                    item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+'明天及以后的任务：'+"</span></p></body></html>")
                    self.listWidget_5.setItemWidget(item,item1)
                    zhuangzaixiaoxiangmu(mingrigongzuo,mingrishenghuo,mingrilicai,mingrisuoshi,mingritisheng,mingriqita)

                ### 装载以往项目
                if yiqianrenwu == []:
                    pass
                else:
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(12)
                    item.setFont(font)
                    self.listWidget_5.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget_5)
                    item1 .setFont(font)
                    item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+'以前没有完成的任务（经验和娱乐点奖励减半）：'+"</span></p></body></html>")
                    self.listWidget_5.setItemWidget(item,item1)
                    zhuangzaixiaoxiangmu(zuorigongzuo,zuorishenghuo,zuorilicai,zuorisuoshi,zuoritisheng,zuoriqita)
            kaishizhuangzai()
        def renwuxianshi2():
            global renwu
            import datetime
            jinrirenwu = []
            mingrirenwu = []
            yiqianrenwu = []
            daynow = datetime.date.today().year*365+datetime.date.today().month*30+datetime.date.today().day
            for i in renwu:
                if i[0] == daynow:
                    jinrirenwu.append(i)
                elif i[0] > daynow:
                    mingrirenwu.append(i)
                elif i[0] < daynow:
                    yiqianrenwu.append(i)
            self.listWidget_5.clear()
            time = str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)
            ji = datetime.date.today().weekday()
            xingqi = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']

            ###装载表头，今天日期星期，12号粗体，如果没有任务显示（没有任务）
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(12)
            item.setFont(font)
            self.listWidget_5.addItem(item)
            a = str(time)+'  '+xingqi[ji]+'今日任务：（没有任务）'
            b = str(time)+'  '+xingqi[ji]+'  '+'今日任务：'
            item1 = QtWidgets.QLabel(self.listWidget_5)
            item1.setFont(font)
            if jinrirenwu == []:
                item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+a+"</span></p></body></html>")
            else :
                item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+b+"</span></p></body></html>")
            self.listWidget_5.setItemWidget(item,item1)


            ### 开始对每个进行分类，按重要性，1,2,3,4代表四种重要性
            jinri1,jinri2,jinri3,jinri4 = [],[],[],[]
            mingri1,mingri2,mingri3,mingri4=  [],[],[],[]
            zuori1,zuori2,zuori3,zuori4 = [],[],[],[]
            def fenlei():
             for i in jinrirenwu:
                if i[4] == 1:
                    jinri1.append(i)
                elif i[4] == 2:
                    jinri2.append(i)
                elif i[4] == 3:
                    jinri3.append(i)
                elif i[4] == 4:
                    jinri4.append(i)

             for i in mingrirenwu:
                if i[4] == 1:
                    mingri1.append(i)
                elif i[4] == 2:
                    mingri2.append(i)
                elif i[4] == 3:
                    mingri3.append(i)
                elif i[4] == 4:
                    mingri4.append(i)

             for i in yiqianrenwu:
                if i[4] == 1:
                    zuori1.append(i)
                elif i[4] == 2:
                    zuori2.append(i)
                elif i[4] == 3:
                    zuori3.append(i)
                elif i[4] == 4:
                    zuori4.append(i)
            fenlei()

            ### 开始装载每个部分
            def kaishizhuangzai():
                global count5
                count5 = 1
                ## 前六个是类别装载，第七个是类别中项目装载
                def shengchengzy1():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('重要且紧急：')
                    self.listWidget_5.addItem(item)
                def shengchengzy2():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('重要但不紧急：')
                    self.listWidget_5.addItem(item)
                def shengchengzy3():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('紧急但不重要：')
                    self.listWidget_5.addItem(item)
                def shengchengzy4():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('不重要不紧急：')
                    self.listWidget_5.addItem(item)
                # 子项目装载
                def zixiangmuzhuangzai(i):
                        global count5
                        item = QtWidgets.QListWidgetItem()
                        value = ' ('+str(count5)+') '+i[2]+'：'+i[5]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        font = QtGui.QFont()
                        font.setPointSize(int(length/69+1)*11)
                        item.setFont(font)
                        item.setWhatsThis(i[15])
                        self.listWidget_5.addItem(item)
                        item1 = QtWidgets.QLabel(self.listWidget_5)
                        item1.setText(value)
                        item1.setToolTip(i[1])
                        item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
                        item1.setWordWrap(True)
                        self.listWidget_5.setItemWidget(item,item1)
                        app.processEvents()
                        count5 += 1

                ##装载每个小项目后面的子项目
                def zhuangzaixiaoxiangmu(zy1,zy2,zy3,zy4):
                    if zy1 == []:
                        pass
                    else:
                        shengchengzy1()
                        for i in zy1:
                            zixiangmuzhuangzai(i)
                    if zy2 == []:
                        pass
                    else:
                        shengchengzy2()
                        for i in zy2:
                            zixiangmuzhuangzai(i)
                    if zy3 == []:
                        pass
                    else:
                        shengchengzy3()
                        for i in zy3:
                            zixiangmuzhuangzai(i)
                    if zy4 == []:
                        pass
                    else:
                        shengchengzy4()
                        for i in zy4:
                            zixiangmuzhuangzai(i)

                ### 装载今日项目
                zhuangzaixiaoxiangmu(jinri1,jinri2,jinri3,jinri4)

                ### 装载明日项目
                if mingrirenwu == []:
                    pass
                else:
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(12)
                    item.setFont(font)
                    self.listWidget_5.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget_5)
                    item1 .setFont(font)
                    item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+'明天及以后的任务：'+"</span></p></body></html>")
                    self.listWidget_5.setItemWidget(item,item1)
                    zhuangzaixiaoxiangmu(mingri1,mingri2,mingri3,mingri4)

                ### 装载以往项目
                if yiqianrenwu == []:
                    pass
                else:
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(12)
                    item.setFont(font)
                    self.listWidget_5.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget_5)
                    item1 .setFont(font)
                    item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+'以前没有完成的任务（经验和娱乐点奖励减半）：'+"</span></p></body></html>")
                    self.listWidget_5.setItemWidget(item,item1)
                    zhuangzaixiaoxiangmu(zuori1,zuori2,zuori3,zuori4)
            kaishizhuangzai()

        #### 基于习惯未完成或超天没有设置习惯的扣分并显示经验值同时调用重载显示
        def jinrixiguankoufenxianshi():
            ##首先计算扣分
            import datetime
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            daynow = datetime.date.today().year*365+datetime.date.today().month*30+datetime.date.today().day
            dayinfile = xiguangeverday[0][0]*365+xiguangeverday[0][1]*30+xiguangeverday[0][2]
            time = str(xiguangeverday[0][0])+'-'+str(xiguangeverday[0][1])+'-'+str(xiguangeverday[0][2])
            daycha = daynow-dayinfile-1
            xiguancha = len(xiguangeverday[0])-3
            if daycha == 0:
                xiguangeverday[1] = '你因上次还有'+str(xiguancha)+'个任务没有完成，因此总共扣'+str(8*xiguancha)+'点经验和'+str(2*xiguancha)+'点娱乐点。'
            else:
                xiguangeverday[1] = '上次存档时间是'+time+'，你因有'+str(daycha)+'天没有安排每日习惯，总共扣'+str(20*daycha)+'点经验和'+str(8*daycha)+'点娱乐点。'+'你因上次还有'+str(xiguancha)+'个任务没有完成，总共扣'+str(8*xiguancha)+'点经验和'+str(2*xiguancha)+'点娱乐点。'
            del xiguangeverday[0]
            xiguangeverday.insert(0,[datetime.date.today().year,datetime.date.today().month,datetime.date.today().day])
            dianshu['d7'] = dianshu['d7'] - 20*daycha - 8*xiguancha
            if dianshu['d7']<0:
                dianshu['d7'] = 0
            dianshu['d8'] = dianshu['d8'] - 8*daycha - 2*xiguancha
            ## 然后改变经验值和娱乐点

            #经验等级显示
            if int(dianshu['d7']/180) < 1:
                dengji = 0
            else:
             for i in range(int(dianshu['d7']/200+5)):
                if  int(dianshu['d7']/180) == 1:
                    dengji = 1
                    break
                if 10*(i**2)+170*i > dianshu['d7']:
                    dengji = i-1
                    break
            xiayijijingyan = 20*(dengji-1)+180+20
            duoyujingyan = dianshu['d7'] - (10*(dengji**2)+170*dengji)
            xianshidengji = '等级：'+"<span style=\" font-size:10pt;color:#930000;\">"+'LV.'+str(dengji)+"</span>"+' 下一级：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(duoyujingyan)+'/'+str(xiayijijingyan)+"</span>"
            fontjingyan = QtGui.QFont()
            fontjingyan.setBold(True)
            self.label_13.setFont(fontjingyan)
            self.label_14.setFont(fontjingyan)
            self.label_13.setText(xianshidengji)
            ############
            self.label_14.setText('娱乐点：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(dianshu['d8'])+"</span>")
            ## 最后保存变量并调用显示
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            jinrixiguanxianshi()



            pass
            ## 扣分并重新装载经验娱乐点和存档内容

        #### 重写所有基本点
        def chongxiejinbendian():
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path
            self.label_3.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'体质：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d1'])+"</span>")
            self.label_4.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'体重（千克）：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d2'])+"</span>")
            self.label_5.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'耐力：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d3'])+"</span>")
            self.label_2.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'专注：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d4'])+"</span>")
            self.label.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'智力：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d5'])+"</span>")
            self.label_12.setText("<span style=\" font-size:10pt;font-weight:bold;\">"'知识量：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d6'])+"</span>")
            # 经验系统需要更详细的设计
            if int(dianshu['d7']/180) < 1:
                dengji = 0
            else:
             for i in range(int(dianshu['d7']/200+5)):
                if  int(dianshu['d7']/180) == 1:
                    dengji = 1
                    break
                if 10*(i**2)+170*i > dianshu['d7']:
                    dengji = i-1
                    break
            xiayijijingyan = 20*(dengji-1)+180+20
            duoyujingyan = dianshu['d7'] - (10*(dengji**2)+170*dengji)
            xianshidengji = '等级：'+"<span style=\" font-size:10pt;color:#930000;\">"+'LV.'+str(dengji)+"</span>"+' 下一级：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(duoyujingyan)+'/'+str(xiayijijingyan)+"</span>"
            fontjingyan = QtGui.QFont()
            fontjingyan.setBold(True)
            self.label_13.setFont(fontjingyan)
            self.label_14.setFont(fontjingyan)
            self.label_13.setText(xianshidengji)
            ############
            self.label_14.setText('娱乐点：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(dianshu['d8'])+"</span>")

        #### 增量显示完成任务
        def zhengliangxianshiwanchengrenwu():
            global zengliangwanchengrenwu
            for i in zengliangwanchengrenwu:
                leixing = ['工作','生活','理财','琐事','自我提升','其他']
                zhongyaoxing = ['重要且紧急','重要但不紧急','紧急但不重要','不重要不紧急']
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '(新完成) '+leixing[i[2]-1]+'：'+i[4]+'（计划时间：'+i[1]+'）'
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/40+1)*10)
                item.setFont(font)
                #######################################
                self.listWidget_6.insertItem(0,item)
                item1 = QtWidgets.QLabel(self.listWidget_6)
                item1.setText("<html><head/><body><p><span style=\" font-size:9pt; color:#6F6F6F;\">"+value+"</span></p></body></html>")
                item1.setToolTip(zhongyaoxing[i[3]-1]+'，'+i[6]+'\n'+'描述：'+i[5])
                # print(i)
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_6.setItemWidget(item,item1)

        #### 任务日志的装载，因为涉及到新建日志后重新调用，所以单独建立函数
        def rizhixianshi():
            global rizhi
            self.treeWidget.clear()
            self.treeWidget.setIndentation(10)
            for i in rizhi:
                if i == rizhi[0]:
                    continue
                else:
                    if i[1] == int(i[1]):
                        ##添加一个主任务显示对象，并添加背景，装载Qlabel对象
                        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                        brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        brush2 = QtGui.QBrush(QtGui.QColor(180, 250, 251))
                        brush2.setStyle(QtCore.Qt.SolidPattern)
                        value = str(i[1])+'.'+i[0]+'：'+i[2]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        neirong = QtWidgets.QLabel(self.treeWidget)
                        neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                        neirong.setFixedHeight((int(length/60)+1)*21)
                        neirong.setWordWrap(True)
                        font = QtGui.QFont()
                        font.setBold(True)
                        font.setPointSize(10)
                        neirong.setFont(font)
                        if i[0] =='主线任务':
                            item_0.setBackground(0, brush)
                            neirong.setText("<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">"+value+"</span></p></body></html>")
                        else:
                            item_0.setBackground(0, brush2)
                            neirong.setText(value)
                        neirong.setToolTip('添加时间：'+i[6]+'；'+'奖励经验：'+str(i[4])+'，娱乐点：'+str(i[5])+'\n'+'备注：'+i[3])
                        self.treeWidget.setItemWidget(item_0,0,neirong)
                        app.processEvents()
                        continue
                    if round(i[1]*1000,3) == round(i[1]*1000,0):
                        item_1 = QtWidgets.QTreeWidgetItem(item_0)
                        # print(str(int(round(i[1]*10000000,0)))[-4:-3])
                        xuhao = str(int(str(int(round(i[1]*10000000,0)))[:-7]))+'.'+str(int(str(int(round(i[1]*10000000,0)))[-7:-4]))
                        value = xuhao +'.'+i[0]+'：'+i[2]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        neirong = QtWidgets.QLabel(self.treeWidget)
                        neirong.setFixedHeight((int(length/62)+1)*21)
                        neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                        neirong.setWordWrap(True)
                        neirong.setText(value)
                        neirong.setToolTip('添加时间：'+i[6]+'；'+'备注：'+i[3])
                        self.treeWidget.setItemWidget(item_1,0,neirong)
                        app.processEvents()
                        continue
                    if round(i[1]*100000,5) == round(i[1]*100000,0):
                        item_2 = QtWidgets.QTreeWidgetItem(item_1)
                        xuhao = str(int(str(int(round(i[1]*10000000,0)))[:-7]))+'.'+str(int(str(int(round(i[1]*10000000,0)))[-7:-4]))+'.'+str(int(str(int(round(i[1]*10000000,0)))[-4:-2]))
                        value = xuhao+'.'+i[0]+'：'+i[2]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        neirong = QtWidgets.QLabel(self.treeWidget)
                        neirong.setFixedHeight((int(length/60)+1)*21)
                        neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                        neirong.setWordWrap(True)
                        neirong.setText(value)
                        neirong.setToolTip('添加时间：'+i[6]+'；'+'备注：'+i[3])
                        self.treeWidget.setItemWidget(item_2,0,neirong)
                        app.processEvents()
                        continue
                    if round(i[1]*10000000,7) == round(i[1]*10000000,0):
                        item_3 = QtWidgets.QTreeWidgetItem(item_2)
                        xuhao = str(int(str(int(round(i[1]*10000000,0)))[:-7]))+'.'+str(int(str(int(round(i[1]*10000000,0)))[-7:-4]))+'.'+str(int(str(int(round(i[1]*10000000,0)))[-4:-2]))+'.'+str(int(str(int(round(i[1]*10000000,0)))[-2:]))
                        value = xuhao+'.'+i[0]+'：'+i[2]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        neirong = QtWidgets.QLabel(self.treeWidget)
                        neirong.setFixedHeight((int(length/59)+1)*21)
                        neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                        neirong.setWordWrap(True)
                        neirong.setText(value)
                        neirong.setToolTip('添加时间：'+i[6]+'；'+'备注：'+i[3])
                        self.treeWidget.setItemWidget(item_3,0,neirong)
                        app.processEvents()
                        continue

        #### 增量显示完成日志
        def wanchengrizhizengliangxianshi():
            global zengliangwanchengrizhi,countrizhizhuxian,countrizhizhixian
            global  rizhifinish,rizhi
            for i in zengliangwanchengrizhi:
                        item_0 = QtWidgets.QListWidgetItem()
                        brush = QtGui.QBrush(QtGui.QColor(234, 255, 227))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        brush2 = QtGui.QBrush(QtGui.QColor(227, 243, 255))
                        brush2.setStyle(QtCore.Qt.SolidPattern)
                        value = str(i[1])+'.'+i[0]+'：'+i[2]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        font = QtGui.QFont()
                        font.setPointSize((int(length/42)+1)*10)
                        neirong = QtWidgets.QLabel(self.treeWidget)
                        neirong.setWordWrap(True)
                        item_0.setFont(font)
                        self.listrizhiwancheng.insertItem(0,item_0)
                        if i[0] =='主线任务':
                            item_0.setBackground(brush)
                            neirong.setText("<span style=\" font-size:9pt; color:#7b1714;\">"+value+"</span>")
                        else:
                            item_0.setBackground(brush2)
                            neirong.setText("<span style=\" font-size:9pt; color:#6F6F6F;\">"+value+"</span>")
                        item_0.setWhatsThis(str(i[1]))
                        item_0.setToolTip(i[7]+'；添加时间：'+i[6]+'；'+'奖励经验：'+str(i[4])+'，娱乐点：'+str(i[5])+'\n'+'备注：'+i[3])
                        self.listrizhiwancheng.setItemWidget(item_0,neirong)
                        if i[0] == '主线任务':
                            countrizhizhuxian += 1
                        if i[0] == '支线任务':
                            countrizhizhixian += 1
            self.label_15.setText('完成'+str(countrizhizhuxian)+'主线|'+str(countrizhizhixian)+'支线')

        #### 奖励重载显示
        def jianglixianshi():
            global jiangli
            global count7
            count7 = 1
            self.listWidget_7.clear()
            for i in jiangli:
                item = QtWidgets.QListWidgetItem()
                value = '('+str(count7)+') '+i[0]+'(将消耗'+str(i[2])+'点娱乐点)'
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/51+1)*11)
                item.setFont(font)
                self.listWidget_7.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_3)
                item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#2a368e;\">"+'('+str(count7)+') '+i[0]+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#ff0000;\">"+'(将消耗'+str(i[2])+'点娱乐点)'+"</span>")
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                item1.setToolTip(i[1])
                self.listWidget_7.setItemWidget(item,item1)
                count7 += 1

        #### 已获得奖励增量显示():
        def jianglizengliang():
            global zengliangjiangli
            for i in zengliangjiangli:
                item = QtWidgets.QListWidgetItem()
                value =  '(新获得奖励) '+i[0]+'：'+i[1]
                item.setText(value)
                font = QtGui.QFont()
                font.setBold(True)
                font.setPointSize(9)
                brush = QtGui.QBrush(QtGui.QColor(185, 127,127))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                item.setFont(font)
                self.listWidget_8.insertItem(0,item)

        ### 装载愿望，已完成愿望只装载200条，因为涉及到新建后重新调用，所以单独建立函数
        def zhuangzaiyuanwang():
            global  yuanwang
            self.treeWidget_3.clear()
            self.treeWidget_3.setIndentation(10)
            self.treeWidget_3.setWordWrap(True)
            for i in yuanwang[0]:
                if i == yuanwang[0][0]:
                    continue
                if i[0] == int(i[0]):
                    item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
                    brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    value = str(int(i[0]))+' ('+i[5]+')：'+i[3]
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    neirong = QtWidgets.QLabel(self.treeWidget)
                    neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                    neirong.setFixedHeight((int(length/99)+1)*21)
                    neirong.setWordWrap(True)
                    neirong.setToolTip('等级：'+str(i[2])+'<br/>'+i[4])
                    neirong.setText("<span style=\" font-size:10pt;font-weight:bold;; color:#1c9700;\">"+value+"</span>")
                    self.treeWidget_3.setItemWidget(item_0,0,neirong)
                    app.processEvents()
                else:
                    item_1 = QtWidgets.QTreeWidgetItem(item_0)
                    brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    value = str(i[0])+' ('+i[5]+')：'+i[3]+'('+str(i[1])+'%)'
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    neirong = QtWidgets.QLabel(self.treeWidget)
                    neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                    neirong.setFixedHeight((int(length/108)+1)*21)
                    neirong.setWordWrap(True)
                    neirong.setToolTip(i[4])
                    neirong.setText(value)
                    self.treeWidget_3.setItemWidget(item_1,0,neirong)
                    app.processEvents()
            y = 0
            for i in range(len(yuanwang[1])):
                if yuanwang[1][i] == yuanwang[1][0]:
                    continue
                if yuanwang[1][i][0] == int(yuanwang[1][i][0]):
                    y += 1
                if y > 100:
                    break
                if yuanwang[1][i][0] == int(yuanwang[1][i][0]):
                    item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
                    brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    value ='（已完成）'+str(int(yuanwang[1][i][0]))+' ('+yuanwang[1][i][5]+')：'+yuanwang[1][i][3]
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    neirong = QtWidgets.QLabel(self.treeWidget)
                    neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                    neirong.setFixedHeight((int(length/99)+1)*21)
                    neirong.setWordWrap(True)
                    neirong.setToolTip(yuanwang[1][i][4])
                    neirong.setText("<span style=\" font-size:10pt;font-weight:bold;; color:#8090b0;\">"+value+"</span>")
                    self.treeWidget_3.setItemWidget(item_0,0,neirong)
                    app.processEvents()
                else:
                    item_1 = QtWidgets.QTreeWidgetItem(item_0)
                    brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    value = str(yuanwang[1][i][0])+' ('+yuanwang[1][i][5]+')：'+yuanwang[1][i][3]+'('+str(yuanwang[1][i][1])+'%)'
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    neirong = QtWidgets.QLabel(self.treeWidget)
                    neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                    neirong.setFixedHeight((int(length/108)+1)*21)
                    neirong.setWordWrap(True)
                    neirong.setToolTip(yuanwang[1][i][4])
                    neirong.setText(value)
                    self.treeWidget_3.setItemWidget(item_1,0,neirong)
                    app.processEvents()

        #### 今日作息安排显示(此函数在下面一个函数后面运行)
        def zuoxixianshi():
            import datetime
            global dianshu
            nian22 = datetime.date.today().year
            yue22 = datetime.date.today().month
            ri22 = datetime.date.today().day
            jintianriqi = QtWidgets.QDateEdit()
            jintianriqi.setDate(QtCore.QDate(nian22,yue22,ri22))
            today = jintianriqi.text()
            xingqiji = datetime.date.today().weekday()

            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(14)

            self.textBrowser.setFont(font)
            color = QtGui.QColor(7,64,125)
            self.textBrowser.setTextColor(color)

            if today in dianshu.keys():
                self.textBrowser.setText(today+'\n'+dianshu[today])
            else:
                if xingqiji< 5 and  '平时' in dianshu.keys():
                    self.textBrowser.setText('平时'+'\n'+dianshu['平时'])
                    return
                if xingqiji == 5 and  '周六' in dianshu.keys():
                    self.textBrowser.setText('周六'+'\n'+dianshu['周六'])
                    return
                if  xingqiji == 6 and  '周日' in dianshu.keys():
                    self.textBrowser.setText('周日'+'\n'+dianshu['周日'])
                    return
                else:
                    self.textBrowser.setText('目前没有制定任何作息安排表')



        #### 装载所有变量到相应位置
        def zhuangzai():
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang

            ## 第一部分装载所有变量到面板当中
            #"<span style=\" font-size:10pt;color:#00DB00;\">"+value+"</span>"
            # 装载点数和经验部分
            self.label_3.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'体质：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d1'])+"</span>")
            self.label_4.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'体重（千克）：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d2'])+"</span>")
            self.label_5.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'耐力：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d3'])+"</span>")
            self.label_2.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'专注：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d4'])+"</span>")
            self.label.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'智力：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d5'])+"</span>")
            self.label_12.setText("<span style=\" font-size:10pt;font-weight:bold;\">"'知识量：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d6'])+"</span>")
            # 经验系统需要更详细的设计
            if int(dianshu['d7']/180) < 1:
                dengji = 0
            else:
             for i in range(int(dianshu['d7']/200+5)):
                if  int(dianshu['d7']/180) == 1:
                    dengji = 1
                    break
                if 10*(i**2)+170*i > dianshu['d7']:
                    dengji = i-1
                    break
            xiayijijingyan = 20*(dengji-1)+180+20
            duoyujingyan = dianshu['d7'] - (10*(dengji**2)+170*dengji)

            xianshidengji = '等级：'+"<span style=\" font-size:10pt;color:#930000;\">"+'LV.'+str(dengji)+"</span>"+' 下一级：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(duoyujingyan)+'/'+str(xiayijijingyan)+"</span>"
            fontjingyan = QtGui.QFont()
            fontjingyan.setBold(True)
            self.label_13.setFont(fontjingyan)
            self.label_14.setFont(fontjingyan)
            self.label_13.setText(xianshidengji)
            ############
            self.label_14.setText('娱乐点：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(dianshu['d8'])+"</span>")
            # 装载天赋和能力
            self.listWidget.clear()
            global count
            count = 1
            for i in nengli:
                item = QtWidgets.QListWidgetItem()
                # 取得天赋和能力显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count)+') '+i[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/43+1)*11)
                item.setFont(font)
                ####################################
                self.listWidget.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget)
                brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                if i[0][0:2] == '天赋':
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#0e9000;\">"+value+"</span>")
                else:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#123e80;\">"+value+"</span>")
                item1.setToolTip(i[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget.setItemWidget(item,item1)
                app.processEvents()
                count += 1

            # 装载装备
            self.listWidget_2.clear()
            global count2
            count2 = 1
            for i in zhuangbei:
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count2)+') '+i[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/43+1)*11)
                item.setFont(font)
                ####################################
                self.listWidget_2.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_2)
                brush = QtGui.QBrush(QtGui.QColor(180, 250, 251))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                item1.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+value+"</span>")
                item1.setToolTip(i[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_2.setItemWidget(item,item1)
                app.processEvents()
                count2 += 1

            # 装载所有习惯
            self.listWidget_4.clear()
            global count3
            count3 = 1
            for i in xiguanall:
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count3)+') '+i[0]+'(你将获得'+str(i[8])+'的经验和'+str(i[9])+'点娱乐点)'
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/51+1)*11)
                item.setFont(font)
                #######################################
                self.listWidget_4.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_4)
                if i[8]>0:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#0e9000;\">"+value+"</span>")
                else:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold;color:#a20000;\">"+value+"</span>")
                item1.setToolTip(i[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_4.setItemWidget(item,item1)
                count3 += 1

            # 装载今日习惯
            # 这个非常麻烦，因为每天都要完成一定的习惯，所以如果某天跳开需要判断是否有跳开的，有的话就要扣分， 如果上一次有没有完成的也需要扣分
            # 该体系的设计是基于[[年,月,日,[习惯1],[习惯2]..],信息这样的方式]，首先开档检查年月日是不是今天，如果是就直接其中内容进行显示，如果不是今天
            # 需要判断系统时间是否有错，如果当前时间小于年月日，那么基本上是时间回调了，给出警示，然后不做任何修改，如果当前时间大于年月日30天，将判断是否系统时间被设置成未来，给出弹窗
            # 选择没有设置，直接扣分，是的话，不做任何改变，建议修改时间后再打开
            # 这种设计的话，在添加的时候就不需要顾虑，直接添加即可，但是有一种打开程序的时候和添加可能跨天，需要在添加界面进行判断，如果为空，删除该条目，删除该条目，并修改信息直接添加
            # 如果不为空，警告用户，前一天有任务没有完成，让用户重启进行惩罚后后重新添加今日习惯。



            # 装载已经完成任务，只装载200条
            self.listWidget_6.clear()
            global count6
            count6 = 1
            for i in range(len(renwufinish)):
                if i > 199:
                    break
                leixing = ['工作','生活','理财','琐事','自我提升','其他']
                zhongyaoxing = ['重要且紧急','重要但不紧急','紧急但不重要','不重要不紧急']
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count6)+') '+leixing[renwufinish[i][2]-1]+'：'+renwufinish[i][4]+'（计划时间：'+renwufinish[i][1]+'）'
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/40+1)*10)
                item.setFont(font)
                #######################################
                self.listWidget_6.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_6)
                item1.setText("<html><head/><body><p><span style=\" font-size:9pt; color:#6F6F6F;\">"+value+"</span></p></body></html>")
                item1.setToolTip(zhongyaoxing[renwufinish[i][3]-1]+'，'+renwufinish[i][6]+'\n'+'描述：'+renwufinish[i][5])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_6.setItemWidget(item,item1)
                count6 += 1

            # 装载已经完成的日志,只装载200项
            global countrizhizhuxian,countrizhizhixian
            self.listrizhiwancheng.clear()
            for i in range(len(rizhifinish)):
                        if i > 199:
                            break
                        item_0 = QtWidgets.QListWidgetItem()
                        brush = QtGui.QBrush(QtGui.QColor(234, 255, 227))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        brush2 = QtGui.QBrush(QtGui.QColor(227, 243, 255))
                        brush2.setStyle(QtCore.Qt.SolidPattern)
                        value = str(rizhifinish[i][1])+'.'+rizhifinish[i][0]+'：'+rizhifinish[i][2]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        font = QtGui.QFont()
                        font.setPointSize((int(length/42)+1)*10)
                        neirong = QtWidgets.QLabel(self.treeWidget)
                        neirong.setWordWrap(True)
                        item_0.setFont(font)
                        self.listrizhiwancheng.addItem(item_0)
                        if rizhifinish[i][0] =='主线任务':
                            item_0.setBackground(brush)
                            neirong.setText("<span style=\" font-size:9pt; color:#7b1714;\">"+value+"</span>")
                        else:
                            item_0.setBackground(brush2)
                            neirong.setText("<span style=\" font-size:9pt; color:#6F6F6F;\">"+value+"</span>")
                        item_0.setWhatsThis(str(rizhifinish[i][1]))
                        item_0.setToolTip(rizhifinish[i][7]+'；添加时间：'+rizhifinish[i][6]+'；'+'已获得奖励经验：'+str(rizhifinish[i][4])+'，娱乐点：'+str(rizhifinish[i][5])+'\n'+'备注：'+rizhifinish[i][3])
                        self.listrizhiwancheng.setItemWidget(item_0,neirong)
                        app.processEvents()
            for i in  rizhifinish:
                if i[0] == '主线任务':
                            countrizhizhuxian +=1
                if i[0] == '支线任务':
                            countrizhizhixian +=1
            self.label_15.setText('完成'+str(countrizhizhuxian)+'主线|'+str(countrizhizhixian)+'支线')

            #装载已获得的奖励
            self.listWidget_8.clear()
            self.listWidget_8.setWordWrap(True)
            global count8
            count8 = 1
            for i in range(len(jiangliget)):
                if i > 199:
                    break
                item = QtWidgets.QListWidgetItem()
                value =  '('+str(count8)+') '+jiangliget[i][0]+'：'+jiangliget[i][1]
                item.setText(value)
                font = QtGui.QFont()
                font.setBold(True)
                font.setPointSize(9)
                brush = QtGui.QBrush(QtGui.QColor(185, 127,127))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                item.setFont(font)
                self.listWidget_8.addItem(item)
                count8 += 1

        ###今日习惯的扣分系统会造成存档问题，因此这里单独设置显示，新打开程序时，只有切换到习惯才会显示
        def xiguanjinggaochuangkou(x):
          global xiguangeverday
          if x == 2 :
            import datetime
            if xiguangeverday == []:
                jinrixiguandanduxianshi()
                return
            if xiguangeverday[0][0] == datetime.date.today().year and xiguangeverday[0][1] == datetime.date.today().month and xiguangeverday[0][2] == datetime.date.today().day:
                jinrixiguanxianshi()
                return
            else:
                import cundangjinggao
                Dialog = QtWidgets.QDialog()
                ui = cundangjinggao.Ui_Dialog()
                ui.setupUi(Dialog)
                Dialog.show()
                ui.pushButton.clicked.connect(jinrixiguandanduxianshi)
        def jinrixiguandanduxianshi():
            import datetime
            global count4,xiguangeverday
            count4 = 1
            #判断今日习惯是否为空若为空，就创建一个新档案
            if xiguangeverday == []:
                xiguangeverday = [[datetime.date.today().year,datetime.date.today().month,datetime.date.today().day],'这是你第一次使用设定每日习惯，请使用“设定每日习惯”按钮来添加每日完成习惯。']
                import pickle
                path = open('D:/MyRPG/data.dat','wb')
                pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
                path.close()
                del path
            #判断其中内容是不是今天的，如果是就直接显示出来

            if xiguangeverday[0][0] == datetime.date.today().year and xiguangeverday[0][1] == datetime.date.today().month and xiguangeverday[0][2] == datetime.date.today().day:
                # print(True)
                jinrixiguanxianshi()

            else:
                daynow = datetime.date.today().year*365+datetime.date.today().month*30+datetime.date.today().day
                dayinfile = xiguangeverday[0][0]*365+xiguangeverday[0][1]*30+xiguangeverday[0][2]
                daycha = daynow-dayinfile
                # print(False)
                if daycha == 1:
                    if len(xiguangeverday[0]) == 3:
                        xiguangeverday[1] = '很好，你完成了昨天所有的每日习惯，并且没有出现超天的情况。'
                        del xiguangeverday[0]
                        xiguangeverday.insert(0,[datetime.date.today().year,datetime.date.today().month,datetime.date.today().day])
                        #此处应该写入文件并直接原地重载，因为不扣分
                        import pickle
                        path = open('D:/MyRPG/data.dat','wb')
                        pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
                        path.close()
                        del path
                        jinrixiguanxianshi()
                    else:
                        jinrixiguankoufenxianshi()

                elif daycha < 0:
                    xiguangeverday[1] = '当前日期小于最后一次存档，可能是本机时间回调或上次存档错误，请检查或恢复存档，最好不要新增操作，如果需要，请慎重重置。'
                    jinrixiguanxianshi()

                elif daycha > 30:
                    xiguangeverday[1] = '存档太旧或本机时间错误，请检查本机时间或恢复存档，最好不要新增操作，如果需要，请慎重重置。'
                    import shijianjinggao
                    Dialog = QtWidgets.QDialog()
                    ui = shijianjinggao.Ui_Dialog()
                    ui.setupUi(Dialog)
                    Dialog.show()
                    jinrixiguanxianshi()
                    ui.pushButton_2.clicked.connect(jinrixiguankoufenxianshi)
                else:
                    jinrixiguankoufenxianshi()

        global xiguanbool
        self.tabWidget.currentChanged.connect(xiguanjinggaochuangkou)


        #### 每次数据改变需要完全重载时和同步时候调用，重新载入所有数据并装载到界面上
        def freshandload():
            import time
            time.sleep(0.1)
            chushihua()
            zhuangzai()

        #### 每次数据改变需要增量载入时调用，该方法在开始写第三页的时候发生改变，后面的内容可能不再会使用它。因为增量显示直接调研变量重载和自身重载就行了，这个方法需要全部都判断一下
        #### 时间上可能差不多，因为要判断增量变量是否为空，但是还是稍显麻烦，新的方法不需要增加一个全局增量变量
        def zengliangload():
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            global zengliangnengli
            import time
            time.sleep(0.1)
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path

            ## 增量装载点数和经验部分
            self.label_3.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'体质：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d1'])+"</span>")
            self.label_4.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'体重（千克）：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d2'])+"</span>")
            self.label_5.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'耐力：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d3'])+"</span>")
            self.label_2.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'专注：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d4'])+"</span>")
            self.label.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+'智力：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d5'])+"</span>")
            self.label_12.setText("<span style=\" font-size:10pt;font-weight:bold;\">"'知识量：'+"</span>"+"<span style=\" font-size:10pt;font-weight:bold; color:#000079;\">"+str(dianshu['d6'])+"</span>")
            # 经验系统需要更详细的设计
            if int(dianshu['d7']/180) < 1:
                dengji = 0
            else:
             for i in range(int(dianshu['d7']/200+5)):
                if  int(dianshu['d7']/180) == 1:
                    dengji = 1
                    break
                if 10*(i**2)+170*i > dianshu['d7']:
                    dengji = i-1
                    break
            xiayijijingyan = 20*(dengji-1)+180+20
            duoyujingyan = dianshu['d7'] - (10*(dengji**2)+170*dengji)
            xianshidengji = '等级：'+"<span style=\" font-size:10pt;color:#930000;\">"+'LV.'+str(dengji)+"</span>"+' 下一级：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(duoyujingyan)+'/'+str(xiayijijingyan)+"</span>"
            fontjingyan = QtGui.QFont()
            fontjingyan.setBold(True)
            self.label_13.setFont(fontjingyan)
            self.label_14.setFont(fontjingyan)
            self.label_13.setText(xianshidengji)
            ############
            self.label_14.setText('娱乐点：'+"<span style=\" font-size:10pt;color:#009100;\">"+str(dianshu['d8'])+"</span>")

            ## 增量装载能力部分
            import dialog4_shedingtianfunengli
            global count,zengliangnengli
            try:
                zengliangnengli = dialog4_shedingtianfunengli.add
            except:
                pass
            if zengliangnengli == []:
                pass
            else:
                item = QtWidgets.QListWidgetItem()
                # 取得天赋和能力显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count)+') '+zengliangnengli[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/43+1)*11)
                item.setFont(font)
                ##################################
                self.listWidget.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget)
                brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                if zengliangnengli[0][0:2] == '天赋':
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#0e9000;\">"+value+"</span>")
                else:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#123e80;\">"+value+"</span>")
                item1.setToolTip(zengliangnengli[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget.setItemWidget(item,item1)
                count += 1
                zengliangnengli = []
                dialog4_shedingtianfunengli.add = []

            ## 增量装载装备部分
            import dialog5_zhuangbei
            global count2,zengliangzhuangbei
            try:
                zengliangzhuangbei = dialog5_zhuangbei.add
            except:
                pass
            if zengliangzhuangbei == []:
                pass
            else:
                item = QtWidgets.QListWidgetItem()
                value = '('+str(count2)+') '+zengliangzhuangbei[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/43+1)*11)
                item.setFont(font)
                self.listWidget_2.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_2)
                brush = QtGui.QBrush(QtGui.QColor(180, 250, 251))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                item1.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+value+"</span>")
                item1.setToolTip(zengliangzhuangbei[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_2.setItemWidget(item,item1)
                count2 += 1
                zengliangzhuangbei = []
                dialog5_zhuangbei.add = []
                # print(zhuangbei)

            ## 增量装载习惯部分
            import dialog6_tianjiaxiguan
            global count3,zengliangxiguanall
            try:
                zengliangxiguanall = dialog6_tianjiaxiguan.add
            except:
                pass
            if zengliangxiguanall == []:
                pass
            else:

                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count3)+') '+zengliangxiguanall[0]+'(你将获得'+str(zengliangxiguanall[8])+'的经验和'+str(zengliangxiguanall[9])+'点娱乐点)'
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/51+1)*11)
                item.setFont(font)
                #######################################
                self.listWidget_4.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_4)
                if zengliangxiguanall[8]>0:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#0e9000;\">"+value+"</span>")
                else:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold;color:#a20000;\">"+value+"</span>")
                item1.setToolTip(zengliangxiguanall[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_4.setItemWidget(item,item1)
                count3 += 1
                zengliangxiguanall = []
                dialog6_tianjiaxiguan.add = []

        #### 打开同步模块
        def renwudandu():
            if self.radioButton_2.isChecked():
                renwuxianshi()
            if self.radioButton.isChecked():
                renwuxianshi2()
        def dakaitongbu():
            import dialog2_tongbu
            Dialog = QtWidgets.QDialog()
            ui = dialog2_tongbu.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            Dialog.finished.connect(freshandload)
            Dialog.finished.connect(rizhixianshi)
            Dialog.finished.connect(jianglixianshi)
            Dialog.finished.connect(zhuangzaiyuanwang)
            Dialog.finished.connect(renwudandu)
            Dialog.finished.connect(rilibianse)
            Dialog.finished.connect(zuoxixianshi)

        #### 打开设定点数模块
        def shedingdianshu():
            import dialog3_shedingjibendian
            Dialog = QtWidgets.QDialog()
            ui = dialog3_shedingjibendian.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton_2.clicked.connect(zengliangload)

        #### 打开设定能力模块
        def shedingnengli():
            import dialog4_shedingtianfunengli
            Dialog = QtWidgets.QDialog()
            ui = dialog4_shedingtianfunengli.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(zengliangload)

        ####打开装备模块
        def shedingzhuangbei():
            import dialog5_zhuangbei
            Dialog = QtWidgets.QDialog()
            ui = dialog5_zhuangbei.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(zengliangload)

        ####打开添加习惯模块
        def tianjiaxiguan():
            import dialog6_tianjiaxiguan
            Dialog = QtWidgets.QDialog()
            ui = dialog6_tianjiaxiguan.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(zengliangload)

        ####习惯删除后重新装载，从dialog7中直接读取变量而不是重新读取存档，存档已经保存了。
        def shanxiguangengxin():
            global xiguanall
            import dialog7_shanchuxiguan
            xiguanall = dialog7_shanchuxiguan.xiguanall
            self.listWidget_4.clear()
            global count3
            count3 = 1
            for i in xiguanall:
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count3)+') '+i[0]+'(你将获得'+str(i[8])+'的经验和'+str(i[9])+'点娱乐点)'
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/51+1)*11)
                item.setFont(font)
                #######################################
                self.listWidget_4.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_4)
                if i[8]>0:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#0e9000;\">"+value+"</span>")
                else:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold;color:#a20000;\">"+value+"</span>")
                item1.setToolTip(i[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_4.setItemWidget(item,item1)
                count3 += 1

        ####打开删除习惯模块
        def shanchuxiguan():
            import dialog7_shanchuxiguan
            Dialog = QtWidgets.QDialog()
            ui = dialog7_shanchuxiguan.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(shanxiguangengxin)

        ####习惯增量更新
        def xiguanzenglianggengxin():
            global xiguangeverday
            import dialog8_shedingmeirixiguan
            xiguangeverday = dialog8_shedingmeirixiguan.xiguangeverday
            jinrixiguanxianshi()

        ####打开设定今日习惯模块
        def shedingjinrixiguan():
            import dialog8_shedingmeirixiguan
            Dialog = QtWidgets.QDialog()
            ui = dialog8_shedingmeirixiguan.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(xiguanzenglianggengxin)

        ####重写基本点，重新载入今日习惯，在完成习惯之后进行调用
        def chongxiejibendianhexiguan():
            chongxiejinbendian()
            jinrixiguanxianshi()

        ####设定打开完成习惯
        def wanchengxiguan():
            import dialog9_wanchengxiguan
            Dialog = QtWidgets.QDialog()
            ui = dialog9_wanchengxiguan.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(chongxiejibendianhexiguan)

        ####打开设定添加任务模块，以下两个函数一起工作
        def huoderenwugengxin():
            import dialog10_tianjiarenwu
            global renwu
            renwu = dialog10_tianjiarenwu.renwu
            if self.radioButton_2.isChecked():
                renwuxianshi()
            if self.radioButton.isChecked():
                renwuxianshi2()
            rilibianse()
        def tianjiarenwu():
            global renwu
            import dialog10_tianjiarenwu
            Dialog = QtWidgets.QDialog()
            ui = dialog10_tianjiarenwu.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(huoderenwugengxin)

        #### 点击任务弹出小窗
        def dianjirenwuxiangqing(item):
            global renwu
            import dialog10fujia_xianshirenwuxiangqing
            Form = dialog10fujia_xianshirenwuxiangqing.window()
            ui = dialog10fujia_xianshirenwuxiangqing.Ui_Form()
            ui.setupUi(Form)
            widget = ui.listWidget
            widget.clear()
            for i in renwu:
                if i[15] == item.whatsThis():
                    leixing = ['工作','生活','理财','琐事','自我提升','其他']
                    zhongyaoxing = ['重要且紧急','重要但不紧急','紧急但不重要','不重要不紧急']

                    item = QtWidgets.QListWidgetItem()
                    item1 = QtWidgets.QLabel(widget)
                    value = ''+i[5]
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    font = QtGui.QFont()
                    font.setPointSize(int(length/42+1)*11)
                    item.setFont(font)
                    font1 = QtGui.QFont()
                    font1.setBold(True)
                    widget.addItem(item)
                    item1.setText(value)
                    item1.setFont(font1)
                    item1.setWordWrap(True)
                    widget.setItemWidget(item,item1)

                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    # font.setBold(True)
                    item.setFont(font)
                    item.setText('时间：'+i[1]+'至'+i[2])
                    widget.addItem(item)

                    item = QtWidgets.QListWidgetItem()
                    item.setFont(font)
                    item.setText('类型：'+leixing[i[3]-1])
                    widget.addItem(item)

                    item = QtWidgets.QListWidgetItem()
                    item.setFont(font)
                    item.setText('重要性：'+zhongyaoxing[i[4]-1])
                    widget.addItem(item)

                    item = QtWidgets.QListWidgetItem()
                    item.setFont(font)

                    xiaoguo = ['丨体质','丨体重','丨耐力','丨专注','丨智力','丨知识量']
                    kk = 0
                    xianshixiaoguo = ''
                    for ii in [i[7],i[8],i[9],i[10],i[11],i[12]]:
                        if ii == 0:
                            kk += 1
                        else:
                            xianshixiaoguo = str(xianshixiaoguo) + xiaoguo[kk] + str(ii)
                            kk += 1
                    if xianshixiaoguo == '':
                        xianshixiaoguo=''
                    item.setText('奖励：经验'+str(i[13])+'丨娱乐点'+str(i[14])+xianshixiaoguo)
                    widget.addItem(item)


                    item = QtWidgets.QListWidgetItem()
                    item1 = QtWidgets.QLabel(widget)
                    value = '描述：'+i[6]
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    font = QtGui.QFont()
                    font.setPointSize(int(length/42+1)*11)
                    item.setFont(font)
                    font1 = QtGui.QFont()
                    # font1.setBold(True)
                    widget.addItem(item)
                    item1.setText(value)
                    item1.setFont(font1)
                    item1.setWordWrap(True)
                    widget.setItemWidget(item,item1)
                    Form.show()
                    break

        ### 点击任务上的日期，显示一个弹窗显示当天的任务
        def rilixianshi(date):
            import re
            global renwu
            xianshirenwu = []
            for i in renwu:
                a = re.split("\D",i[2])
                day = QtCore.QDate(int(a[0]),int(a[1]),int(a[2]))
                if day == date:
                    xianshirenwu.append(i)
            import dialog10fujia_rilixianshi
            Form = dialog10fujia_rilixianshi.window()
            ui = dialog10fujia_rilixianshi.Ui_Form()
            ui.setupUi(Form)
            widget = ui.listWidget
            widget.clear()
            count = 1
            leixing = ['工作','生活','理财','琐事','自我提升','其他']
            if xianshirenwu == []:
                pass
            else:
                # print(date.year(),date.month(),date.day(),date.dayOfWeek())
                item = QtWidgets.QListWidgetItem()
                time = str(date.year())+'-'+str(date.month())+'-'+str(date.day())
                ji = date.dayOfWeek()
                xingqi = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
                item.setText(time+' '+xingqi[ji-1]+' 共'+str(len(xianshirenwu ))+'项任务')
                widget.addItem(item)

            for k in xianshirenwu:
                item = QtWidgets.QListWidgetItem()
                item1 = QtWidgets.QLabel(widget)
                value = '('+str(count)+')'+leixing[k[3]-1]+'：'+k[5]+'(完成时间'+(k[2].split(' '))[1]+')'
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/42+1)*11)
                item.setFont(font)
                font1 = QtGui.QFont()
                # font1.setBold(True)
                widget.addItem(item)
                item1.setText(value)
                item1.setFont(font1)
                item1.setWordWrap(True)
                widget.setItemWidget(item,item1)
                count += 1
            if xianshirenwu == []:
                pass
            else:
               Form.show()

        ### 有任务的日期内将变色
        def rilibianse():
            import re
            global renwu,dayyourenwu2
            yangshe = QtGui.QTextCharFormat()
            for i in dayyourenwu2:
                self.calendarWidget.setDateTextFormat(i,yangshe)
            dayyourenwu = []
            for i in renwu:
                a = re.split("\D",i[2])
                day = QtCore.QDate(int(a[0]),int(a[1]),int(a[2]))
                dayyourenwu.append(day)
            dayyourenwu2 = list(set(dayyourenwu))
            yangshe = QtGui.QTextCharFormat()
            c = QtGui.QFont()
            c .setBold(True)
            c.setPointSize(16)
            d = QtGui.QBrush(QtCore.Qt.green)
            yangshe.setFont(c)
            yangshe.setBackground(d)
            self.calendarWidget.repaint()
            for i in dayyourenwu2:
                self.calendarWidget.setDateTextFormat(i,yangshe)

        ### 链接完成任务窗口,任务完成和任务废弃的分别执行函数
        def renwuwancheng():
            global renwu,zengliangwanchengrenwu,dianshu
            import dialog11_wanchengrenwu
            zengliangwanchengrenwu = []
            zengliangwanchengrenwu = dialog11_wanchengrenwu.add
            renwu = dialog11_wanchengrenwu.renwu
            dianshu = dialog11_wanchengrenwu.dianshu
            if self.radioButton_2.isChecked():
                renwuxianshi()
            if self.radioButton.isChecked():
                renwuxianshi2()
            chongxiejinbendian()
            rilibianse()
            zhengliangxianshiwanchengrenwu()
            dialog11_wanchengrenwu.add = []
        def renwufeiqi():
            global renwu
            import dialog11_wanchengrenwu
            renwu = dialog11_wanchengrenwu.renwu
            rilibianse()
            if self.radioButton_2.isChecked():
                renwuxianshi()
            if self.radioButton.isChecked():
                renwuxianshi2()
        def wanchengrenwu():
            import dialog11_wanchengrenwu
            Dialog = QtWidgets.QDialog()
            ui = dialog11_wanchengrenwu.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ###完成任务的不同按钮链接到不同函数
            #首先确定之后，任务需要重载，完成任务需要增量显示
            ui.pushButton.clicked.connect(renwuwancheng)
            Dialog.accepted.connect(renwufeiqi)

        ### 打开添加日志窗口
        def gengxinrizhi():
            import dialog12_chuangjianrizhi
            global rizhi
            rizhi = dialog12_chuangjianrizhi.rizhi
            rizhixianshi()
        def tianjiarizhi():
            import dialog12_chuangjianrizhi
            Dialog = QtWidgets.QDialog()
            ui = dialog12_chuangjianrizhi.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(gengxinrizhi)

        ### 完成日志窗口
        def gengxinwanchengrizhi():
            import dialog13_wanchengrizhi
            global rizhi,rizhifinish,dianshu, zengliangwanchengrizhi
            rizhi = dialog13_wanchengrizhi.rizhi
            rizhifinish = dialog13_wanchengrizhi.rizhifinish
            dianshu = dialog13_wanchengrizhi.dianshu
            zengliangwanchengrizhi = dialog13_wanchengrizhi.add
            chongxiejinbendian()
            rizhixianshi()
            wanchengrizhizengliangxianshi()
            dialog13_wanchengrizhi.add = []
        def rizhifeiqi():
            import dialog13_wanchengrizhi
            global rizhi
            rizhi = dialog13_wanchengrizhi.rizhi
            rizhixianshi()
        def wanchengrizhi():
            import dialog13_wanchengrizhi
            Dialog = QtWidgets.QDialog()
            ui = dialog13_wanchengrizhi.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(gengxinwanchengrizhi)
            Dialog.accepted.connect(rizhifeiqi)

        ### 点击已经完成的日志得到小弹窗
        def dianjiwanchengrizhi(date):
            global rizhifinish
            import dialog13fujia_rizhixianshi
            Form = dialog13fujia_rizhixianshi.window()
            ui = dialog13fujia_rizhixianshi.Ui_Form()
            ui.setupUi(Form)
            widget = ui.treeWidget
            widget.clear()
            for i in rizhifinish:
                if i[1] == int(date.whatsThis()):
                    widget.setIndentation(10)
                    widget.headerItem().setText(0,i[0]+str(i[1])+'的子任务：')
                    item_0 = QtWidgets.QTreeWidgetItem(widget)
                    neirong = QtWidgets.QLabel(widget)
                    neirong.setText("<span style=\" font-size:9pt; color:#6F6F6F;\">（单击小三角形展开，单击任务文字退出）</span>")
                    widget.setItemWidget(item_0,0,neirong)
                    for kr in range(len(i)):
                        if kr in [0,1,2,3,4,5,6,7]:
                            continue
                        else:
                            if round(i[kr][1]*1000,3) == round(i[kr][1]*1000,0):
                                item_0 = QtWidgets.QTreeWidgetItem(widget)
                                xuhao = str(int(str(int(round(i[kr][1]*10000000,0)))[:-7]))+'.'+str(int(str(int(round(i[kr][1]*10000000,0)))[-7:-4]))
                                value = xuhao+'.'+i[kr][0]+'：'+i[kr][2]
                                length = len(value)
                                utf8_length = len(value.encode('utf-8'))
                                length = (utf8_length - length)/2 + length
                                neirong = QtWidgets.QLabel(widget)
                                neirong.setFixedHeight((int(length/58)+1)*21)
                                neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
                                neirong.setWordWrap(True)
                                neirong.setText(value)
                                neirong.setToolTip('添加时间：'+i[kr][6]+'；'+'备注：'+i[kr][3])
                                widget.setItemWidget(item_0,0,neirong)
                                app.processEvents()
                                continue
                            if round(i[kr][1]*100000,5) == round(i[kr][1]*100000,0):
                                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                                xuhao = str(int(str(int(round(i[kr][1]*10000000,0)))[:-7]))+'.'+str(int(str(int(round(i[kr][1]*10000000,0)))[-7:-4]))+'.'+str(int(str(int(round(i[kr][1]*10000000,0)))[-4:-2]))
                                value = xuhao+'.'+i[kr][0]+'：'+i[kr][2]
                                length = len(value)
                                utf8_length = len(value.encode('utf-8'))
                                length = (utf8_length - length)/2 + length
                                neirong = QtWidgets.QLabel(widget)
                                neirong.setFixedHeight((int(length/56)+1)*21)
                                neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
                                neirong.setWordWrap(True)
                                neirong.setText(value)
                                neirong.setToolTip('添加时间：'+i[kr][6]+'；'+'备注：'+i[kr][3])
                                widget.setItemWidget(item_1,0,neirong)
                                app.processEvents()
                                continue
                            if round(i[kr][1]*10000000,2) == round(i[kr][1]*10000000,7):
                                item_2 = QtWidgets.QTreeWidgetItem(item_1)
                                xuhao = str(int(str(int(round(i[kr][1]*10000000,0)))[:-7]))+'.'+str(int(str(int(round(i[kr][1]*10000000,0)))[-7:-4]))+'.'+str(int(str(int(round(i[kr][1]*10000000,0)))[-4:-2]))+'.'+str(int(str(int(round(i[kr][1]*10000000,0)))[-2:]))
                                value = xuhao+'.'+i[kr][0]+'：'+i[kr][2]
                                length = len(value)
                                utf8_length = len(value.encode('utf-8'))
                                length = (utf8_length - length)/2 + length
                                neirong = QtWidgets.QLabel(widget)
                                neirong.setFixedHeight((int(length/56)+1)*21)
                                neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
                                neirong.setWordWrap(True)
                                neirong.setText(value)
                                neirong.setToolTip('添加时间：'+i[kr][6]+'；'+'备注：'+i[kr][3])
                                widget.setItemWidget(item_2,0,neirong)
                                app.processEvents()
                                continue

                    break
            Form.show()

        ### 打开添加并调用重载显示
        def jianglichongzai():
            global jiangli
            import dialog14_zengjiajiangli
            jiangli = dialog14_zengjiajiangli.jiangli
            jianglixianshi()
        def tianjiajiangli():
            import dialog14_zengjiajiangli
            Dialog = QtWidgets.QDialog()
            ui = dialog14_zengjiajiangli.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(jianglichongzai)
            pass

        ### 奖励自己窗口
        def jianglizijizenglianggenxin(): ###奖励自己增量更新
            import dialog15_jiangliziji
            global jiangliget,zengliangjiangli,dianshu
            jiangliget = dialog15_jiangliziji.jiangliget
            zengliangjiangli = dialog15_jiangliziji.add
            dianshu = dialog15_jiangliziji.dianshu
            chongxiejinbendian()
            jianglizengliang()
        def jiangliziji():
            import dialog15_jiangliziji
            Dialog = QtWidgets.QDialog()
            ui = dialog15_jiangliziji.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(jianglizijizenglianggenxin)
            pass

        ###增加愿望窗口
        def yuanwanggengxin():
            global yuanwang, dianshu
            import dialog16_yuanwang
            dianshu = dialog16_yuanwang.dianshu
            yuanwang = dialog16_yuanwang.yuanwang
            chongxiejinbendian()
            zhuangzaiyuanwang()
        def zengjiayuanwang():
            import dialog16_yuanwang
            Dialog = QtWidgets.QDialog()
            ui = dialog16_yuanwang.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(yuanwanggengxin)
            pass

        ###默认只显示200条已完成任务，奖励，愿望，若需要显示全部，调用此命令
        def wanchengrenwushuliang(x):
            global renwufinish
            newcount = 201
            if x == 0:
                self.comboBox.setEnabled(False)
                for i in range(self.listWidget_6.count()-1,0,-1):
                    if i < 200:
                        break
                    else:
                        self.listWidget_6.takeItem(i)
                        app.processEvents()
                self.comboBox.setEnabled(True)

            if x == 1:
                self.comboBox.setEnabled(False)
                for i in range(len(renwufinish)):
                  if i < 200:
                        continue
                  else:
                    leixing = ['工作','生活','理财','琐事','自我提升','其他']
                    zhongyaoxing = ['重要且紧急','重要但不紧急','紧急但不重要','不重要不紧急']
                    item = QtWidgets.QListWidgetItem()
                    # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                    value = '('+str(newcount)+') '+leixing[renwufinish[i][2]-1]+'：'+renwufinish[i][4]+'（计划时间：'+renwufinish[i][1]+'）'
                    length = len(value)
                    utf8_length = len(value.encode('utf-8'))
                    length = (utf8_length - length)/2 + length
                    font = QtGui.QFont()
                    font.setPointSize(int(length/40+1)*10)
                    item.setFont(font)
                    #######################################
                    self.listWidget_6.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget_6)
                    item1.setText("<html><head/><body><p><span style=\" font-size:9pt; color:#6F6F6F;\">"+value+"</span></p></body></html>")
                    item1.setToolTip(zhongyaoxing[renwufinish[i][3]-1]+'，'+renwufinish[i][6]+'\n'+'描述：'+renwufinish[i][5])
                    item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                    item1.setWordWrap(True)
                    self.listWidget_6.setItemWidget(item,item1)
                    app.processEvents()
                    newcount += 1
                self.comboBox.setEnabled(True)
        self.comboBox.currentIndexChanged.connect(wanchengrenwushuliang)
        #获得奖励数量
        def huodejianglishuliang(x):
            global jiangliget
            newcount = 201
            if x == 0:
                self.comboBox_3.setEnabled(False)
                for i in range(self.listWidget_8.count()-1,0,-1):
                    if i < 200:
                        break
                    else:
                        self.listWidget_8.takeItem(i)
                        app.processEvents()
                self.comboBox_3.setEnabled(True)
            if x == 1:
                self.comboBox_3.setEnabled(False)
                for i in range(len(jiangliget)):
                    if i < 200:
                        continue
                    else:
                        item = QtWidgets.QListWidgetItem()
                        value =  '('+str(newcount)+') '+jiangliget[i][0]+'：'+jiangliget[i][1]
                        item.setText(value)
                        font = QtGui.QFont()
                        font.setBold(True)
                        font.setPointSize(9)
                        brush = QtGui.QBrush(QtGui.QColor(185, 127,127))
                        brush.setStyle(QtCore.Qt.NoBrush)
                        item.setForeground(brush)
                        item.setFont(font)
                        self.listWidget_8.addItem(item)
                        app.processEvents()
                        newcount += 1
                self.comboBox_3.setEnabled(True)
        self.comboBox_3.currentIndexChanged.connect(huodejianglishuliang)
        #完成愿望数量
        def wanchengyuanwangshuliang(x):
            global yuanwang
            if x == 0:
                self.comboBox_2.setEnabled(False)
                zhuangzaiyuanwang()
                self.comboBox_2.setEnabled(True)
            if x == 1:
                self.comboBox_2.setEnabled(False)
                # print(len(yuanwang[1]))
                y = 0
                for i in range(len(yuanwang[1])):
                    if yuanwang[1][i] == yuanwang[1][0]:
                        continue
                    if yuanwang[1][i][0] == int(yuanwang[1][i][0]):
                        y += 1
                    if y <= 100:
                        continue
                    else:
                        if yuanwang[1][i][0] == int(yuanwang[1][i][0]):
                            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
                            brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                            brush.setStyle(QtCore.Qt.SolidPattern)
                            value ='（已完成）'+str(int(yuanwang[1][i][0]))+' ('+yuanwang[1][i][5]+')：'+yuanwang[1][i][3]
                            length = len(value)
                            utf8_length = len(value.encode('utf-8'))
                            length = (utf8_length - length)/2 + length
                            neirong = QtWidgets.QLabel(self.treeWidget)
                            neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                            neirong.setFixedHeight((int(length/99)+1)*21)
                            neirong.setWordWrap(True)
                            neirong.setToolTip(yuanwang[1][i][4])
                            neirong.setText("<span style=\" font-size:10pt;font-weight:bold;; color:#8090b0;\">"+value+"</span>")
                            self.treeWidget_3.setItemWidget(item_0,0,neirong)
                            app.processEvents()
                        else:
                            item_1 = QtWidgets.QTreeWidgetItem(item_0)
                            brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                            brush.setStyle(QtCore.Qt.SolidPattern)
                            value = str(yuanwang[1][i][0])+' ('+yuanwang[1][i][5]+')：'+yuanwang[1][i][3]+'('+str(yuanwang[1][i][1])+'%)'
                            length = len(value)
                            utf8_length = len(value.encode('utf-8'))
                            length = (utf8_length - length)/2 + length
                            neirong = QtWidgets.QLabel(self.treeWidget)
                            neirong.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                            neirong.setFixedHeight((int(length/108)+1)*21)
                            neirong.setWordWrap(True)
                            neirong.setToolTip(yuanwang[1][i][4])
                            neirong.setText(value)
                            self.treeWidget_3.setItemWidget(item_1,0,neirong)
                            app.processEvents()
                self.comboBox_2.setEnabled(True)
        self.comboBox_2.currentIndexChanged.connect(wanchengyuanwangshuliang)
        #完成日志数量
        def wanchengrizhishuliang(x):
            global rizhifinish
            if x == 0:
                self.comboBoxrizhi.setEnabled(False)
                for i in range(self.listrizhiwancheng.count()-1,0,-1):
                    if i < 200:
                        break
                    else:
                        self.listrizhiwancheng.takeItem(i)
                        app.processEvents()
                self.comboBoxrizhi.setEnabled(True)
            if x == 1:
                self.comboBoxrizhi.setEnabled(False)
                for i in range(len(rizhifinish)):
                    if i < 200:
                        continue
                    else:
                        item_0 = QtWidgets.QListWidgetItem()
                        brush = QtGui.QBrush(QtGui.QColor(234, 255, 227))
                        brush.setStyle(QtCore.Qt.SolidPattern)
                        brush2 = QtGui.QBrush(QtGui.QColor(227, 243, 255))
                        brush2.setStyle(QtCore.Qt.SolidPattern)
                        value = str(rizhifinish[i][1])+'.'+rizhifinish[i][0]+'：'+rizhifinish[i][2]
                        length = len(value)
                        utf8_length = len(value.encode('utf-8'))
                        length = (utf8_length - length)/2 + length
                        font = QtGui.QFont()
                        font.setPointSize((int(length/42)+1)*10)
                        neirong = QtWidgets.QLabel(self.treeWidget)
                        neirong.setWordWrap(True)
                        item_0.setFont(font)
                        self.listrizhiwancheng.addItem(item_0)
                        if rizhifinish[i][0] =='主线任务':
                            item_0.setBackground(brush)
                            neirong.setText("<span style=\" font-size:9pt; color:#7b1714;\">"+value+"</span>")
                        else:
                            item_0.setBackground(brush2)
                            neirong.setText("<span style=\" font-size:9pt; color:#6F6F6F;\">"+value+"</span>")
                        item_0.setWhatsThis(str(rizhifinish[i][1]))
                        item_0.setToolTip(rizhifinish[i][7]+'；添加时间：'+rizhifinish[i][6]+'；'+'已获得奖励经验：'+str(rizhifinish[i][4])+'，娱乐点：'+str(rizhifinish[i][5])+'\n'+'备注：'+rizhifinish[i][3])
                        self.listrizhiwancheng.setItemWidget(item_0,neirong)
                        app.processEvents()
                self.comboBoxrizhi.setEnabled(True)
        self.comboBoxrizhi.currentIndexChanged.connect(wanchengrizhishuliang)

        ####删除愿望
        def quedingshanchuyuanwang():
            global yuanwang
            import dialog17_feiqiyuanwang
            yuanwang = dialog17_feiqiyuanwang.yuanwang
            zhuangzaiyuanwang()
        def shanchuyuanwang():
            import dialog17_feiqiyuanwang
            Dialog = QtWidgets.QDialog()
            ui = dialog17_feiqiyuanwang.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            Dialog.accepted.connect(quedingshanchuyuanwang)

        #### 删除奖励
        def quedingshanchujiangli():
            import  dialog18_shanchujiangli
            global jiangli
            jiangli = dialog18_shanchujiangli.jiangli
            jianglixianshi()
        def shanchujiangli():
            import dialog18_shanchujiangli
            Dialog = QtWidgets.QDialog()
            ui = dialog18_shanchujiangli.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(quedingshanchujiangli)

        ####删除能力
        def quedingshanchunengli():
            import dialog19_shanchunengli
            global nengli,dianshu
            nengli = dialog19_shanchunengli.nengli
            chongxiejinbendian()
            self.listWidget.clear()
            global count
            count = 1
            for i in nengli:
                item = QtWidgets.QListWidgetItem()
                # 取得天赋和能力显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count)+') '+i[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/43+1)*11)
                item.setFont(font)
                ####################################
                self.listWidget.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget)
                brush = QtGui.QBrush(QtGui.QColor(180, 251, 187))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                if i[0][0:2] == '天赋':
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#0e9000;\">"+value+"</span>")
                else:
                    item1.setText("<span style=\" font-size:10pt;font-weight:bold; color:#123e80;\">"+value+"</span>")
                item1.setToolTip(i[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget.setItemWidget(item,item1)
                app.processEvents()
                count += 1
        def shanchunengli():
            import dialog19_shanchunengli
            Dialog = QtWidgets.QDialog()
            ui = dialog19_shanchunengli.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(quedingshanchunengli)

        ####删除装备
        def quedingshanchuzhuangbei():
            import dialog20_shanchuzhuangbei
            global nengli,dianshu
            zhuangbei = dialog20_shanchuzhuangbei.zhuangbei
            chongxiejinbendian()
            self.listWidget_2.clear()
            global count2
            count2 = 1
            for i in zhuangbei:
                item = QtWidgets.QListWidgetItem()
                # 取得装备显示文字中的字符串长度，并通过不同长度来调整表格大小
                value = '('+str(count2)+') '+i[0]
                length = len(value)
                utf8_length = len(value.encode('utf-8'))
                length = (utf8_length - length)/2 + length
                font = QtGui.QFont()
                font.setPointSize(int(length/43+1)*11)
                item.setFont(font)
                ####################################
                self.listWidget_2.addItem(item)
                item1 = QtWidgets.QLabel(self.listWidget_2)
                brush = QtGui.QBrush(QtGui.QColor(180, 250, 251))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                item1.setText("<span style=\" font-size:10pt;font-weight:bold;\">"+value+"</span>")
                item1.setToolTip(i[1])
                item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
                item1.setWordWrap(True)
                self.listWidget_2.setItemWidget(item,item1)
                app.processEvents()
                count2 += 1
        def shanchuzhuangbei():
            import dialog20_shanchuzhuangbei
            Dialog = QtWidgets.QDialog()
            ui = dialog20_shanchuzhuangbei.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(quedingshanchuzhuangbei)

        ###作息
        def zuoxigengxin():
            import dialog21_zuoxianpai
            global dianshu
            dianshu = dialog21_zuoxianpai.dianshu
            zuoxixianshi()
        def dakaizuoxi():
            import dialog21_zuoxianpai
            Dialog = QtWidgets.QDialog()
            ui = dialog21_zuoxianpai.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton_2.clicked.connect(zuoxigengxin)

        chushihua()
        zhuangzai()
        ###单独显示任务模块
        self.radioButton_2.setChecked(True)
        renwuxianshi()
        ############
        zuoxixianshi()###单独显示作息时间模块
        rilibianse()###日历变色
        rizhixianshi()###单独显示日志模块
        jianglixianshi()###单独显示奖励模块
        zhuangzaiyuanwang()###单独装载愿望模块

        self.pushButton_21.clicked.connect(dakaizuoxi)##作息编辑
        self.action.triggered.connect(dakaitongbu)   #按钮连接同步
        self.pushButton.clicked.connect(shedingdianshu) #按钮连接设定基本点数
        self.pushButton_8.clicked.connect(shedingnengli) #按钮连接设定能力
        self.pushButton_13.clicked.connect(shedingzhuangbei) #按钮连接设定装备
        self.pushButton_5.clicked.connect(tianjiaxiguan) #按钮链接添加习惯
        self.pushButton_shanxiguan.clicked.connect(shanchuxiguan) #按钮链接删除习惯
        self.pushButton_4.clicked.connect(shedingjinrixiguan) ##按钮链接设定今日习惯
        self.pushButton_6.clicked.connect(wanchengxiguan)##按钮链接完成习惯
        self.pushButton_7.clicked.connect(tianjiarenwu)##按钮链接添加任务
        self.listWidget_5.itemPressed.connect(dianjirenwuxiangqing)##点击任务得到任务详情
        ### 日历显示相关的设置
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        self.calendarWidget.setPalette(palette)
        self.calendarWidget.clicked['QDate'].connect(rilixianshi)
        ##################################
        self.radioButton.toggled.connect(renwuxianshi2)  ####调整任务显示模式，类型或重要性
        self.radioButton_2.toggled.connect(renwuxianshi) ####调整任务显示模式，类型或重要性
        self.pushButton_10.clicked.connect(wanchengrenwu)###完成任务按钮链接
        self.pushButton_3.clicked.connect(tianjiarizhi)###添加日志按钮链接
        self.pushButton_2.clicked.connect(wanchengrizhi)###完成日志按钮
        self.listrizhiwancheng.itemPressed.connect(dianjiwanchengrizhi)   ##点击已完成日志得到日志详情
        self.pushButton_11.clicked.connect(tianjiajiangli)#### 添加奖励
        self.pushButton_12.clicked.connect(jiangliziji)### 自己活得奖励
        self.pushButton_9.clicked.connect(zengjiayuanwang)###添加愿望
        self.pushButton_14.clicked.connect(shanchuyuanwang)##删除愿望
        self.pushButton_15.clicked.connect(shanchujiangli)##删除奖励
        self.pushButton_17.clicked.connect(shanchunengli)##删除能力
        self.pushButton_16.clicked.connect(shanchuzhuangbei)##删除能力

        self.action_2.setEnabled(False)##警戒窗口暂时未开发

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyRPG alpha version 1.0 Powered by Alwayswdc"))
        self.zhuangbei.setText(_translate("MainWindow", "装备"))
        self.pushButton_13.setText(_translate("MainWindow", "添加"))
        self.jingyanheyuledian.setText(_translate("MainWindow", "经验和娱乐点"))
        self.jibenshuxingdian.setText(_translate("MainWindow", "基本属性点"))
        self.pushButton.setText(_translate("MainWindow", "设定点数"))
        self.tianfuhenengli.setText(_translate("MainWindow", "天赋和能力"))
        self.pushButton_8.setText(_translate("MainWindow", "添加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "属性"))
        self.pushButton_5.setText(_translate("MainWindow", "添加习惯"))
        self.pushButton_4.setText(_translate("MainWindow", "设定每日习惯"))
        self.label_9.setText(_translate("MainWindow", "所有习惯（好坏均有）"))
        self.pushButton_6.setText(_translate("MainWindow", "完成习惯"))
        self.label_8.setText(_translate("MainWindow", "每日必完成习惯"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "习惯"))
        self.label_7.setText(_translate("MainWindow", "已经完成的任务"))
        self.pushButton_7.setText(_translate("MainWindow", "添加任务"))
        self.pushButton_10.setText(_translate("MainWindow", "完成任务"))
        self.label_6.setText(_translate("MainWindow", "任务安排"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "每日任务"))
        self.pushButton_3.setText(_translate("MainWindow", "添加日志"))
        self.pushButton_2.setText(_translate("MainWindow", "完成任务"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "任务日志-进行中"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "任务日志"))
        self.pushButton_12.setText(_translate("MainWindow", "奖励自己"))
        self.label_10.setText(_translate("MainWindow", "所有奖励"))
        self.label_11.setText(_translate("MainWindow", "已获得的奖励"))
        self.pushButton_11.setText(_translate("MainWindow", "增加奖励"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "奖励"))
        self.pushButton_9.setText(_translate("MainWindow", "添加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "愿望清单和进度"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.action.setText(_translate("MainWindow", "同步"))
        self.action_2.setText(_translate("MainWindow", "设置警戒状态"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())