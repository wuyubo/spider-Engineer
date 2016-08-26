from source import source
#from DataBase import DataBase
from RW_txt import Read_txt
class analyze():
    def __init__(self):
        #self.db=DataBase()
        self.resultlist=[]
        self.scalelist=[]
        self.all_result={"1.嵌入式软件工程师":[], 
                    "2.JAVA软件工程师":[], 
                    "3.WEB软件工程师":[] , 
                    "4.IOS软件工程师":[], 
                    "5..Net软件工程师":[], 
                    "6.C#软件工程师":[],
                    "7.PHP软件工程师":[],
                    "8.Android开发工程师":[],
                    "9.C++软件工程师":[]
                    }
        self.all_wages={"1.嵌入式软件工程师":[], 
                    "2.JAVA软件工程师":[], 
                    "3.WEB软件工程师":[] , 
                    "4.IOS软件工程师":[], 
                    "5..Net软件工程师":[], 
                    "6.C#软件工程师":[],
                    "7.PHP软件工程师":[],
                    "8.Android开发工程师":[],
                    "9.C++软件工程师":[]
                    }
        self.all_Ewages={"1.嵌入式软件工程师":5000, 
                    "2.JAVA软件工程师":5000, 
                    "3.WEB软件工程师":5000 , 
                    "4.IOS软件工程师":5000, 
                    "5..Net软件工程师":5000, 
                    "6.C#软件工程师":5000,
                    "7.PHP软件工程师":5000,
                    "8.Android开发工程师":5000,
                    "9.C++软件工程师":5000
                    }
        self.num=0.000
    def select_all(self, name):
        source.read_txt=Read_txt(source.Edbname[name])
        read_txt=source.read_txt
        rl=[]
        classrl=[]
        classfy=source.Eclassfy[name]
       # self.db.open()
        #result=self.db.select(dbname)
        result=read_txt.readlines()
        if result=="error":
            return "error"
        for r in result:
            res=r.split(',')
            rl.append(res)
        self.all_result[name]=rl
        k=0
        for c in classfy:
            classrl.append([c[0]])
            for n in range(len(c)):
                classrl[k].append(0)
            k=k+1
        for i in rl:
            for k in range(0, len(i)):
                for j in range(len(classfy)):
                    for n in range(1, len(classfy[j])):
                        if classfy[j][n]==k+2:
                            if i[k]=="1":
                                classrl[j][n]=classrl[j][n]+1
        #self.db.close()
        read_txt.close()
        return classrl
    def getscale(self, result):
        scalelist=[]
        if len(result)>0:
            sum=0
            #scalelist.append(result[0])
            for l in range(1, len(result)):
                sum=sum+result[l]
            if sum==0:
                return 0
            for l in range(1, len(result)):
                scalelist.append(result[l]/sum)
        return scalelist
    def getbest(self, classrl, name):
        data_name=source.Erealdata[name]
        classfy=source.Eclassfy[name]
        resultlist=[]
        for c in classrl:
            rl=[]
            for i in range(1, len(c)):
                rl.append(c[i])
            resultlist.append(rl)
        bestlist=[]
        biglist=[]
        for r in resultlist:
            biglist.append(r.index(self.compare(r)))
        i=0
        for big in biglist:
            bestlist.append(data_name[classfy[i][big+1]-1])
            i=i+1
        return bestlist
    def compare(self, list):
        big=0
        for s in list:
            if s>big:
                big=s
        return big
    def get_alldata(self):
        rl=[]
        self.num=0
        for n in source.enginename:
            read_txt=Read_txt(source.Edbname[n])
            result=read_txt.readlines()
            if result=="error":
                return "error"
            self.num=self.num+len(result)-1
            for r in result:
                res=r.split(',')
                res.pop()
                rl.append(res)
            rl.pop()
            self.all_result[n]=rl
            rl=[]
            read_txt.close()
        return self.all_result
    def get_allscale(self, name):
        result=self.all_result[name]
        return len(result)/self.num
    def get_wages(self):
        read_txt=Read_txt("wages")
        result=read_txt.readlines()
        name=""
        wage=0
        if result=="error":
                return "error"
        for r in result:
                res=r.split('-')
                if len(res)==3:
                    name=res[0]
                    wage=(int(res[1])+int(res[2]))/2
                    self.all_wages[name].append(wage)
        for n in source.enginename:
            wage=0
            for w in self.all_wages[n]:
                wage=wage+w
            if len(self.all_wages[n])>0:
                wage=wage/len(self.all_wages[n])
                self.all_Ewages[n]=int(wage)
        return self.all_Ewages
