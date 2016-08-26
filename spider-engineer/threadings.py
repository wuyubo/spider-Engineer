import threading
from crawler import crawler
from source import source
#from DataBase import database
import time
'''
    线程树**********************************
'''
class Tnuls(threading.Thread):     #获得各网站链接，线程树的入口线程
    def __init__(self, num):        
        threading.Thread.__init__(self)
        self.setDaemon(True)#将线程声明为守护线程
        self.num=num
        self.cl=crawler(num)  
        self.cond=threading.Condition()
    def run(self):
        cond=self.cond
        cond.acquire()#
        source.threadnum=source.threadnum+1#线程数+1
        #database.open()#打开数据库
        if  self.num==0 or self.num==2 or self.num==4:
            urllist=source.urllist[self.num]
            for i in range(1,urllist[1]):
                down=downhtml([urllist[2]+str(i),str(i)], self.num)
                down.start()    #开始下载网站线程
                source.nurllist[self.num].append([urllist[2]+str(i),str(i)])
                time.sleep(0.1)
        if self.num==1:
            urllist=source.urllist[self.num]
            for i in range(1, urllist[1]):
                down=downhtml([urllist[2]+str((i-1)*20),str(i)], self.num)
                down.start()
                source.nurllist[self.num].append([source.urllist[self.num][2]+str((i-1)*20),str(i)])
                time.sleep(0.1)
        if self.num==3:
            urllist=source.urllist[self.num]
            for i in range(0, urllist[1]):
                down=downhtml([urllist[2]+str(i),str(i)], self.num)
                down.start()
                source.nurllist[self.num].append([source.urllist[self.num][2]+str(i),str(i)])
                time.sleep(0.1)
        if self.num==5:
            urllist=source.urllist[self.num]
            for i in range(1, urllist[1]):
                down=downhtml([urllist[2]+str(i)+urllist[3],str(i)], self.num)
                down.start()
                source.nurllist[self.num].append([source.urllist[self.num][2]+str(i),str(i)])
                time.sleep(0.1)
        #source.nurlisend[self.num]=True
        cond.notifyAll()#
        cond.release()#
        dw=downwaiturl()
        dw.start()
        source.threadnum=source.threadnum-1#线程数-1
        
        
class downhtml(threading.Thread):  #下载网页的线程
    def __init__(self, url, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)#将线程声明为守护线程
        self.url=url[0]
        self.index=url[1]
        self.cl=crawler(num)
        self.num=num
        self.trytimes=0
        self.cond=threading.Condition()
    def run(self):
        cond=self.cond
        cond.acquire()#
        source.threadnum=source.threadnum+1#线程数+1
        htmlt=[self.index, self.cl.gethtml(self.url)]
        if (not htmlt[1]=="error") and (not source.isurlerror[self.num] ):
            if not self.check(htmlt[1]):
                source.htmllist[self.num].append(htmlt)
                te=TgetEngineurl(htmlt, self.num)
                te.start()
        else :
                if self.trytimes<2:
                    time.sleep(0.1)
                    self.trytimes=self.trytimes+1
                    self.run()
                source.waiteurl.append([self.num, self.url])
                source.isurlerror[self.num]=True
        source.threadnum=source.threadnum-1#线程数-1
        cond.notifyAll()#
        cond.release()#
    def check(self, html):
        for u in source.htmllist[self.num]:
            if u[1]==html:
                print("repetion")
                return True
        return False
            
            
class TgetEngineurl(threading.Thread):    # *****获得工程师的url的入口线程*****
    def __init__(self, htmlt, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)#将线程声明为守护线程
        self.names=source.enginename
        self.num=num
        self.htmlt=htmlt
        self.cond=threading.Condition()
    def run(self):
        cond=self.cond
        cond.acquire()#
        source.threadnum=source.threadnum+1#线程数+1
        for n in self.names:                #*********遍历所有要查找的工程师并分配线程****
            e=tgeteurl(self.htmlt, n, self.num)
            e.start()
        source.threadnum=source.threadnum-1#线程数-1
        cond.notifyAll()#
        cond.release()#
            
            
