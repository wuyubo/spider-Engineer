import re
import urllib
import urllib.request
#from html.parser import HTMLParser

'''
    ******爬虫蜘蛛*************************
'''
class spider():
    def __init__(self):
        self.code='utf-8'   #网页编码方式aa  
    def gethtml(self, url):  # get html
        html=""
        try:
            page = urllib.request.urlopen(url)  #open url
            html =page.read()  #read url
            html=html.decode(self.code,'ignore')  #decode 'utf-8' or 'gb2312'
        except Exception as e:
            print("UrlError:")
            print(e)
            return "error"
        return html
        
    def geturl(self, html, reg): 
        try:
            plist =re.findall(reg,html, re.I)  #find reg in html
        except Exception as e:
            print("ReError:")
            print(e)
            return "error"
        return plist
    def getstring(self, html, reg):
        try:
            pre=re.compile(reg)
            plist =re.findall(pre,html)
        except Exception as e:
            print("GetsError:")
            print(e)
            return "error"
        return plist
    def ismatch(self, html, reg):
        try:
            ismatch=(re.search(reg, html, re.I)!=None)
        except Exception as e:
            print("MatchError:")
            print(e)
            return "error"
        return ismatch

'''
class parseText(HTMLParser):
    def __init__(self):
        self.is_txt=False
        self.strdata=[]
    def handle_starttag(self,tag,attr):  
        if tag=='p':  
            self.is_txt=True  
    def handle_endtag(self,tag):  
        if tag=='p':  
            self.is_txt=False  
    def handle_data(self, data):
       if self.is_txt:
           self.strdata.append(data)
'''
