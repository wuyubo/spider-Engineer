import threading
import time
from DataBase import database
from source import source
from threadings import Tnuls
from threads import qthreadt

import threading
import crawler
    ustr=""
    strl=""
    nustr=""
    bool=True
    urllist=""
  def bigin_click(self):
      #  starttime=time.time(); #记录开始时间
        if self.bool==True:
            threads = [] #创建一个线程列表，用于存放需要执行的子线程
            t1 = threading.Thread(target=self.threadcl) #创建第一个子线程，子线程的任务是调用task1函数，注意函数名后不能
            threads.append(t1)#将这个子线程添加到线程列表中
            t1.setDaemon(True)
            t1.start()
        self.bool=False
      #  for t in threads: #遍历线程列表
       #     t.setDaemon(True) #将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
        #    t.start() #启动子线程
    def show_click(self):
        self.strl=self.comboBox.currentText()
        self.textEdit_get.setText(self.strl)
        self.textEdit_getstr.setText(self.ustr)
        
    def crawling(self, url):
        cl=crawler.crawler()
        cl.gethtml(url)
        self.urllist=cl.geturllist()
        nexturllist=cl.getnexturl()
        self.getnexturl(nexturllist, cl)
        for i in range(len(self.urllist)):
            ul=self.urllist[i]
            self.ustr=self.ustr+str(i)+"、"+ul[1]+"  :"+ul[0]+"\n\n"
        #for ur in self.urllist:
           # cl.gethtml(ur[0])
            #sl=cl.getstrlist()
           # self.strl=self.strl+sl
            

    def getnexturl(self, nexturllist, cl):
        for i in range(len(nexturllist)):
            nul=nexturllist[i]
            self.nustr=self.nustr+nul[1]+nul[0]+"\n"
            cl.gethtml("http://gz.58.com"+nul[0])
            uls=cl.geturllist()
            if cl.isend():
                if i==(len(nexturllist)-1):
                    cl.gethtml("http://gz.58.com"+nul[0])
                    nus=cl.getnexturl()
                    del nus[0:(i+1)]
                    self.getnexturl(nus, cl)
            self.urllist=self.urllist+uls
    def threadcl(self):
        url="http://gz.58.com/tech/?key=java%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&cmcskey=java%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&final=1&jump=2&specialtype=gls&canclequery=isbiz%3D0&sourcetype=4"
        self.crawling(url)
    '''#时针
        transform.translate(50,50)
        transform.rotate(hour_angle)
        transform.translate(-50,-50)
        painter.setWorldTransform(transform)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.darkRed))
        painter.drawPolygon(QPolygonF(hourPoints))
         
        transform.reset()
         
        #分针
        transform.translate(50,50)
        transform.rotate(minite_angle)
        transform.translate(-50,-50)
        painter.setWorldTransform(transform)
        painter.setBrush(QBrush(Qt.darkGreen))
        painter.drawPolygon(QPolygonF(minPoints))
       
        transform.reset()
        
        #秒针
        transform.translate(50,50)
        transform.rotate(-53)#second_angle
        transform.translate(-50,-50)
        painter.setWorldTransform(transform)
        painter.setPen(QPen(Qt.darkCyan,1))
        painter.drawLine(50,50,90,20) 
        ''' 
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
    def initUI(self): 
        self.setGeometry(100, 35, 1200, 670)
    def paintEvent(self,event):
        source.ui.groupBox_show.close()
        pt=QPainter(self)
        pt.begin(self)
        #self.drawRect(pt)
        self.drawclock(pt)
        pt.end()
    def drawRect(self, pt):
        pen1=QPen(QColor(225, 225, 225, 225))
        rec=QRect(500, 500,500, 500)
        pt.setPen(pen1)
        pt.drawRect(rec)
        pt.setBrush(QColor(0, 0, 0, 255))
        pt.drawRect(300, 300, 300, 600)
    def drawclock(self, painter):
        painter.setRenderHint(QPainter.Antialiasing)
         
        #设置表盘中的文字字体
        font=QFont("Times",6)
        fm=QFontMetrics(font)
        fontRect=fm.boundingRect("99")#获取绘制字体的矩形范围
         
        #分针坐标点
        minPoints=[QPointF(50,25),
                   QPointF(48,50),
                   QPointF(52,50)]
         
        #时钟坐标点
        hourPoints=[QPointF(50,35),
                   QPointF(48,50),
                   QPointF(52,50)]
         
        side=min(self.width(),self.height())
        painter.setViewport((2*self.width())/5,self.height()/16,
                            (4*side)/7, (4*side)/7)#始终处于窗口中心位置显示
         
         
        #设置QPainter的坐标系统，无论窗体大小如何变化，
        #窗体左上坐标为(0,0),右下坐标为(100,100),
        #因此窗体中心坐标为(50,50)
        painter.setWindow(0,0,100,100)
         
        #绘制表盘，使用环形渐变色
        niceBlue=QColor(150,150,200)
        haloGrident=QRadialGradient(50,50,50,50,50)
        haloGrident.setColorAt(0.0,Qt.lightGray)
        haloGrident.setColorAt(0.5,Qt.darkGray)
        haloGrident.setColorAt(0.9,Qt.white)
        haloGrident.setColorAt(1.0,niceBlue)
        painter.setBrush(haloGrident)
        painter.setPen(QPen(Qt.darkGray,1))
        painter.drawEllipse(0,0,100,100)
         
         
        transform=QTransform()
         
        #绘制时钟为0的字，以及刻度
        painter.setPen(QPen(Qt.black,1.5))
        fontRect.moveCenter(QPoint(50,10+fontRect.height()/2))
        painter.setFont(font)
        painter.drawLine(50,2,50,8)#
        painter.drawText(QRectF(fontRect),Qt.AlignHCenter|Qt.AlignTop,"0")
         
        for i in range(1,12):
            transform.translate(50, 50)
            transform.rotate(30)
            transform.translate(-50,-50)
            painter.setWorldTransform(transform)
            painter.drawLine(50,2,50,8)
            painter.drawText(QRectF(fontRect),Qt.AlignHCenter|Qt.AlignTop,"%d" % i)
         
        transform.reset()
         
        #绘制分钟刻度线
        painter.setPen(QPen(Qt.blue,1))
        for i in range(1,60): 
            transform.translate(50,50)
            transform.rotate(6)
            transform.translate(-50,-50)
            if i%5!=0:
                painter.setWorldTransform(transform)
                painter.drawLine(50,2,50,5)
                 
                 
        transform.reset()
         
        #获取当前时间
        currentTime=QTime().currentTime()
        #hour=currentTime.hour() if currentTime.hour()<12 else currentTime.hour()-12
        #minite=currentTime.minute()
        second=currentTime.second()
         
        #获取所需旋转角度
        #hour_angle=hour*30.0+(minite/60.0)*30.0
        #minite_angle=(minite/60.0)*360.0
        second_angle=second*6.0-53
        source.ui.textEdit_get.setText(str(second))
        self.draw_line(painter, transform, second_angle)
        self.draw_line(painter, transform)
        
    def draw_line(self, painter, transform, angle=-53):
         #秒针
        transform.reset()
        transform.translate(50,50)
        transform.rotate(angle)#second_angle
        transform.translate(-50,-50)
        painter.setWorldTransform(transform)
        painter.setPen(QPen(Qt.darkCyan,1))
        painter.drawLine(50,50,90,20)   
     def drawRect(self, pt):
        pen1=QPen(QColor(225, 225, 225, 225))
        rec=QRect(500, 500,500, 500)
        pt.setPen(pen1)
        pt.drawRect(rec)
        pt.setBrush(QColor(0, 0, 0, 255))
        pt.drawRect(300, 300, 300, 600)
        
 #**********************************************************************8 