class tgeteurl(threading.Thread):       #****** 获得工程师的url线程******
    def __init__(self, htmlt, name, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)#将线程声明为守护线程
        self.cl=crawler(num)
        self.html=htmlt[1]
        self.name=name
        self.num=num
        self.cond=threading.Condition()
    def run(self):              #****** 获得工程师的url并分配线程下载html******
        cond=self.cond
        cond.acquire()#
        source.threadnum=source.threadnum+1#线程数+1
        self.cl.sethtml(self.html)
        self.cl.setengineName(self.name)
        urllist=self.cl.geturllist()            
        if len(urllist)>0:
            for urlt in urllist:
                d=TdownEnghtml(self.name, urlt, self.num)
                d.start()
            source.Engineurllist[self.num]=source.Engineurllist[self.num]+urllist
        source.threadnum=source.threadnum-1#线程数-1
        cond.notifyAll()#
        cond.release()#
            
            
class TdownEnghtml(threading.Thread):   #***********下载各工程师的html并品配存入数据库线程*******************
    def __init__(self, name, urlt, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)#将线程声明为守护线程
        self.name=name
        if num==3:
            self.url=urlt[1]
            self.urln=urlt[0]
        else:
            self.url=urlt[0]
            self.urln=urlt[1]
        if num==4:
            self.url="http://www.jobcn.com/"+self.url
        self.cl=crawler(num)
        self.stop=False
        self.ehcount=0
        self.num=num
        self.trytimes=0
        self.cond=threading.Condition()
    def run(self):
        cond=self.cond
        cond.acquire()#
        source.threadnum=source.threadnum+1#线程数+1
        if not self.cl.checkurl(self.name, self.url):
            htmlt=self.cl.gethtml(self.url)
            if (not htmlt[1]=="error") and (not source.isurlerror[self.num] ):
                #htmlt=[self.name, self.urlt[1],self.cl.getText()]
                source.enghtmllist[self.num].append(htmlt)
                iferror=self.cl.csql(self.name)
                if not iferror=="error":
                    self.cl.inserthurl(self.name, self.url)
            else :
                if self.trytimes<2:
                    time.sleep(0.1)
                    self.trytimes=self.trytimes+1
                    self.run()
                source.waiteurl.append([self.num, self.name, self.url])
                source.isurlerror[self.num]=True
        source.threadnum=source.threadnum-1#线程数-1
        cond.notifyAll()#
        cond.release()#


class downwaiturl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)#将线程声明为守护线程
        self.stop=False
        self.times=0
        self.Ttimes=0
        self.cond=threading.Condition()
    def run(self):
        cond=self.cond
        cond.acquire()#
        source.threadnum=source.threadnum+1#线程数+1
        while not self.stop:
            if len(source.waiteurl)>0:
                for urlt in source.waiteurl:
                    ed=TdownEnghtml(urlt[1], urlt[2], urlt[0])
                    ed.start()
                    source.waiteurl.remove(urlt)
                    self.times=self.times+1
                    if  self.times==10:
                        break
                    time.sleep(0.1)
            if len(source.waitpurl)>0:
                for urlt in source.waitpurl:
                    td=downhtml(urlt[1], urlt[0])
                    td.start()
                    source.waiteurl.remove(urlt)
                    self.times=self.times+1
                    if  self.times==10:
                        break
                    time.sleep(0.1)
            self.Ttimes=self.Ttimes+1
            if self.Ttimes==50:
                self.stop=True
            if (source.threadnum==0) and (len(source.waitpurl))==0 and len(source.waiteurl)==0:
                self.stop=True
        source.threadnum=source.threadnum-1#线程数-1
        cond.notifyAll()#
        cond.release()#
        
        
