# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog21_zuoxianpai.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 354)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 295))
        self.textEdit.setObjectName("textEdit")


        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_day = QtWidgets.QLabel(Dialog)
        self.label_day.setText("<span style=\" color:#919191;\">"+'（请选择）'"</span>")
        self.gridLayout.addWidget(self.label_day, 0, 1, 1, 1)

        self.riqi = QtWidgets.QDateEdit()
        import datetime
        nian = datetime.date.today().year
        yue = datetime.date.today().month
        ri = datetime.date.today().day
        self.riqi.setDate(QtCore.QDate(nian,yue,ri))



        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.label.hide()



        #### 初始化变量，如果没有任何作息安排，补充平时和周末的安排
        import pickle
        path = open('D:/MyRPG/data.dat','rb')
        global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
        dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
        path.close()
        del path
        wenben = '7:30：起床'+'\n'+'7:30―8:00：在早饭之前刷牙'+'\n'+'8:00―8:30：吃早饭'+'\n'+'8:30―9:00：避免运动'+'\n'+'9:30：开始一天中最困难的工作'+'\n'+'10:30：让眼睛离开屏幕休息一下'+'\n'+'11:00：吃点水果'+'\n'+'13:00：在面包上加一些豆类蔬菜'+'\n'+'13:00―13:30：午休一小会儿'+'\n'+'13:30―17:00：下午工作'+'\n'+'17:00―19:00：锻炼身体'+'\n'+'19:30：晚餐少吃点'+'\n'+'21:45：看会电视'+'\n'+'23:00：洗个热水澡'+'\n'+'23:30：上床睡觉'
        keys = ['d1','d2','d3','d4','d5','d6','d7','d7','d8','平时','周六','周日']
        if '平时' in dianshu.keys():
            pass
        else:
            dianshu['平时'] = wenben
            dianshu['周六'] = wenben
            dianshu['周日'] = wenben

        #### 装载所有的作息安排内容到界面中
        def zhuangzai():

            global n
            createVar = locals()
            n = 0

            ##然后装载具体内容到右边栏
            def zhuangzaiyoubian(i):
                global f

                if self.radioButtonP.isChecked():
                    self.label_day.setText('平时')
                    self.textEdit.setText(dianshu['平时'])
                    self.pushButton_3.setDisabled(True)
                    return

                if self.radioButtonZ1.isChecked():
                    self.label_day.setText('周六')
                    self.textEdit.setText(dianshu['周六'])
                    self.pushButton_3.setDisabled(True)
                    return

                if self.radioButtonZ2.isChecked():
                    self.label_day.setText('周日')
                    self.textEdit.setText(dianshu['周日'])
                    self.pushButton_3.setDisabled(True)
                    return

                if i != 'a' or  i != 'b':
                    self.label_day.setEnabled(True)
                    self.pushButton_3.setEnabled(True)
                    self.label_day.setText(i)
                    f = i
                    try:
                        self.textEdit.setText(str(dianshu[i]))
                    except:
                        return
                    return
                else:
                    return


            ## 首先装载平时和周末
            self.radioButtonP = QtWidgets.QRadioButton(Dialog)
            self.radioButtonP.setText('平时')
            self.gridLayout.addWidget(self.radioButtonP, 0, 0, 1, 1)
            self.radioButtonZ1 = QtWidgets.QRadioButton(Dialog)
            self.radioButtonZ1.setText('周六')
            self.gridLayout.addWidget(self.radioButtonZ1, 1, 0, 1, 1)
            self.radioButtonZ2 = QtWidgets.QRadioButton(Dialog)
            self.radioButtonZ2.setText('周日')
            self.gridLayout.addWidget(self.radioButtonZ2, 2, 0, 1, 1)

            for i in sorted(dianshu.keys()):
                if i in keys:
                    pass
                else:
                    createVar['radioButton'+str(n)] = QtWidgets.QRadioButton(Dialog)
                    createVar['radioButton'+str(n)].setText(i)
                    self.gridLayout.addWidget(createVar['radioButton'+str(n)], n+3, 0, 1, 1)
                    n += 1


            self.gridLayout.addWidget(self.textEdit, 1, 1, n+1, 3)
            self.gridLayout.addWidget(self.riqi,n+2, 1, 1, 1)
            self.gridLayout.addWidget(self.pushButton, n+3, 1, 1, 1)
            self.gridLayout.addWidget(self.pushButton_2, n+3, 3, 1, 1)
            self.gridLayout.addWidget(self.pushButton_3, n+3, 2, 1, 1)




            self.radioButtonP.toggled.connect(lambda:zhuangzaiyoubian('a'))
            self.radioButtonZ1.toggled.connect(lambda:zhuangzaiyoubian('b'))
            self.radioButtonZ2.toggled.connect(lambda:zhuangzaiyoubian('c'))

            try:
                createVar['radioButton'+str(0)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(0)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(1)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(1)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(2)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(2)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(3)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(3)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(4)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(4)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(5)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(5)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(6)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(6)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(7)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(7)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(8)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(8)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(9)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(9)].text()))
            except:
                pass
            try:
                createVar['radioButton'+str(10)].toggled.connect(lambda:zhuangzaiyoubian(createVar['radioButton'+str(10)].text()))
            except:
                pass


        zhuangzai()

        ### 增加条目
        def zengjia():
            global f
            if len(dianshu)>21:
                f = 0
                self.label_day.setText("<span style=\" color:#919191;\">"+'（请选择）'"</span>")
                zhuangzai()
                self.textEdit.setText("<span style=\" font-size:12pt;font-weight:bold;color:#FF0000;\">"+'除平时和周末外，只允许建立11条额外作息安排，请删除不需要的条目后再增加条目！'+"</span>")
                return
            if self.riqi.text() in dianshu.keys():
                return
            else:
                f = 0
                self.label_day.setText("<span style=\" color:#919191;\">"+'（请选择）'"</span>")
                self.textEdit.setText('')
                a = Dialog.findChildren(QtWidgets.QRadioButton)
                for i in a:
                    i.hide()
                dianshu[self.riqi.text()] = wenben
                # print(dianshu.keys())
                zhuangzai()

        ###删除条目
        def shanchu():
            global f
            try:
                del dianshu[f]
                self.label_day.setText("<span style=\" color:#919191;\">"+'（请选择）'"</span>")
                self.textEdit.setText('')
            except:
                pass
            a = Dialog.findChildren(QtWidgets.QRadioButton)
            for i in a:
                i.hide()
            zhuangzai()

        ###条目更新
        def gengxin():
            a = self.label_day.text()
            if len(a)< 11:
                try:
                    dianshu[a] = self.textEdit.toPlainText()
                except:
                    pass
            else:
                pass

        def queding():
            import pickle
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.close()


        self.textEdit.textChanged.connect(gengxin)
        self.pushButton.clicked.connect(zengjia)
        self.pushButton_3.clicked.connect(shanchu)
        self.pushButton_2.clicked.connect(queding)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "编辑作息时间"))
        self.pushButton.setText(_translate("Dialog", "增加"))
        self.pushButton_3.setText(_translate("Dialog", "删除"))
        self.pushButton_2.setText(_translate("Dialog", "确定"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_2.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_3.setText(_translate("Dialog", "RadioButton"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#8a8a8a;\">注意时间格式为:20**-**-**(个位数不加0)</span></p></body></html>"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())