from PyQt5 import QtCore, QtGui, QtWidgets
from source import source
from threadings import Tnuls
import threading 
import time
from ui_paint import Window


    def bigin_click(self):
        if not source.isbigan:
            if self.comboBox_2.currentText ()=="58同城":
                t=Tnuls(0)
                t.start()
                source.isbigan=True
            if  self.comboBox_2.currentText ()=="中华英才网":
                t=Tnuls(1)
                t.start()
                source.isbigan=True
            if  self.comboBox_2.currentText ()=="智联招聘":
                t=Tnuls(2)
                t.start()
                source.isbigan=True
            if  self.comboBox_2.currentText ()=="猎聘猎头网":
                t=Tnuls(3)
                t.start()
                source.isbigan=True
            if  self.comboBox_2.currentText ()=="卓博人才网":
                t=Tnuls(4)
                t.start()
                source.isbigan=True
            if  self.comboBox_2.currentText ()=="前程无忧":
                t=Tnuls(5)
                t.start()
                source.isbigan=True
        
        if  source.isbigan:
            t1 = threading.Thread(target=self.threadcl) #创建第一个子线程，子线程的任务
            t1.setDaemon(True)
            t1.start()
        MainWindow.update()
        
    def show_click(self):
        MainWindow.getdata()
        MainWindow.setUpdatesEnabled(False);
        MainWindow.setUpdatesEnabled(True);
        MainWindow.repaint();
        if len(MainWindow.bestlist)>0:
            bestlist=MainWindow.bestlist
            antext=source.Eanalyze[self.comboBox.currentText ()]
            analyze_text=""
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            self.textEdit_get.setText(analyze_text)
    def threadcl(self):
        #database.open()#打开数据库
        source.open_txt()
        '''
        for i in range(1, 2):#len(source.urllist)
            t=Tnuls(i)
            t.start()
            time.sleep(0.5)
            while source.threadnum>800:
                time.sleep(0.3)
        '''
        while source.isbigan:
            time.sleep(1)
            if source.threadnum<1:
                source.isgetweb=True
                source.isbigan=False
       # database.close()#关闭数据库
        source.close_txt()
        source.copy_txt()
        #------------------------------------------------------------------------------------------
        self.pushButton_bigin.clicked.connect(MainWindow.bigin_click)
        self.pushButton_show.clicked.connect(MainWindow.show_click)
        self.pushButton_back.clicked.connect(MainWindow.ui_reshow)
        self.pushButton.clicked.connect(MainWindow.deep_ay)
        self.pushButton_2.clicked.connect(MainWindow.duibi_hx)
        self.pushButton_3.clicked.connect(MainWindow.duibi_zx)
        self.pushButton_4.clicked.connect(MainWindow.duibi_nl)
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =Window() #QtWidgets.QMainWindow()
    source.ui = Ui_MainWindow()
    source.ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
