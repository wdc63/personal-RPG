# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2_tongbu.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
global state,fuwuqi
global  ip,name,password,tim,y
y = 1
state = 0

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        """
        :type self: object
        """
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 174)
        Dialog.setModal(True)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 2, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 1, 1, 3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 7, 1, 1, 3)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 8, 1, 1, 3)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 3, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ########初始化
        def shuaxin():
          import pickle
          import os
          global fuwuqi
          if os.path.exists('D:/MyRPG/fuwuqi.dat'):
            try:
              path = open('D:/MyRPG/fuwuqi.dat','rb')
              fuwuqi = pickle.load(path)
              path.close()
              del path
            except:
              fuwuqi = [['','','','0'],['','','','0'],['','','','0']]
              path = open('D:/MyRPG/fuwuqi.dat','wb')
              pickle.dump(fuwuqi,path)
              path.close()
              del path
          else:
            fuwuqi = [['','','','0'],['','','','0'],['','','','0']]
            path = open('D:/MyRPG/fuwuqi.dat','wb')
            pickle.dump(fuwuqi,path)
            path.close()
            del path
        def chushixianshi():
              global fuwuqi
              self.lineEdit.setText(fuwuqi[0][0])
              self.lineEdit_2.setText(fuwuqi[0][1])
              self.lineEdit_3.setText(fuwuqi[0][2])
              self.lineEdit_4.setText(fuwuqi[0][3])
              # print(fuwuqi)

        def fuwuqi1shuaxin():
            global fuwuqi
            shuaxin()
            self.lineEdit.setText(fuwuqi[0][0])
            self.lineEdit_2.setText(fuwuqi[0][1])
            self.lineEdit_3.setText(fuwuqi[0][2])
            self.lineEdit_4.setText(fuwuqi[0][3])
            global state
            state = 1
        def fuwuqi2shuaxin():
            global fuwuqi
            shuaxin()
            self.lineEdit.setText(fuwuqi[1][0])
            self.lineEdit_2.setText(fuwuqi[1][1])
            self.lineEdit_3.setText(fuwuqi[1][2])
            self.lineEdit_4.setText(fuwuqi[1][3])


            global state
            state = 2
        def fuwuqi3shuaxin():
            global fuwuqi
            shuaxin()
            self.lineEdit.setText(fuwuqi[2][0])
            self.lineEdit_2.setText(fuwuqi[2][1])
            self.lineEdit_3.setText(fuwuqi[2][2])
            self.lineEdit_4.setText(fuwuqi[2][3])


            global state
            state = 3
        def baocun():
            global state,fuwuqi
            import pickle
            if state == 1:
                writein = [self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text()]
                fuwuqi[0] = writein
            if state == 2:
                writein = [self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text()]
                fuwuqi[1] = writein
            if state == 3:
                writein = [self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text()]
                fuwuqi[2] = writein
            path = open('D:/MyRPG/fuwuqi.dat','wb')
            pickle.dump(fuwuqi,path)
            path.close()
            # print(fuwuqi,state)
            del path
        def gengxin():
            global ip,name,password,tim
            ip = self.lineEdit.text()
            name = self.lineEdit_2.text()
            password = self.lineEdit_3.text()
            tim = self.lineEdit_4.text()
            if False:
                Dialog.close()

        self.lineEdit.editingFinished.connect(gengxin)
        self.lineEdit_2.editingFinished.connect(gengxin)
        self.lineEdit_3.editingFinished.connect(gengxin)
        self.lineEdit_4.editingFinished.connect(gengxin)

        def timestop(x):
            global y
            x = x+1
            timer.stop()
            if y == 2:
                self.label_4.setText('同步失败')
                x = '完成'
                return x
            if y == 3:
                self.label_4.setText('同步成功')
                x = '完成'
                return x

        def jiemianbianhua():
            global jishu,jishuxianshi
            self.label_4.setText(jishuxianshi[jishu%8])
            jishu += 1

        def FTPwork():
            timer.start(400)
            self.thread = WorkThread()
            self.thread.start()
            self.thread.trigger.connect(timestop)

        global jishu,jishuxianshi
        jishu = 0
        jishuxianshi = ['同步中','同步中.','同步中..','同步中...','同步中.../',"同步中..."+"\\",'同步中.../',"同步中..."+"\\"]
        timer = QtCore.QTimer()
        timer.timeout.connect(jiemianbianhua)

        # def tongbu():
        #     global y
        #     import time
        #     self.thread = WorkThread()
        #     self.thread.start()
        #     x = ''
        #     while x == '':
        #         self.label_4.setText('同步中')
        #         app.processEvents()
        #         time.sleep(0.4)
        #         app.processEvents()
        #         self.label_4.setText('同步中.')
        #         app.processEvents()
        #         time.sleep(0.4)
        #         self.label_4.setText('同步中..')
        #         app.processEvents()
        #         time.sleep(0.4)
        #         self.label_4.setText('同步中...')
        #         app.processEvents()
        #         time.sleep(0.4)
        #         self.label_4.setText('同步中.../')
        #         app.processEvents()
        #         time.sleep(0.4)
        #         self.label_4.setText("同步中..."+"\\")
        #         app.processEvents()
        #         time.sleep(0.4)
        #         self.label_4.setText('')
        #         app.processEvents()
        #         self.thread.trigger.connect(wancheng)
        #         x = wancheng(1)
        #     y = 1
        #
        # def wancheng(z):
        #     z = z+2            ##z没用
        #     global y
        #     if y == 1:
        #         x = ''
        #         return x
        #     if y == 2:
        #         self.label_4.setText('同步失败')
        #         x = '完成'
        #         return x
        #     if y == 3:
        #         self.label_4.setText('同步成功')
        #         x = '完成'
        #         return x



        shuaxin()
        chushixianshi()

        global ip,name,password,tim
        ip = self.lineEdit.text()
        name = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        try:
          self.lineEdit_4.setText(self.lineEdit_4.text())
        except:
          self.lineEdit_4.setText('0')
        if self.lineEdit_4.text() == '':
           tim = 0
        else:
           tim = int(self.lineEdit_4.text())

        self.radioButton.toggled.connect(fuwuqi1shuaxin)
        self.radioButton_2.toggled.connect(fuwuqi2shuaxin)
        self.radioButton_3.toggled.connect(fuwuqi3shuaxin)

        self.radioButton.toggled.connect(gengxin)
        self.radioButton_2.toggled.connect(gengxin)
        self.radioButton_3.toggled.connect(gengxin)


        self.pushButton.clicked.connect(FTPwork)
        self.pushButton_2.clicked.connect(baocun)

    def retranslateUi(self, Dialog):
        global fuwuqi
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "同步"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.label.setText(_translate("Dialog", "FTP地址"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.label_5.setToolTip(_translate("Dialog", "<html><head/><body><p>单位为秒，服务器时间减去本机时间（北京时间）。</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "服务器延迟"))
        self.radioButton_3.setText(_translate("Dialog", "服务器3"))
        self.radioButton_2.setText(_translate("Dialog", "服务器2"))
        self.radioButton.setText(_translate("Dialog", "服务器1"))
        self.pushButton_2.setText(_translate("Dialog", "保存服务器"))
        self.pushButton.setText(_translate("Dialog", "开始同步"))
        xianzishuzi = QtGui.QIntValidator(-86041,86401)
        self.lineEdit_4.setValidator(xianzishuzi)

class WorkThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(int)
    def __int__(self):
        super(WorkThread,self).__init__()
    def run(self):
            global ip,name,password,tim,y
            import ftputil
            try:
                with ftputil.FTPHost(ip,name,password) as ftp_host:
                     # print(True)
                     # try:
                     #   ftp_host.set_time_shift(tim)
                     # except:
                     #   pass
                     try:
                        ftp_host.mkdir('RPG')
                     except:
                        pass
                     ftp_host.chdir('/RPG')

                     import os
                     if os.path.exists('D:/MyRPG/data.dat'):
                       localmtime = os.stat('D:/MyRPG/data.dat').st_mtime
                       try:
                          ftpmtime = ftp_host.lstat('/RPG/data.dat').st_mtime
                          # ftpmtime1 = ftp_host.lstat('/RPG/data.dat').st_ctime
                          # ftpmtime2 = ftp_host.lstat('/RPG/data.dat').st_mtine
                       except:
                          ftpmtime = 0
                       realftpmtime = ftpmtime - tim
                       # print(localmtime)
                       # print(realftpmtime)
                       info = os.stat('D:/MyRPG/data.dat').st_size

                       if info == 165 or info == 300 or localmtime < realftpmtime:
                         ftp_host.download('/RPG/data.dat','D:/MyRPG/data.dat')
                         ftp_host.download('/RPG/fuwuqi.dat','D:/MyRPG/fuwuqi.dat')
                         ftp_host.download('/RPG/fanqie.dat','D:/MyRPG/fanqie.dat')
                         y = 3
                         self.trigger.emit(3)
                         return
                       else:
                            ftp_host.upload('D:/MyRPG/data.dat','/RPG/data.dat')
                            ftp_host.upload('D:/MyRPG/fuwuqi.dat','/RPG/fuwuqi.dat')
                            ftp_host.upload('D:/MyRPG/fanqie.dat','/RPG/fanqie.dat')
                            y = 3
                            self.trigger.emit(3)
                            return

                            if False:
                               Dialog.close()
                     else:
                       try:
                         ftp_host.download('/RPG/data.dat','D:/MyRPG/data.dat')
                         ftp_host.download('/RPG/fuwuqi.dat','D:/MyRPG/fuwuqi.dat')
                         ftp_host.download('/RPG/fanqie.dat','D:/MyRPG/fanqie.dat')
                         y = 3
                         self.trigger.emit(3)
                         return
                       except:
                         y = 2
                         self.trigger.emit(2)
            except:
                y = 2
                self.trigger.emit(2)
#
# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())
