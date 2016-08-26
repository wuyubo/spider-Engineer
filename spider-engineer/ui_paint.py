from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from source import source
from analyze import analyze
import math
import time
from threadings import Tnuls
import threading 

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        self.ename=""
        self.aly=analyze()
        self.classlist=[]
        self.count=0
        self.datasum=0
        self.scalelist=[]
        self.doing=0
        self.bestlist=[]
        self.catch_time=0
        self.second=0
        self.isdeep_ay=False
        self.all_result={}
        self.all_rscale={}
        self.zu_name=[]
        self.zu_namel=[]
        self.ze_Ewage={}
        self.deep_state=0
        self.colors=[Qt.red, QColor(100, 10, 50, 255), Qt.green, Qt.yellow,Qt.gray,QColor(100, 100, 0, 255),QColor(100, 10, 20, 255),QColor(0, 100, 40, 255) ,QColor(0, 30, 140, 255)  , Qt.yellow, Qt.green, Qt.black, Qt.blue, Qt.red]
    def initUI(self): 
        self.setGeometry(35, 35, 1300, 670)
    def paintEvent(self,event):
        pt=QPainter(self)
        pt.begin(self)
        side=min(self.width(),self.height())
        #获取当前时间
        currentTime=QTime().currentTime()
        currentsecond=currentTime.second()
        w=(5*side)/13
        x=475/871*source.ui.groupBox_show.width()
        y=65/631*source.ui.groupBox_show.height()
        ax=102/871*source.ui.groupBox_show.width()
        ay=40/631*source.ui.groupBox_show.height()
           # if len(self.bestlist)>0:
        self.drawRect(pt,self.width(), self.height(), QColor(10, 40, 50, 255))#------------
       
        if not self.isdeep_ay:
            self.show_bestlist(pt,self.bestlist, x-200, y+100, w-40, w+300)
            for i in range(4):#len(self.classlist)
                #self.drawclock(pt, x, y, w, w, i)
                if i==0 and len(self.classlist)>0:
                    self.drawclock(pt, x-20, y, w, w, 0)
                if i==1 and len(self.classlist)>1:
                    self.drawclock(pt, x+w+ax, y, w, w, 1)
                if i==2 and len(self.classlist)>2:
                    self.drawclock(pt, x-20, y+w+ay, w, w, 2)
                if i==3 and len(self.classlist)>3:
                    self.drawclock(pt, x+w+ax, y+w+ay, w, w, 3)
        else:
            if self.deep_state==1:
                self.draw_pillar(pt,self.zu_name, self.all_rscale, self.zu_namel)
            if self.deep_state==2:
                self.draw_brline(pt,self.zu_name, self.all_result, self.zu_namel)
        pt.end()
        
        if  source.isbigan:
            if self.second==59:
                self.second=0
            if self.second<currentsecond:
                self.catch_time=self.catch_time+1
                self.second=currentsecond
            text="数据抓取中."+str(self.catch_time)
            self.doing=self.doing+1
            if self.doing%2==0:
                text=text+"."
            #if self.doing==20:
               # text="数据抓取中."
              #  self.doing=0
            source.ui.label_getstatus.setText(text)
        else :
            if source.isgetweb:
                source.ui.label_getstatus.setText("抓取完成")
            else :
                source.ui.label_getstatus.setText("待抓取")
        self.ui_autolocation()#
     
    def drawclock(self, painter, x, y, w, h, num=0):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setViewport(x,y,w,h)
        #设置QPainter的坐标系统，无论窗体大小如何变化，
        #窗体左上坐标为(0,0),右下坐标为(100,100),
        #因此窗体中心坐标为(50,50)
        painter.setWindow(0,0,100,100)
         
        #绘制
        niceBlue=QColor(200,150,100)
        haloGrident=QRadialGradient(50,50,50,50,50)
        #haloGrident.setColorAt(0.5,Qt.lightGray)
        #haloGrident.setColorAt(0.5,Qt.darkGray)
        #haloGrident.setColorAt(0.9,Qt.white)
        haloGrident.setColorAt(1.0,niceBlue)
        painter.setBrush(haloGrident)
        painter.setPen(QPen(Qt.darkGray,1))
        painter.drawEllipse(0,0,100,100)
         
         
        transform=QTransform()
        
        #self.draw_text(painter, font, "java", 20, 40)
        
        if not self.ename=="":
            if len(self.classlist)>0:
                self.datasum=len(self.classlist)
                self.count=source.Erealdata[self.ename][0]
                if  num<len(self.classlist):
                    sl=self.aly.getscale(self.classlist[num])
                    self.scalelist=sl
                    self.ui_settext(self.classlist[num][0], num, painter)
                    
                    if not sl==0:
                        i=0
                        hyangle=0
                        angle=0
                        self.draw_line(painter, transform, angle)
                          #设置文字字体
                        font=QFont("Times",5)
                        for s in sl:
                            angle=s*360+angle
                            #self.draw_line(painter, transform, angle)
                            i=i+1
                            if not hyangle==angle:
                                c=source.Eclassfy[self.ename]
                                text=source.Erealdata[self.ename][c[num][i]-1]
                                for a in range(int(hyangle), int(angle)):
                                    self.draw_line(painter, transform, a, self.colors[i-1])
                                scale=str(round(sl[i-1]*100, 2))+"%"
                                location=self.get_textpoint(hyangle,angle)
                                self.draw_text(painter, font,text,location["x"],location["y"], self.colors[i])#source.Erealdata[self.ename][i]
                                
                                location2=self.get_textpoint(hyangle,angle, 30, 0)
                                self.drawLines(painter, location2["x"],location2["y"],location["x"],location["y"]+8, self.colors[i])
                                self.draw_text(painter, font,scale,location["x"],location["y"]+6 , self.colors[i])
                              
                                hyangle=angle
    def draw_line(self, painter, transform, angle=-53, color=Qt.darkCyan):
         #秒针
        transform.reset()
        transform.translate(50,50)
        transform.rotate(angle)#second_angle
        transform.translate(-50,-50)
        painter.setWorldTransform(transform)
        painter.setPen(QPen(color,1))
        painter.drawLine(50,50,90,20)   
        transform.reset()
        painter.setWorldTransform(transform)
    def drawLines(self, qp, x1, y1, x2, y2, color=Qt.black, lw=1):
        if y2 > 70:
            y2=y2-10
            if x2 < 30:
                x2=x2+20
        else:
            if x2< 30:
                x2=x2+20
        pen=QPen(color, lw, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(x1, y1, x2, y2)
    def draw_text(self, painter, font, text, x=0, y=0, color=Qt.white):
        painter.setPen(QPen(color,1.5))
        painter.setFont(font)
        painter.drawText(x, y, text)
    def drawRect(self, pt, w, h, color=QColor(50, 100, 200, 255),  x=0, y=0):
        #pen1=QPen(QColor(225, 0, 225, 225))
        #rec=QRect(500, 500,500, 500)
        #pt.setPen(pen1)
        #pt.drawRect(rec)
        pt.setBrush(color)
        pt.drawRect(x, y, w, h)
    def show_bestlist(self, painter,bestlist,  x=250, y=30, w=100, h=100):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setViewport(x,y,w,h)
        #设置QPainter的坐标系统，无论窗体大小如何变化，
        #窗体左上坐标为(0,0),右下坐标为(100,100),
        #因此窗体中心坐标为(50,50)
        painter.setWindow(0,0,60,200)
        font=QFont("Times",5)
        i=0
        tw=0
        self.draw_text(painter, font,"最佳组合:",0 , tw-8)
        font=QFont("Times",4)
        for text in bestlist:
            tw=tw+5*i
            self.draw_text(painter, font,text,0, tw)
            i=1+1
    def ui_settext(self, text, num, painter):
        font=QFont("Times",6)
        self.draw_text(painter, font,text,0, 0)
    def ui_autolocation(self):
        source.ui.frame_ay.setGeometry(QRect(0, 0, self.width(), self.height()))
        source.ui.pushButton_bigin.setGeometry(QRect(self.width()/15,self.height()*11/67, self.width()*7/60, self.height()*51/670))
        source.ui.pushButton_show.setGeometry(QRect(self.width()/15, self.height()*22/67, self.width()*47/400, self.height()*51/670))
        source.ui.comboBox.setGeometry(QRect(self.width()/40, self.height()*17/67, self.width()*77/400,self.height()*47/670))
        source.ui.pushButton_back.setGeometry(QRect(self.width()*1180/1300, self.height()*20/670, self.width()*91/1300, self.height()*41/670))
        source.ui.groupBox_show.setGeometry(QRect(self.width()*3/13, self.height()*2/70, self.width()*890/1200, self.height()*645/670))
        source.ui.groupBox.setGeometry(QRect(self.width()/60, self.height()*29/67, self.width()*281/1300, self.height()*361/670))
        source.ui.textEdit_get.setGeometry(QRect(self.width()/60, self.height()*4/67, self.width()*241/1300, self.height()*301/670))
        source.ui.comboBox_2.setGeometry(QRect(self.width()/40, self.height()*6/67, self.width()*77/400, self.height()*41/670))
        source.ui.label.setGeometry(QRect(self.width()/40, self.height()*2/67, self.width()*61/1300, self.height()*31/670))
        source.ui.label_getstatus.setGeometry(QRect(self.width()*3/40, self.height()*2/67, self.width()/4, self.height()*31/670))
    def get_textpoint(self, hyangle, angle, length=60, state=1):
        cangle=hyangle+(angle-hyangle)/2
        angleR=self.location(cangle)
        cangle=angleR[1]/360*(2*3.14)
        point={"x":0, "y":0}
        x=math.cos(cangle)*length
        y=math.sin(cangle)*length
        if angleR[0]==90:
            point["x"]=50+25
            point["y"]=50
        if angleR[0]==180:
            point["x"]=50
            point["y"]=50+25
        if angleR[0]==270:
            point["x"]=50-25
            point["y"]=50
        if angleR[0]==360:
            point["x"]=50
            point["y"]=50-25
        if angleR[0]==1:
            point["y"]=50-y
            point["x"]=50+x
        if angleR[0]==2: 
            point["x"]=50+x
            point["y"]=50+y
        if angleR[0]==3:
            point["y"]=50+y
            if state==1:
                point["x"]=35-x
            else:
                point["x"]=50-x
        if angleR[0]==4:
            point["y"]=50-y
            if state==1:
                point["x"]=35-x
            else:
                point["x"]=50-x
        return point
    def location(self, angle):
        angleR=[]
        if angle==40:
            angleR=[90, 0]
        if angle==310:
            angleR=[360, 0]
        if angle==130:
            angleR=[180, 0]
        if angle==220:
            angleR=[270, 0]
        if angle>-50 and angle<40:
            angleR=[1,40-angle]
        if angle>310 and angle<400:
             angleR=[1,400-angle]
        if angle>40 and angle<130:
             angleR=[2,angle-40]
        if angle>130 and angle<220:
             angleR=[3,220-angle]
        if angle>220 and angle <310:
             angleR=[4,angle-220]
        return angleR
    def getdata(self):
        ename=source.ui.comboBox.currentText ()
        if not ename=="请选择要分析的工程师":
            self.ename=ename
            classlist=self.aly.select_all(ename)
            if not classlist=="error" and len(classlist)>0:
                self.classlist=classlist
                self.bestlist=self.aly.getbest(classlist, ename)
            self.count=0
            self.datasum=0
            self.scalelist=[]
 #-----------------------------------------------------------------------------------------#
    def draw_pillar(self, painter, xy_name=["y", "x"], result_list={}, namel=[] , x1=200, y1= 150, x2=200, y2=550, x3=1100, y3=550):
        x1=x1*self.width()/1300
        y1=y1*self.height()/670
        x2=x2*self.width()/1300
        y2=y2*self.height()/670
        x3=x3*self.width()/1300
        y3=y3*self.height()/670
        self.draw_Lines(painter,x1,y1 ,x2 , y2, Qt.black)
        self.draw_Lines(painter, x2, y2,x3 ,y3 , Qt.black)
        font=QFont("Times",12)
        self.draw_text(painter, font,xy_name[0] , x1+5, y1)
        self.draw_text(painter, font, xy_name[1], x3, y3-5)
        xt=1100*self.width()/1300
        yt=90*self.height()/670
        w1=(x3-x2)/(len(namel)+2)
        w=w1*2/3
        xn=x2
        d=20
        i=0
        for name in namel:
            h=result_list[name]*float(y2-y1)*2
            xn=xn+w1
            yn=y2-h
            self.drawRect(painter, w, h,self.colors[i], xn, yn )
            strscal= str("%.2f" % (result_list[name]*100))+"%"
            if name==self.ename:
                strscal=strscal+"***"
            self.draw_text(painter,font,strscal, xn, yn-20)
            i=i+1
            self.draw_text(painter, font, str(i), xn+10, yn+h+d)
            self.draw_text(painter, font, name, xt, yt)
            self.drawRect(painter, 40, 15, self.colors[i-1], xt-50, yt-15)
            yt=yt+30
            if name==self.ename:
                scale=str("%.2f" % (result_list[name]*100)+"%")
        if not self.ename=="":
            rank=self.get_rank(result_list, self.ename, namel)
            text0=self.ename+source.deep_zuay[0]+scale+source.deep_zuay[1]+str(rank)+source.deep_zuay[2]
            self.draw_text(painter,font, text0, x1+100, y1-100)
            if rank<4:
                text1=source.deep_zuay1[0]
            if rank>3 and rank<7:
                text1=source.deep_zuay1[1]
            if rank>6 and rank<10:
                text1=source.deep_zuay1[2]
            self.draw_text(painter,font, text1, x1+80, y1-80)
    def get_rank(self, resultlist, name, namel):
        rank=1
        s0=resultlist[name]
        for n in namel:
            if resultlist[n]>s0:
                rank=rank+1
        return rank
    def draw_Lines(self, qp, x1, y1, x2, y2, color=Qt.black, lw=2):
        pen=QPen(color, lw, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(x1, y1, x2, y2)
        
    def draw_brline(self , painter, xy_name=["y", "x"], result_list={}, namel=[] , x1=200, y1= 80, x2=200, y2=480, x3=1100, y3=480):
        x1=x1*self.width()/1300
        y1=y1*self.height()/670
        x2=x2*self.width()/1300
        y2=y2*self.height()/670
        x3=x3*self.width()/1300
        y3=y3*self.height()/670
        xt=1100*self.width()/1300
        yt=90*self.height()/670
        self.draw_Lines(painter,x1,y1 ,x2 , y2, Qt.black)
        self.draw_Lines(painter, x2, y2,x3 ,y3 , Qt.black)
        font=QFont("Times",12)
        self.draw_text(painter, font,xy_name[0] , x1+5, y1)
        self.draw_text(painter, font, xy_name[1], x3, y3-5)
        #---
        w=(x3-x2)/(len(source.deep_years))
        xn=x2
        
        for year in source.deep_years:
            self.draw_text(painter,font, year,xn-5, y2+20)
            self.draw_Lines(painter, xn,y2-5, xn, y2 , Qt.black)
            xn=xn+w
            
        wg=(source.deep_wages[1])/10
        wage=int(wg)
        wh=(y2-y1-50)/10
        wyh=wh
        self.draw_text(painter,font, "0",x2-50, y2)
        for i in range(10):
            self.draw_text(painter,font, str(int(wage)),x2-50, y2-wyh)
            self.draw_Lines(painter, x1,y2-wyh, x1+5, y2-wyh , Qt.black)
            wage=wage+wg
            wyh=wyh+wh
        i=0
        add=50
        xb=x2-100
        for name in namel:
            xw0=x2
            xw1=x2
            yw0=0
            yw1=0
            result=result_list[name]
            self.draw_Lines(painter, xb-50,y2+50, xb-50, y2+185 , Qt.black)
            self.draw_Lines(painter, xb-30,y2+add+7, xb+40, y2+add+7 , self.colors[i])
            self.draw_Lines(painter, xb+60,y2+50, xb+60, y2+185 , Qt.black)
            lw=2
            if name==self.ename:
                lw=6
            for rwge in result:
                yw1=y2-rwge*(y2-y1-50)/source.deep_wages[1]
                if not xw0==xw1:
                    self.draw_Lines(painter, xw0,yw0, xw1, yw1 , self.colors[i], lw)
                self.draw_Lines(painter, xw1+60,y2+50, xw1+60, y2+185 , Qt.black)
                self.draw_text(painter,font, str(rwge),xw1-10, y2+add+13)
                xw0=xw1
                xw1=xw1+w
                yw0=yw1
                self.draw_Lines(painter, x3,y2+50, x3, y2+185 , Qt.black)
                
            self.draw_Lines(painter, xb-50,y2+add, x3, y2+add , Qt.black)
            add=add+15
       
           #------------------------------------------------------------------------------------- 
            self.draw_text(painter, font, name, xt, yt)
            self.drawRect(painter, 40, 10, self.colors[i], xt-50, yt-15)
            self.draw_Lines(painter, xt-50,yt, xt-10, yt , self.colors[i])
            yt=yt+30
            i=i+1
        self.draw_Lines(painter, xb-50,y2+add, x3, y2+add , Qt.black)
        #----------------------
        self.drawRect(painter, 40, 10, self.colors[0], xt-50, yt+50)
        self.draw_text(painter,font, "平均工资",xt, yt+50)
        self.draw_Lines(painter, xt-50,yt+80, xt-10, yt+80 , self.colors[0])
        self.draw_text(painter,font, "工龄工资",xt, yt+80)
        #self.draw_pillar(painter,self.zu_name, self.ze_Ewage, self.zu_namel, x1, y1, x2, y2, x3, y3)
        if len(self.ze_Ewage)>0:
            w1=(x3-x2)/(len(namel)+2)
            w=w1*2/3
            xn=x2
            d=40
            i=0
            for name in namel:
                h=self.ze_Ewage[name]*(y2-y1-50)/source.deep_wages[1]
                xn=xn+w1
                yn=y2-h
                self.drawRect(painter, w, h,self.colors[i], xn, yn )
                tw=str(self.ze_Ewage[name])
                i=i+1
                ti=str(i)
                if name==self.ename:
                    tw=tw+"***"
                    ti=ti+"***"
                self.draw_text(painter,font,tw , xn, yn-20)
                self.draw_text(painter, font, ti, xn+10, yn+h+d)
 #-----------------------------------------------------------------------------------------#
    def ui_clear(self):
        source.ui.pushButton_bigin.close()
        source.ui.pushButton_show.close()
        source.ui.comboBox.close()
        source.ui.groupBox_show.close()
        source.ui.groupBox.close()
        source.ui.textEdit_get.close()
        source.ui.comboBox_2.close()
        source.ui.label.close()
        source.ui.label_getstatus.close()
    def ui_reshow(self):
        source.ui.frame_ay.close()
        source.ui.pushButton_bigin.show()
        source.ui.pushButton_show.show()
        source.ui.comboBox.show()
        source.ui.groupBox_show.show()
        source.ui.groupBox.show()
        source.ui.textEdit_get.show()
        source.ui.comboBox_2.show()
        source.ui.label.show()
        source.ui.label_getstatus.show()
        self.isdeep_ay=False
 #-----------------------------------------------------------------------------------------#
    def deep_ay(self):
        self.ui_clear()
        source.ui.frame_ay.show()
        self.isdeep_ay=True
        if self.deep_state==0:
            self.hengxiang()
    def hengxiang(self):
        self.all_result=self.aly.get_alldata()
        for n in source.enginename:
            scale=self.aly.get_allscale(n)
            self.all_rscale[n]=scale
        self.zu_namel=source.enginename
        self.zu_name=["比例%", "工程师"]
        self.deep_state=1
    def duibi_hx(self):
        self.deep_state=1
        self.zu_name=["比例%", "工程师"]
        
        self.deep_state=1
        self.update()
    def duibi_zx(self):
        self.deep_state=2
        self.all_result=source.deep_engwages
        self.zu_name=["薪资", "工龄"]
        self.ze_Ewage=self.aly.get_wages()
        self.update()
    def duibi_nl(self):
        self.deep_state=3
        self.update()
    def bigin_click(self):
        if not source.isbigan:
            self.second=0
            if source.ui.comboBox_2.currentText ()=="58同城":
                t=Tnuls(0)
                t.start()
                source.isbigan=True
            if  source.ui.comboBox_2.currentText ()=="中华英才网":
                t=Tnuls(1)
                t.start()
                source.isbigan=True
            if  source.ui.comboBox_2.currentText ()=="智联招聘":
                t=Tnuls(2)
                t.start()
                source.isbigan=True
            if  source.ui.comboBox_2.currentText ()=="猎聘猎头网":
                t=Tnuls(3)
                t.start()
                source.isbigan=True
            if  source.ui.comboBox_2.currentText ()=="卓博人才网":
                t=Tnuls(4)
                t.start()
                source.isbigan=True
            if  source.ui.comboBox_2.currentText ()=="前程无忧":
                t=Tnuls(5)
                t.start()
                source.isbigan=True
        
        if  source.isbigan:
            self.catch_time=0
            t1 = threading.Thread(target=self.threadcl) #创建第一个子线程，子线程的任务
            t1.setDaemon(True)
            t1.start()
        self.update()
        
    def show_click(self):
        self.getdata()
        self.setUpdatesEnabled(False);
        self.setUpdatesEnabled(True);
        self.repaint();
        if len(self.bestlist)>0:
            bestlist=self.bestlist
            antext=source.Eanalyze[source.ui.comboBox.currentText ()]
            analyze_text=self.set_ayetext(antext, self.ename, bestlist)
          
            source.ui.textEdit_get.setText(analyze_text)
    def set_ayetext(self, antext, name, bestlist):
        analyze_text=""
        if name=="1.嵌入式软件工程师":
            analyze_text=antext[0]+bestlist[4]+antext[1]+bestlist[0]+antext[2]+bestlist[1]+antext[3]+bestlist[2]+antext[4]+bestlist[3]+antext[5]
            return analyze_text
        if name=="2.JAVA软件工程师":
            b=bestlist[3]
            bestlist[3]=bestlist[4]
            bestlist[4]=b
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist) and not i==5:
                    analyze_text=analyze_text+bestlist[i]
                    
            return analyze_text
        if name=="3.WEB软件工程师":
            b=bestlist[2]
            bestlist[2]=bestlist[3]
            bestlist[3]=b
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            return analyze_text
        if name=="4.IOS软件工程师":
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            return analyze_text
        if name=="5..Net软件工程师":
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            return analyze_text
        if name=="6.C#软件工程师":
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            return analyze_text
        if name=="7.PHP软件工程师":
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            return analyze_text
        if name=="8.Android开发工程师":
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            return analyze_text
        if name=="9.C++软件工程师":
            for i in range(len(antext)):
                analyze_text=analyze_text+antext[i]
                if i<len(bestlist):
                    analyze_text=analyze_text+bestlist[i]
            return analyze_text
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
    
