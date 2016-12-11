# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog11_wanchengrenwu.ui'
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
        Dialog.resize(520, 352)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 4)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        def renwuxianshi():
            import pickle
            path = open('D:/MyRPG/data.dat','rb')
            global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
            dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
            path.close()
            del path
            # print(renwu[0],dianshu)
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
            self.listWidget.clear()
            time = str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)
            ji = datetime.date.today().weekday()
            xingqi = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']

            ###装载表头，今天日期星期，12号粗体，如果没有任务显示（没有任务）
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setBold(True)
            font.setPointSize(12)
            item.setFont(font)
            self.listWidget.addItem(item)
            a = str(time)+'  '+xingqi[ji]+'今日任务：（没有任务）'
            b = str(time)+'  '+xingqi[ji]+'  '+'今日任务：'
            item1 = QtWidgets.QLabel(self.listWidget)
            item1.setFont(font)
            if jinrirenwu == []:
                item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+a+"</span></p></body></html>")
            else :
                item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+b+"</span></p></body></html>")
            self.listWidget.setItemWidget(item,item1)


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
                    self.listWidget.addItem(item)
                def shengchengshenghuo():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('生活：')
                    self.listWidget.addItem(item)
                def shengchenglicai():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('理财：')
                    self.listWidget.addItem(item)
                def shengchengsuoshi():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('琐事：')
                    self.listWidget.addItem(item)
                def shengchengtisheng():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('自我提升：')
                    self.listWidget.addItem(item)
                def shengchengqita():
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setText('其他：')
                    self.listWidget.addItem(item)
                ##每个子项目装载
                def zixiangmuzhuangzai(i):
                        global count5
                        item = QtWidgets.QListWidgetItem()
                        item.setCheckState(0)
                        value = ' ('+str(count5)+') '+i[2]+'：'+i[5]
                        self.listWidget.addItem(item)
                        item.setWhatsThis(i[15])
                        item.setText(value)
                        count5 += 1
                        # length = len(value)
                        # utf8_length = len(value.encode('utf-8'))
                        # length = (utf8_length - length)/2 + length
                        # font = QtGui.QFont()
                        # font.setPointSize(int(length/69+1)*12)
                        # item.setFont(font)
                        # item1 = QtWidgets.QLabel(self.listWidget)
                        # item1.setToolTip(i[1])
                        # item1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
                        # item1.setWordWrap(True)
                        # self.listWidget.setItemWidget(item,item1)


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

                ### 装载以往项目
                if yiqianrenwu == []:
                    pass
                else:
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(12)
                    item.setFont(font)
                    self.listWidget.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget)
                    item1 .setFont(font)
                    item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+'以前没有完成的任务（经验和娱乐点奖励减半）：'+"</span></p></body></html>")
                    self.listWidget.setItemWidget(item,item1)
                    zhuangzaixiaoxiangmu(zuorigongzuo,zuorishenghuo,zuorilicai,zuorisuoshi,zuoritisheng,zuoriqita)

                ### 装载明日项目
                if mingrirenwu == []:
                    pass
                else:
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setBold(True)
                    font.setPointSize(12)
                    item.setFont(font)
                    self.listWidget.addItem(item)
                    item1 = QtWidgets.QLabel(self.listWidget)
                    item1 .setFont(font)
                    item1.setText("<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">"+'明天及以后的任务：'+"</span></p></body></html>")
                    self.listWidget.setItemWidget(item,item1)
                    zhuangzaixiaoxiangmu(mingrigongzuo,mingrishenghuo,mingrilicai,mingrisuoshi,mingritisheng,mingriqita)



            kaishizhuangzai()
        renwuxianshi()

        def wanchengrenwu():
            global add ##用于增量显示的，可以使用listwidget.insert方法
            global dianshu,renwu,renwufinish
            for i in range(self.listWidget.count()):
                if self.listWidget.item(i).checkState() == 2:
                    for k in renwu:
                        if self.listWidget.item(i).whatsThis() == k[15]:
                            import datetime
                            daynow = datetime.date.today().year*365+datetime.date.today().month*30+datetime.date.today().day
                            renwu.remove(k)
                            s = [k[1],k[2],k[3],k[4],k[5],k[6],'完成时间：'+str(datetime.date.today().year)+'-'+str(datetime.date.today().month)+'-'+str(datetime.date.today().day)+' '+str(datetime.datetime.today().hour)+':'+str(datetime.datetime.today().minute)]
                            renwufinish.insert(0,s)
                            add.insert(0,s)
                            ###写整个数值计算过程，特别是当日期为以前的时候，经验和任务点数值减半，废弃任务重写吧。不然麻烦

                            dianshu['d1'] = round(dianshu['d1']+k[7],3)
                            dianshu['d2'] = round(dianshu['d2']+k[8],3)
                            dianshu['d3'] = round(dianshu['d3']+k[9],3)
                            dianshu['d4'] = round(dianshu['d4']+k[10],3)
                            dianshu['d5'] = round(dianshu['d5']+k[11],3)
                            dianshu['d6'] = round(dianshu['d6']+k[12],3)
                            if k[0] < daynow:
                                dianshu['d7'] = dianshu['d7']+int(k[13]/2)
                                dianshu['d8'] = dianshu['d8']+int(k[14]/2)
                            else:
                                dianshu['d7'] = dianshu['d7']+k[13]
                                dianshu['d8'] = dianshu['d8']+k[14]
                        else: continue
                else: continue
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            # print(renwufinish)
            Dialog.destroy()



        ####  废弃任务，前面和完成任务一样，只是不需要加点，但是需要给出一个确定窗口
        def feiqirenwu1():
            import dialog11fujia_jinggao
            Dialog = QtWidgets.QDialog()
            ui = dialog11fujia_jinggao.Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            ui.pushButton.clicked.connect(feiqirenwu)

        def feiqirenwu():
            global renwu
            for i in range(self.listWidget.count()):
                if self.listWidget.item(i).checkState() == 2:
                    for k in renwu:
                        if self.listWidget.item(i).whatsThis() == k[15]:
                            renwu.remove(k)
                        else: continue
                else: continue
            import pickle
            path = open('D:/MyRPG/data.dat','wb')
            pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
            path.close()
            del path
            Dialog.accept()
            Dialog.destroy()

        def tuichu():
            Dialog.destroy()

        self.pushButton.clicked.connect(wanchengrenwu)
        self.pushButton_2.clicked.connect(feiqirenwu1)
        self.pushButton_3.clicked.connect(tuichu)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "完成任务"))
        self.label.setText(_translate("Dialog", "所有任务列表"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.pushButton_2.setText(_translate("Dialog", "废弃任务"))
        self.pushButton.setText(_translate("Dialog", "完成任务"))

# import sys
# app = QtWidgets.QApplication(sys.argv)
# Dialog = QtWidgets.QDialog()
# ui = Ui_Dialog()
# ui.setupUi(Dialog)
# Dialog.show()
# sys.exit(app.exec_())