import spider
#from DataBase import DataBase
from source import source


'''
    ***爬虫最小网络*******************************
'''
class crawler():
    def __init__(self, num):
        self.num=num
        self.sp=spider.spider()
        if num==4 or num==5:
            self.sp.code='gb2312'
        self.html=""
        self.engineName=r'.*?java.*?工程师.*?'
        #self.db=DataBase()
    def sethtml(self, html):
        self.html=html
    def gethtml(self, url):
        self.html=self.sp.gethtml(url)
        #if self.checkhtml(self.html):
         #   return "error"
        return self.html
    def geturllist(self):
        reg=self.getreg(self.num)
        urllist=self.sp.geturl(self.html, reg)
        return urllist 
    def csql(self, name):
        name_txt=source.select_txt(name)
        data=""
        edatalist=source.Edatalist[name]
        #ename=source.Edbname[name]
        Text=self.html
        count=0
        for d in edatalist:
            if self.sp.ismatch(Text, d):
                data=data+"1,"
                count=count+1
            else:
                data=data+"0,"
        self.getsalary(name)
        if count>0:
            iferror=name_txt.writelines(data)
            return  iferror
        return "empty"
    def inserthurl(self, name, url):
        iferror=source.write_htyurl_txt.writelines(url)
       #self.db.insert("'"+name+"','"+url+"'","historyurl")
        if iferror=="error":
            return iferror
        return "seccess"
    def checkurl(self, name, url):
        isexit=False
        result=source.read_txt.readlines()
        #self.db.select("historyurl "," WHERE url='"+url+"' and name='"+name+"'")
        if  not result=="error":
            for r in result:
                isexit=(url==r)
                break
        return isexit
    def getsalary(self, name):
        name_txt=source.write_wagestxt
        reg=r'([\d].*[-]?[\d].*)[元万].?[/]?[月年].?'
        salary=self.sp.getstring(self.html, reg)
        if len(salary)>0:
                return name_txt.writelines(name+"-"+salary[0])
        else :
            return "面议"
    def checkhtml(self, html):
        reg=r'访问.*?频繁'
        return self.sp.ismatch(html, reg)
        
    def setengineName(self, name):
        if name=="2.JAVA软件工程师":
            self.engineName=r'.*?java.*?工程师.*?'
        if name=="1.嵌入式软件工程师":
            self.engineName=r'.*?嵌入式.*?工程师.*?'
        if name=="3.WEB应用软件工程师":
            self.engineName=r'.*?WEB.*?工程师.*?'
        if name=="4.IOS软件工程师":
            self.engineName=r'.*?Ios.*?工程师.*?'
        if name=="5..Net软件工程师":
            self.engineName=r'.*?\.NET.*?工程师.*?'
        if name=="6.C#软件工程师":
            self.engineName=r'.*?C#.*?工程师.*?'
        if name=="7.PHP软件工程师":
            self.engineName=".*?PHP.*?工程师.*?"
        if name=="8.Android开发工程师":
            self.engineName=".*?安卓.*?工程师.*?|.*?Android.*?工程师.*?"
        if name=="9.C++软件工程师":
            self.engineName=".*?C\+\+.*?工程师.*?"
    def getreg(self, num):
        if num==0 or num==2:
            reg=r'<a .*?href=.(http://.*?). target="_blank".*?>('+self.engineName+')</a>'
        if num==1:
            reg=r'<a .*?href=.(http://.*?). target="_blank".*?>\r[\n].[\t]*('+self.engineName+')\r[\n].'
        if num==3:
            reg=r'<a title="('+self.engineName+')".*?href="(http://.*?)".*?>'
        if num==4:
            reg=r'<a .*?href=.(.*?). target="_blank".*?>('+self.engineName+')</a>'
        if num==5:
            reg=r'<td class="td1"><a .*?href="(http://.*?)".*?>('+self.engineName+')</font>.*?</a>'
        return reg
     
'''
    def getstrlist(self):
        reg=r'.*?任职要求([岗任].*?[位职].*?[职资要].*?[责格求].*?.*?).*?联系方式'
        strlist=self.sp.getstring(self.html, reg)
        return strlist
    def getText(self):
        reg=r'<p.*?>(.*?)</[p>'
       # reg=r'[\u4e00-\u9fa5]+'
        strText=self.sp.getstring(self.html, reg)
        str=""
        for s in strText:
            str=str+"|"+s
        return str
'''
