import threading
from crawler import crawler
from spider import spider
from DataBase import DataBase
from source import source
from PyQt5 import QtCore

class qthreadt(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.stop=False
    def run(self):
        while not self.stop:
            print("12")
            print("12")
            print("12")
            print("12")
            self.stop=True
        print("aa")
        self.__init__()
        print("bb")
        
class Tnuls(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num=num
        self.cl=crawler()
    def run(self):
        if self.num==0:
            for i in range(1, source.urllist[self.num][1]):
                source.nurllist[self.num].append([source.urllist[self.num][2]+str(i),str(i)])
        if self.num==1:
            for i in range(1, source.urllist[self.num][1]):
                source.nurllist[self.num].append([source.urllist[self.num][2]+str((i-1)*20),str(i)])
        source.nurlisend[self.num]=True
class Tgetnexturl(threading.Thread):
    isend=False
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num=num
        self.cl=crawler()
        self.url=source.urllist[num][0]
        self.setDaemon(True)
        self.stop=False
        self.db=DataBase()
        self.headurl=source.urllist[num][1]
        self.hurl=source.urllist[num][2]
    def run(self):
        while not self.stop:
            htmlt=["1",self.cl.gethtml(self.url) ]
            source.htmllist[self.num].append(htmlt)#//////////////
            nul=self.cl.getnexturl(self.hurl)
            source.nurllist[self.num]=source.nurllist[self.num]+nul
            #for n in nul:
              # self.db.insert(n[1]+","+n[0], "nexturl(page,url)")
            self.getnexturl(nul, self.cl)
    def getnexturl(self,lasturl,cl):
        if  cl.isend():
            htmlt=[lasturl[len(lasturl)-1][1], cl.gethtml(self.headurl+lasturl[len(lasturl)-1][0])]
            source.htmllist[self.num].append(htmlt)#//////////////
            nus=cl.getnexturl(self.hurl)
            index=nus.index(lasturl[len(lasturl)-2])
            del nus[0:index+1]
            source.nurllist[self.num]=source.nurllist[self.num]+nus
           # for n in nus:
             #   self.db.insert(n[1]+","+n[0], "nexturl(page,url)")
            self.getnexturl(nus, cl)
        else :
            self.stop=True
            source.nurlisend[self.num]=True
            
class Tdownloadhtml(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.sp=spider()
        self.nulcount=1
        #self.headurl=source.urllist[num][1]
        self.headurl=""
        self.stop=False
        self.num=num
    def run(self):
        while not self.stop:
            if (len(source.nurllist[self.num])+1)>self.nulcount:
               # for i in range(self.nulcount, (len(Tgetnexturl.nurllist))):
               for url in source.nurllist[self.num]:
                    if self.nulcount<(source.nurllist[self.num].index(url)+1):
                        dhtml=downhtml(url, self.num)
                        dhtml.start()
                        self.nulcount=self.nulcount+1
            if source.nurlisend[self.num] and self.nulcount==len(source.nurllist[self.num]):
                self.stop=True
                source.downisend[self.num]=True
class downhtml(threading.Thread):
    def __init__(self, url, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.url=url[0]
        self.index=url[1]
        self.exist=False
        self.cl=crawler()
        self.stop=False
        self.num=num
        self.headurl=source.urllist[num][1]
    def run(self):
        if not self.stop:
            htmlt=[self.index, self.cl.gethtml(self.url)]
            source.htmllist[self.num].append(htmlt)
            self.stop=True
        
class TgetEngineurl(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.cl=crawler()
        self.htlcount=0
        self.db=DataBase()
        self.stop=False
        self.names=source.enginename
        self.num=num
    def run(self):
        while not self.stop:
            if self.htlcount<(len(source.htmllist[self.num])+1):
                for htmlt in source.htmllist[self.num]:
                    for n in self.names:
                        e=tgeteurl(htmlt, n, self.num)
                        e.start()
                    self.htlcount=self.htlcount+1
            if source.downisend[self.num] and self.htlcount==len(source.htmllist[self.num]):
                source.teisend[self.num]=True
                self.stop=True
class tgeteurl(threading.Thread):
    def __init__(self, htmlt, name, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.cl=crawler()
        self.html=htmlt[1]
        self.name=name
        self.num=num
    def run(self):
        self.cl.sethtml(self.html)
        self.cl.setengineName(self.name)
        urllist=self.cl.geturllist()
        for urlt in urllist:
            d=TdownEnghtml(self.name, urlt, self.num)
            d.start()
        source.Engineurllist[self.num]=source.Engineurllist[self.num]+urllist
                    
class TdownEnghtml(threading.Thread):
    def __init__(self, name, urlt, num):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.name=name
        self.urlt=urlt
        self.cl=crawler()
        self.stop=False
        self.ehcount=0
        self.num=num
    def run(self):
        self.cl.gethtml(self.urlt[0])
        htmlt=[self.name, self.urlt[1],self.cl.getText()]
        source.enghtmllist[self.num].append(htmlt)

            
            
                    
                    
