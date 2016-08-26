'''
    *****全局资源类****************************
'''

from RW_txt import Write_txt
from RW_txt import Read_txt

class source():
    ui=""
    #各大招聘网站
    urllist=[["1、58同城http://gz.58.com/ruanjiangong/",6 , "http://gz.58.com/ruanjiangong/pn", "下一页"], 
    ["2、中华英才网http://www.chinahr.com/so/", 6, "http://www.chinahr.com/so/0/0-0-0-0-0-0-0-1001_1002_1005-0-0-0-0-0-0-0-0/p", "下页"], 
    ["3、智联招聘http://sou.zhaopin.com/", 4, "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e8%be%93%e5%85%a5%e9%80%89%e6%8b%a9%e5%9f%8e%e5%b8%82&kw=%e8%bd%af%e4%bb%b6%e5%b7%a5%e7%a8%8b%e5%b8%88&sm=0&sg=b9ecd3105d5944cda4ae5f6298edbdbc&p="], 
    ["4、猎聘猎头网http://www.liepin.com/", 6, "http://www.liepin.com/zhaopin/?searchField=1&key=%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&industries=&jobTitles=&dqs=050020&compscale=&compkind=&pubTime=&salary=&searchType=1&clean_condition=&jobKind=&isAnalysis=&init=-1&ckid=7cd1389bba732646&curPage="], 
    [ "5、卓博人才网http://www.jobcn.com/",6, "http://www.jobcn.com/search/result.xhtml?s=search%2Ftop&p.sortBy=&p.jobLocationId=&p.jobLocationTown=&p.jobLocationTownId=&p.keyword=%C8%ED%BC%FE%B9%A4%B3%CC%CA%A6&p.keywordType=2&p.workLocation=#P"],
    ["6、前程无忧www.51job.com", 1, "http://search.51job.com/list/000000%252C01,000000,0000,00,9,99,%25C8%25ED%25BC%25FE%25B9%25A4%25B3%25CC%25CA%25A6,1,",".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&confirmdate=14"]
    ]
    #主要查找的软件工程师
    enginename=["1.嵌入式软件工程师","2.JAVA软件工程师", "3.WEB软件工程师" , "4.IOS软件工程师", "5..Net软件工程师", "6.C#软件工程师","7.PHP软件工程师","8.Android开发工程师","9.C++软件工程师"]
   # enginename=["嵌入式软件工程师","JAVA软件工程师"]
    nurllist=[[], [], [], [], [], [], [], [], [], [], [], []]
    nurlisend=[False, False, False, False, False, False, False, False, False]
    htmllist=[[], [], [], [], [], [], [], [], [], [], []]
    enghtmllist=[[], [], [], [], [], [], [], [], [], [], []]
    Engineurllist=[[], [], [], [], [], [], [], [], [], [], []]
    downisend=[False, False, False, False, False, False, False, False, False]
    teisend=[False, False, False, False, False, False, False, False, False]
    nuls=[[], [], [], [], [], [], [], [], [], [], []]
    isendhtml=[False, False, False, False, False, False, False, False, False]
    
    #各工程师可能要具备的技能
    Edatalist={"1.嵌入式软件工程师":["C","Linux","gui[编]?[程]?","Socket|网络[Socket].*?编程","android|安卓","ARM|Cortex","Orancle","RTOS","PCB|电路[设]?[计]?","通讯[协]?[议]?|[通]?[讯]?协议","多线程|多进程","TCP/IP","http/https","MS[ ]?SQL","mysql"],											
                    "2.JAVA软件工程师":["Java[ ]?Web","JSP","Servlet","Struts2","Ajax","Javascript","html\+CSS","Websphere","Weblogic","Jboss","Tomcat","Linux","Unix","xml|XML[ ]?Schema",
                                                "UML","socket[编]?[程]?","Jbuilder","Eclipse","C\+\+","J2EE","struts","spring","(hibernate)[框]?[架]?","(基于JAVA平台的)?B/S(架构)?",
                                                "Oracle","MS[ ]?SQL","mysql","java"],
                    "3.WEB软件工程师":["ASP\.NET","SQL[ ]?server","mysql","css","Extjs","Ext\.net","jquery","bootstrap",
                                                "Oralce","MS[ ]?SQL","Socket","TCP/IP",'http/https',"Java[ ]?script"],
                    "4.IOS软件工程师":["Objective C|ObjectiveC|Objective-C|ObjC","Cocoa[编]?[程]?","iPhoneSDK|iPhone SDK|SDK","底层API[调]?[用]?|API[调]?[用]?","macosx|macos x","xcode" ,
                                                "C\+\+","java[^s].","IOS","MacOS|Mac OS","Socket","TCP/IP|通讯协议|TCP",'http/https|^[^="].http',"swift"],
                    "5..Net软件工程师":["ASP\.NET[(]?[C]?[#]?[)]?",'^[^</"\\].JavaScript^[^">]|js|^[^</"].Java Script^[^">]',"SQL[ ]?server","mysql","MVC(开发模式)?|三层机制","^[^</]html5","Extjs","Ext\.net",
                                                "bootstrap","b/s","vs\.net|Visual[ ]?Studio\.net","C#","^[^</]HTML","WebService[s]?|Web Service[s]?","jquery","div\+css","oracle","AJAX"],
                    "6.C#软件工程师":["Visual[ ]?Studio|vs","SQL[ ]?Server","\.net","C#","WinForm[开]?[发]?","MYSQL","ORACLE","C\+\+","java^[^s]."],
                    "7.PHP软件工程师":["PHP","MYSQL","^[</].html","DIV+CSS","AJAX","JQuery","Smarty","Postgres[ ]?SQL","sql[ ]?server","Java[ ]?Script|js","JSON","ORACLE"],
                    "8.Android开发工程师":["Android[ ]?OS","Framework","Socket","TCP/IP",'^[^="].http/https',"Linux","JNI","java^[^s]","struts","hibernate","spring","C\+\+","\.Net","XML","Windows"],
                    "9.C++软件工程师":["Unix","C#","ProjectWis","\.Net","Visual[ ]?studio|vs","Oracle","SQl[ ]?Server","TCP/IP","Windows[ ]?API","MFC","socket","LINUX","C\+\+","MySQL","Solaris","Windows"]
                    }
    '''
    Edatalist={"1.嵌入式软件工程师":("C|C\+\+","Linux","gui[编].*?[程].*?","(Socket)|网络[(Socket)]?[编]?[程]?","android","(ARM7)|(Cortex-M3)[内]?[核]?","Orancle|数据库","RTOS","PCB[设]?[计]?","[通]?[讯]?协议","多线程|多进程"),
                    "2.JAVA软件工程师":("Java Web","JSP","Servlet","Ajax","Javascript","html|CSS","Websphere","Weblogic","Jboss","Tomcat","Linux","Unix","XML Schema","UML","socket[编]?[程]?","Jbuilder","Eclipse","C|C\+\+","(J2EE)","(struts)","(spring)","(hibernate)[框]?[架]?","(基于JAVA平台的)?B/S(架构)?","Oralce","MS SQL","mysql"),
                    "3.WEB软件工程师":("ASP.NET(C#)","SQLserver","mysql","html5|css3","Extjs","Ext.net","jquery","bootstrap"),
                    "4.IOS软件工程师":("Objective[- ]*C|swift","Cocoa[编]?[程]?","iPhone SDK","底层API[调]?[用]?","macos x","xcode"),
                    "5..Net软件工程师":("ASP\.NET(C#)","Java[ ]?Script","SQL[ ]?server","mysql","jquery","MVC开发模式|三层机制","html5|html5\+css3","Extjs","Ext.net","bootstrap","b/s","vs.net2003|Visual Studio.NET","C#2.0","HTML","WebServices","div\+css","ORACLE",),
                    "6.C#软件工程师":("Visual[ ]?Studio|vs","SQL[ ]?Server",".NET","C#[语]?[言]?","WinForm[开]?[发]?"),
                    "7.PHP软件工程师":("PHP[编]?[程]?","MYSQL","HTML5","DIV\+CSS","AJAX","JQuery","Smarty"),
                    "8.Android开发工程师":("Android OS","Framework","Socket","TCP/IP","http/https","Linux","JNI"),
                    "9.C++软件工程师":("Unix","C#","SQL[ ]?server","ProjectWis",".Net","Visual[ ]?studio","Oracle","TCP/IP","Windows[ ]?API","MFC","socket","LINUX")}
    '''
    #各工程师的数据库表名
    Edbname={"1.嵌入式软件工程师":"embedded","2.JAVA软件工程师":"java", "3.WEB软件工程师":"web" , "4.IOS软件工程师":"ios", "5..Net软件工程师":"net", "6.C#软件工程师":"ch","7.PHP软件工程师":"php","8.Android开发工程师":"android","9.C++软件工程师":"cpp"}
    
     #各工程师可能要具备的技能
    Erealdata={"1.嵌入式软件工程师":[15,"C\C++","Linux","gui编程","Socket网络编程","android","ARM7、Cortex-M3内核","Orancle数据库","RTOS","PCB设计","通讯协议","多线程、多进程","TCP/IP","http/https","MS SQL","mysql"],											
                    "2.JAVA软件工程师":[28,"Java Web","JSP","Servlet","Struts2","Ajax","Javascript","html+CSS","Websphere","Weblogic","Jboss","Tomcat","Linux","Unix","XML Schema",
                                                "UML","socket编程","Jbuilder","Eclipse","C\C++","J2EE","struts","spring","hibernate框架","基于JAVA平台的B/S架构",
                                                "Oralce","MS SQL","mysql","java"],
                    "3.WEB软件工程师":[14,"ASP.NET(C#)","SQLserver","mysql","html5","Extjs","Ext.net","jquery","bootstrap",
                                                "Oralce","MS SQL","Socket","TCP/IP","http/https","Javascript"],
                    "4.IOS软件工程师":[14,"Objective C","Cocoa编程","iPhone SDK","底层API调用","macos x","xcode" ,
                                                "C/C++","java","IOS","MacOS","Socket","TCP/IP","http/https","swift"],
                    "5..Net软件工程师":[18,"ASP.NET(C#)","JavaScript","SQLserver","mysql","MVC开发模式三层机制","html+css","Extjs","Ext.net",
                                                "bootstrap","b/s","vs.net2003","C#2.0","HTML","WebServices","jquery","div|css","oracle","AJAX"],
                    "6.C#软件工程师":[9,"Visual Studio","SQLServer",".NET","C#语言","WinForm开发","MYSQL","ORACLE","C/C++","java"],
                    "7.PHP软件工程师":[12,"PHP编程","MYSQL","html","DIV+CSS","AJAX","JQuery","Smarty","Postgres SQL","sqlserver","JavaScript","JSON","ORACLE"],
                    "8.Android开发工程师":[15,"Android OS","Framework","Socket","TCP/IP","http/https","Linux","JNI","java","struts","hibernate","spring","C/C++",".Net","XML","Windows"],
                    "9.C++软件工程师":[16,"Unix","C#","ProjectWis",".Net","Visual studio","Oracle","SQl Server","TCP/IP","Windows API","MFC","socket","LINUX","C/C++","MySQL","Solaris","Windows"]}
                    
                    
    Eclassfy={"1.嵌入式软件工程师":(["数据库", 8,15,16], ["系统类", 3,6,9], ["网络类", 5,11,13,14], ["其他技术", 4,7,10,12], ["语言类", 2]),
                    "2.JAVA软件工程师":(["语言类", 20,15,16,29], ["数据库", 26,27,28], ["平台工具", 4,9,10,11,12,18,19,], ["架构", 5,21,22,23,24,25], ["系统类", 13,14], ["网络类", 6,7,8,17]), 
                    "3.WEB软件工程师":(["语言类", 2,5], ["数据库", 3,4,10,11], ["平台工具", 7,8], ["网络类", 12,13,14,15], ["架构", 6,9]) , 
                    "4.IOS软件工程师":(["语言类", 2,15], ["系统", 7,10,11], ["网络类", 12,13,14], ["平台工具", 3,4,5]), 
                    "5..Net软件工程师":(["语言类", 2,3,14], ["数据库", 4,5], ["网络类", 7,15,19], ["平台工具", 8,9,10,11,12,15,16], ["其他", 6,17]), 
                    "6.C#软件工程师":(["语言类",5,9,10], ["数据库",3,7,8], ["平台工具",2,4,6]),
                    "7.PHP软件工程师":(["语言类", 2], ["数据库", 3,9,10,13], ["网络类", 4,5,6,11,12], ["平台工具", 7,8]),
                    "8.Android开发工程师":(["语言类", 9,13,14], ["操作系统", 2,7,16], ["网络类", 4,5,6,15], ["框架", 3,10,11,12]),
                    "9.C++软件工程师":(["语言类", 3,5, 14], ["数据库", 7,15], ["系统", 2,13,16,17], ["网络类", 5,9,12], ["平台工具", 4,6,10,11])}
   
    Eanalyze={"1.嵌入式软件工程师":("通过数据分析和市场行情调查，嵌入式软件工程师需要掌握的语言是:",
                                    ", 需要掌握的数据库是:", ", 需要掌握的系统是", ", 需要学习的网络知识是:", "除此之外，该职业还要求工作者掌握 ", "技术。掌握以上技术的毕业生，其平均工资将起步于4000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于6000，甚至达到上万以上。"),
                    "2.JAVA软件工程师":("通过数据分析和市场行情调查，java软件工程师需要掌握的语言是:", "，需要掌握的数据库是","，需要掌握的平台工具是:", "， 需要掌握的系统是","，除此之外，该职业还要求工作者掌握","架构。掌握以上技术的毕业生，其平均工资将起步于3000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于6000。"), 
                    "3.WEB软件工程师":("通过数据分析和市场行情调查，web软件工程师需要掌握的语言是","，需要掌握的数据库是","，需要掌握的网络知识是","，需要掌握的平台工具是","，除此之外，该职业还要求工作者掌握","架构。掌握以上技术的毕业生，其平均工资将起步于3000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于6000。") , 
                    "4.IOS软件工程师":("通过数据分析和市场行情调查，iOS软件工程师需要掌握的语言是","，需要掌握的系统是","，需要掌握的网络知识是","，需要掌握的平台工具是","。掌握以上技术的毕业生，其平均工资将起步于5000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于8000，甚至超过10000。"), 
                    "5..Net软件工程师":("通过数据分析和市场行情调查，Net软件工程师需要掌握的语言是","，需要掌握的数据库是","，需要掌握的网络知识是","，需要掌握的平台工具是","，除此之外，该职业还要求工作者掌握","技术。掌握以上技术的毕业生，其平均工资将起步于3000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于5000。"), 
                    "6.C#软件工程师":("通过数据分析和市场行情调查，C#软件工程师需要掌握的语言是","，需要掌握的数据库是","，需要掌握的平台工具是",",掌握以上技术的毕业生，其平均工资将起步于2500，随着工作时间的增加以及工作经验的积累，其平均工资将会高于4000。"),
                    "7.PHP软件工程师":("通过数据分析和市场行情调查，PHP软件工程师需要掌握的语言是,""，需要掌握的数据库是","，需要掌握的网络知识是","，需要掌握的平台工具是","。掌握以上技术的毕业生，其平均工资将起步于3000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于5000。"),
                    "8.Android开发工程师":("通过数据分析和市场行情调查，Android软件工程师需要掌握的语言是","，需要掌握的系统是","，需要掌握的网络知识是","，需要掌握的架构是","，除此之外，该职业还要求工作者掌握","平台工具。掌握以上技术的毕业生，其平均工资将起步于3000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于5000。"),
                    "9.C++软件工程师":("通过数据分析和市场行情调查，C++软件工程师需要掌握的语言是","，需要掌握的数据库是","，需要掌握的系统是","，需要掌握的网络知识是","，除此之外，需要掌握的平台工具是","。掌握以上技术的毕业生，其平均工资将起步于3000，随着工作时间的增加以及工作经验的积累，其平均工资将会高于6000。")
                    }
    #downhtmllist=[[], [], []]
    threadnum=0
    isurlerror=[False, False, False, False, False, False, False, False, False, False]
    isbigan=False  #是否开始爬虫
    isgetweb=False #是否已经爬虫
    waiteurl=[]#下载出错的url
    waitpurl=[]
    #---------------------------------------------------------------
    deep_years=["应届","1-3年", "3-5年", "5-10年"]
    deep_wages=[4000, 20000]
    deep_engwages={"1.嵌入式软件工程师":[4333, 12064, 12912, 15780], 
                    "2.JAVA软件工程师":[4833, 10139, 13921, 17336], 
                    "3.WEB软件工程师":[5696, 10301, 13488, 17122,] , 
                    "4.IOS软件工程师":[5564, 12088, 15733, 19261], 
                    "5..Net软件工程师":[4237, 9852, 12618, 18659], 
                    "6.C#软件工程师":[4565,8566,12018,19273],
                    "7.PHP软件工程师":[4786, 11423, 14825, 19237],
                    "8.Android开发工程师":[5341, 11361, 15162, 19035],
                    "9.C++软件工程师":[7076, 13268, 15613, 18961]
                    }
    deep_zuay=["的市场需求量所占比例为",",在所有工程师中排名第","位,"]
    deep_zuay1=["市场需求量所占比例重，人才需求量大，市场前景广阔，就业机会众多！！！", 
                    "市场需求量所占比例较大，人才需求量较多，就业市场虽不太火爆，但也不\n至于高冷！！值得有兴趣的同学专攻！！", 
                    "市场需求量比较小，人才需求量不大，就业市场不太乐观，初学者在选择方\n向时，务必考虑清楚，权衡利弊方做决定！"
                    ]
    #-----------------------------------------------------------------
    #文件
    read_txt=""
    write_htyurl_txt=""
    write_embeddedtxt=""
    write_webtxt=""
    write_iostxt=""
    write_nettxt=""
    write_chtxt=""
    write_cpptxt=""
    write_androidtxt=""
    write_phptxt=""
    write_javatxt=""
    write_wagestxt=""
    @staticmethod
    def open_txt():
        source.read_txt=Read_txt('historyurl1')
        source.write_htyurl_txt=Write_txt('historyurl')
        source.write_embeddedtxt=Write_txt('embedded')
        source.write_webtxt=Write_txt('web')
        source.write_iostxt=Write_txt('ios')
        source.write_nettxt=Write_txt('net')
        source.write_chtxt=Write_txt('ch')
        source.write_cpptxt=Write_txt('cpp')
        source.write_androidtxt=Write_txt('android')
        source.write_phptxt=Write_txt('php')
        source.write_javatxt=Write_txt('java')
        source.write_wagestxt=Write_txt('wages')
    @staticmethod
    def close_txt():
        source.read_txt.close()
        source.write_htyurl_txt.close()
        source.write_embeddedtxt.close()
        source.write_webtxt.close()
        source.write_iostxt.close()
        source.write_nettxt.close()
        source.write_chtxt.close()
        source.write_cpptxt.close()
        source.write_androidtxt.close()
        source.write_phptxt.close()
        source.write_javatxt.close()
        source.write_wagestxt.close()
    @staticmethod
    def select_txt(ename):
        if ename=="1.嵌入式软件工程师":
            return source.write_embeddedtxt
        if ename=="2.JAVA软件工程师":
            return  source.write_javatxt
        if ename=="3.WEB软件工程师":
            return source.write_webtxt
        if ename=="4.IOS软件工程师":
            return source.write_iostxt
        if ename=="5..Net软件工程师":
            return source.write_nettxt
        if ename=="6.C#软件工程师":
            return source.write_chtxt
        if ename=="9.C++软件工程师":
            return source.write_cpptxt
        if ename=="8.Android开发工程师":
            return  source.write_androidtxt
        if ename=="7.PHP软件工程师":
            return  source.write_phptxt
    @staticmethod
    def copy_txt():
        read_htyurl_txt=Read_txt('historyurl')
        write_htyurl_txt=Write_txt('historyurl1')
        relist=read_htyurl_txt.readlines()
        for r in relist:
            write_htyurl_txt.writelines(r)
        read_htyurl_txt.close()
        write_htyurl_txt.close()
