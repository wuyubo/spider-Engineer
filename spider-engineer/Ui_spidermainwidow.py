 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python\spiderengineer - （2）\spidermainwidow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from source import source
from ui_paint import Window

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 670)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_bigin = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_bigin.setGeometry(QtCore.QRect(80, 110, 141, 51))
        self.pushButton_bigin.setStyleSheet("font: 75 20pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.pushButton_bigin.setObjectName("pushButton_bigin")
        self.pushButton_show = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_show.setGeometry(QtCore.QRect(80, 220, 141, 51))
        self.pushButton_show.setStyleSheet("font: 75 20pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.pushButton_show.setObjectName("pushButton_show")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 170, 231, 41))
        self.comboBox.setStyleSheet("border-color: rgb(0, 255, 255);\n"
"\n"
"font: 75 14pt \"黑体\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_show = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_show.setGeometry(QtCore.QRect(260, 0, 1300, 670))
        self.groupBox_show.setStyleSheet("font: 75 18pt \"楷体\";\n"
"border-color: rgb(0, 170, 255);")
        self.groupBox_show.setObjectName("groupBox_show")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_show)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 290, 281, 361))
        self.groupBox.setStyleSheet("font: 75 18pt \"楷体\";\n"
"border-color: rgb(255, 170, 0);")
        self.groupBox.setObjectName("groupBox")
        self.textEdit_get = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_get.setGeometry(QtCore.QRect(20, 40, 241, 301))
        self.textEdit_get.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_get.setObjectName("textEdit_get")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 60, 231, 41))
        self.comboBox_2.setStyleSheet("border-color: rgb(0, 255, 255);\n"
"\n"
"font: 75 14pt \"黑体\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 31))
        self.label.setStyleSheet("font: 75 14pt \"楷体\";")
        self.label.setObjectName("label")
        self.label_getstatus = QtWidgets.QLabel(self.centralWidget)
        self.label_getstatus.setGeometry(QtCore.QRect(90, 20, 171, 31))
        self.label_getstatus.setObjectName("label_getstatus")
        self.frame_ay = QtWidgets.QFrame(self.centralWidget)
        self.frame_ay.setGeometry(QtCore.QRect(-1, 0, 1301, 670))
        self.frame_ay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ay.setObjectName("frame_ay")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_ay)
        self.pushButton_back.setGeometry(QtCore.QRect(1180, 20, 91, 41))
        self.pushButton_back.setStyleSheet("font: 75 20pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_ay)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 131, 41))
        self.pushButton_2.setStyleSheet("font: 75 20pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_ay)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 131, 41))
        self.pushButton_3.setStyleSheet("font: 75 20pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        #self.pushButton_4 = QtWidgets.QPushButton(self.frame_ay)
       # self.pushButton_4.setGeometry(QtCore.QRect(10, 150, 131, 41))
        #self.pushButton_4.setStyleSheet("font: 75 20pt \"楷体\";\n"
#"background-color: rgb(0, 170, 255);")
        #self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_bigin.raise_()
        self.pushButton_show.raise_()
        self.comboBox.raise_()
        self.groupBox_show.raise_()
        self.groupBox.raise_()
        self.comboBox_2.raise_()
        self.label.raise_()
        self.label_getstatus.raise_()
        self.pushButton.raise_()
        self.frame_ay.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_bigin.clicked.connect(MainWindow.bigin_click)
        self.pushButton_show.clicked.connect(MainWindow.show_click)
        self.pushButton_back.clicked.connect(MainWindow.ui_reshow)
        self.pushButton.clicked.connect(MainWindow.deep_ay)
        self.pushButton_2.clicked.connect(MainWindow.duibi_hx)
        self.pushButton_3.clicked.connect(MainWindow.duibi_zx)
        #self.pushButton_4.clicked.connect(MainWindow.duibi_nl)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "软件工程师—网络爬虫分析"))
        self.pushButton_bigin.setText(_translate("MainWindow", "抓取数据"))
        self.pushButton_show.setText(_translate("MainWindow", "分析"))
        self.comboBox.setItemText(0, _translate("MainWindow", "请选择要分析的工程师"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1.嵌入式软件工程师"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2.JAVA软件工程师"))
        self.comboBox.setItemText(3, _translate("MainWindow", "3.WEB软件工程师"))
        self.comboBox.setItemText(4, _translate("MainWindow", "4.IOS软件工程师"))
        self.comboBox.setItemText(5, _translate("MainWindow", "5..Net软件工程师"))
        self.comboBox.setItemText(6, _translate("MainWindow", "6.C#软件工程师"))
        self.comboBox.setItemText(7, _translate("MainWindow", "7.PHP软件工程师"))
        self.comboBox.setItemText(8, _translate("MainWindow", "8.Android开发工程师"))
        self.comboBox.setItemText(9, _translate("MainWindow", "9.C++软件工程师"))
        self.groupBox_show.setTitle(_translate("MainWindow", "图示分析"))
        self.pushButton.setText(_translate("MainWindow", "深度分析"))
        self.groupBox.setTitle(_translate("MainWindow", "结果分析"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "请选择要抓取的网站"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "58同城"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "中华英才网"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "智联招聘"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "猎聘猎头网"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "卓博人才网"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "前程无忧（待优化中）"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">状态：</span></p></body></html>"))
        self.label_getstatus.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#00007f;\">待抓取</span></p></body></html>"))
        self.pushButton_back.setText(_translate("MainWindow", "返回"))
        self.pushButton_2.setText(_translate("MainWindow", "横向对比"))
        self.pushButton_3.setText(_translate("MainWindow", "纵向对比"))
        #self.pushButton_4.setText(_translate("MainWindow", "技能分析"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =Window() #QtWidgets.QMainWindow()
    source.ui = Ui_MainWindow()
    source.ui.setupUi(MainWindow)
    source.ui.frame_ay.close()
    MainWindow.show()
    sys.exit(app.exec_())

