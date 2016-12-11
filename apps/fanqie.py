# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fanqie.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 186)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("设置")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setText("开始番茄")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 0, 2, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 5, 0, 1, 2)
        self.listWidget.hide()
        self.listWidget.setFixedHeight(300)


        ###读取配置，初始化变量
        def chushihua():
            global shezhi, fanqielishi, xunhuan,jinrifanqie,date,today
            xunhuan = 1
            import os
            import pickle
            import datetime
            date = datetime.date.today().year*365+datetime.date.today().month*30+datetime.date.today().day
            today = str(datetime.date.today())
            if os.path.exists('D:/MyRPG/fanqie.dat'):
                path = open('D:/MyRPG/fanqie.dat','rb')
                try:
                    shezhi,fanqielishi = pickle.load(path)
                    try:
                        if fanqielishi[0][0] == date:
                            jinrifanqie = fanqielishi[0][1]
                            self.label.setText('今日获得番茄：'+str(jinrifanqie)+'丨连续获得番茄：'+str(int(xunhuan/2)))
                        else:
                            jinrifanqie = 0
                            self.label.setText('今日获得番茄：'+str(jinrifanqie)+'丨连续获得番茄：'+str(int(xunhuan/2)))
                    except:
                        jinrifanqie = 0
                        self.label.setText('今日获得番茄：'+str(jinrifanqie)+'丨连续获得番茄：'+str(int(xunhuan/2)))
                except:
                    shezhi = [25,5,15,4]
                    fanqielishi = []
                    path = open('D:/MyRPG/fanqie.dat','wb')
                    pickle.dump((shezhi,fanqielishi),path)
                    path.close()
                    del path
                    jinrifanqie = 0
                    self.label.setText('今日获得番茄：'+str(jinrifanqie)+'丨连续获得番茄：'+str(int(xunhuan/2)))
                    return
                path.close()
                del path
            else:
                shezhi = [25,5,15,4]
                fanqielishi = []
                path = open('D:/MyRPG/fanqie.dat','wb')
                pickle.dump((shezhi,fanqielishi),path)
                path.close()
                del path
                jinrifanqie = 0
                self.label.setText('今日获得番茄：'+str(jinrifanqie)+'丨连续获得番茄：'+str(int(xunhuan/2)))

        ###初始显示
        def chushixianshi():
            fanqieshijian = shezhi[0]*60
            fenzhong = int(round(fanqieshijian/60,0))
            miao = fanqieshijian%60

            if fenzhong < 10:
                fenzhong = str(0)+str(fenzhong)
            elif fenzhong == 0:
                fenzhong = '00'
            elif fenzhong >= 10:
                fenzhong =str(fenzhong)

            if miao < 10:
                miao = str(0)+str(miao)
            elif miao == 0 :
                miao = '00'
            elif miao > 10:
                miao = str(miao)
            xianshishijian = str(fenzhong)+':'+miao
            self.lcdNumber.display(xianshishijian)
            self.label.setText('今日获得番茄：'+str(jinrifanqie)+'丨连续获得番茄：'+str(int(xunhuan/2)))
            self.progressBar.setFormat('            ')

            # print(shezhi)
            # print(fanqielishi)

        ###开始计时时的状态
        def kaishi():

            global shezhi,timeleft,xunhuan,process
            if xunhuan % 2 == 1:
                import winsound
                winsound.PlaySound('begin.wav',winsound.SND_ASYNC)
                timeleft = shezhi[0]*60
                process = shezhi[0]*60
                self.progressBar.setStyleSheet('color:#a20000')
                self.progressBar.setFormat('   工作中   ')
                self.lcdNumber.setStyleSheet('color:#a20000')

            elif xunhuan % 2 == 0 and xunhuan % (shezhi[3]*2) != 0:
                timeleft = shezhi[1]*60
                process = shezhi[1]*60
                self.progressBar.setStyleSheet('color:#0e9000')
                self.progressBar.setFormat('   短休息中 ')
                self.lcdNumber.setStyleSheet('color:#0e9000')
            elif xunhuan % 2 == 0 and xunhuan % (shezhi[3]*2) == 0:
                timeleft = shezhi[2]*60
                process = shezhi[2]*60
                self.progressBar.setStyleSheet('color:#0e9000')
                self.progressBar.setFormat('   长休息中 ')
                self.lcdNumber.setStyleSheet('color:#0e9000')
            timer.start(1000)
            self.pushButton.setText('停止番茄\n（停止后\n可关闭）')
            self.pushButton_2.setEnabled(False)
            self.pushButton.disconnect()
            self.pushButton.clicked.connect(timestop)

        ### 停止番茄
        def timestop():
            global shezhi, fanqielishi,jinrifanqie,date,today
            timer.stop()

            self.pushButton.setText('开始番茄')
            self.pushButton.disconnect()
            self.pushButton.clicked.connect(kaishi)
            self.progressBar.setValue(100)
            self.progressBar.setFormat('            ')
            self.lcdNumber.setStyleSheet('color:#000000')
            self.pushButton_2.setEnabled(True)

            ### 保存今日番茄数量
            if fanqielishi == []:
                add = [date,jinrifanqie,today]
                fanqielishi.insert(0,add)
            else:
                if fanqielishi[0][0] == date:
                    fanqielishi[0][1] = jinrifanqie
                else:
                    add = [date,jinrifanqie,today]
                    fanqielishi.insert(0,add)
            import pickle
            path = open('D:/MyRPG/fanqie.dat','wb')
            pickle.dump((shezhi,fanqielishi),path)
            path.close()
            del path

            ### 重载
            chushihua()
            chushixianshi()
            pass

        ### 计时变化
        def jishi():
            global timeleft,xunhuan,jinrifanqie,shezhi,fanqielishi,process
            if timeleft > 0:
                timeleft = timeleft - 1
                fenzhong = int(round(timeleft/60,2))
                miao = timeleft%60

                if fenzhong < 10:
                    fenzhong = str(0)+str(fenzhong)
                elif fenzhong == 0:
                    fenzhong = '00'
                elif fenzhong >= 10:
                    fenzhong =str(fenzhong)

                if miao < 10:
                    miao = str(0)+str(miao)
                elif miao == 0:
                    miao = '00'
                elif miao >= 10:
                    miao =str(miao)
                xianshishijian = str(fenzhong)+':'+miao
                self.progressBar.setValue(int((timeleft/process)*100))
                self.lcdNumber.display(xianshishijian)

            if timeleft == 0:
                if xunhuan % 2 == 1:
                    jinrifanqie += 1
                    # print(xunhuan)
                    self.label.setText('今日获得番茄：'+str(jinrifanqie)+'丨连续获得番茄：'+str(int(xunhuan/2)+1))
                    import winsound
                    winsound.PlaySound('finish.wav',winsound.SND_ASYNC)
                xunhuan += 1
                kaishi()

        chushihua()
        chushixianshi()
        global timer
        timer = QtCore.QTimer()
        timer.timeout.connect(jishi)
        self.pushButton.clicked.connect(kaishi)



        ##设置
        def shezhiwancheng():
            chushihua()
            chushixianshi()
        def shezhicanshu():
            import fanqieshezhi
            Dialog = QtWidgets.QDialog()
            ui = fanqieshezhi.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(shezhiwancheng)
        self.pushButton_2.clicked.connect(shezhicanshu)

        ##显示历史番茄数量
        def lishifanqie():
            global shezhi, fanqielishi
            import pickle
            path = open('D:/MyRPG/fanqie.dat','rb')
            shezhi,fanqielishi = pickle.load(path)
            path.close()
            del path
            for i in fanqielishi:
                item = QtWidgets.QListWidgetItem()
                value = '时间：'+i[2]+'     '+'番茄数：'+str(i[1])
                item.setText(value)
                self.listWidget.addItem(item)
        lishifanqie()
        def hideandshow():
            global a
            if a % 2 == 0:
                self.listWidget.hide()
                x = Dialog.x()
                y = Dialog.y()
                Dialog.hide()
                Dialog.show()
                Dialog.setGeometry(x+8,y+30,Dialog.width(),Dialog.height())
                Dialog.resize(Dialog.width(),Dialog.height()-306)
                a += 1
            elif a % 2 == 1:
                Dialog.resize(Dialog.width(),Dialog.height()+306)
                self.listWidget.show()
                a += 1
        global a
        a = 1
        self.pushButton_3.clicked.connect(hideandshow)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "番茄时间"))
        self.pushButton_3.setText(_translate("Dialog", "番茄历史"))
        self.label.setText(_translate("Dialog", "今日获得番茄数："))

class window(QtWidgets.QDialog,Ui_Dialog):

    global timer
    def closeEvent(self, event):
            if fanqielishi == []:
                add = [date,jinrifanqie,today]
                fanqielishi.insert(0,add)
            else:
                if fanqielishi[0][0] == date:
                    fanqielishi[0][1] = jinrifanqie
                else:
                    add = [date,jinrifanqie,today]
                    fanqielishi.insert(0,add)
            import pickle
            path = open('D:/MyRPG/fanqie.dat','wb')
            pickle.dump((shezhi,fanqielishi),path)
            path.close()
            del path
            if timer.isActive():
                event.ignore()
            else:
                event.accept()







import sys

# app = QtWidgets.QApplication(sys.argv)

Dialog = window()
ui = Ui_Dialog()
ui.setupUi(Dialog)

# Dialog.show()
# sys.exit(app.exec_())