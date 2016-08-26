import os
class Read_txt():
    def __init__(self, file_name):
        #BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
        BASE_DIR =os.getcwd()
        self.read=open(BASE_DIR +'\data_txt\\'+file_name+'.txt','r')
    def readlines(self):
        data_list=[]
        data=self.read.read()
        data_list=data.split('\n')
        return data_list
    def close(self):
        self.read.close()
class Write_txt():
    def __init__(self, file_name):
        #BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
        BASE_DIR =os.getcwd()
        self.write=open(BASE_DIR +'\data_txt\\'+file_name+'.txt','a')
    def writelines(self, data):
        self.write.writelines(data+'\n')
        return "success"
    def close(self):
        self.write.close()
