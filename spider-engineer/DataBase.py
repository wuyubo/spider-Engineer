import pymysql
#import sys
'''
    *****连接mysql数据库*****************************
'''
class DataBase():
    def __init__(self):
        self.conn=database.conn
        self.cur=database.cur
    def insert(self, data, engineurl="engineurl(name,url)"):
        query="INSERT INTO "+engineurl+" VALUES(null,"+data+")"
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print("dbinError:")
            print(e)
            return "error"
        return "success"
    def select(self, tbname, tbcondition=""):
        try:
            self.cur.execute("SELECT * FROM "+tbname+tbcondition)
        except Exception as e:
            print("dbseError:")
            print(e)
            return "error"
        return self.cur
    def delete(self, tbname, tbcondition):
        self.open()
        self.cur.execute("DELETE FROM "+tbname+tbcondition)
        self.conn.commit()
        self.close()
    def close(self):
        self.cur.close()
        self.conn.close()
    def open(self):
        self.conn=pymysql.connect(user='root',passwd='295637',host='localhost',db='secrawler', charset='utf8')
        self.cur=self.conn.cursor()
    def quote_buffer(self, buf):  
        """ 
        chinese to mysql 
        """  
        retstr = ''.join(map(lambda c:'%02x'%ord(c), buf))  
        retstr = "x'" + retstr + "'"  
        return retstr
        
        
class database():
    conn=""
    cur=""
    @staticmethod
    def open():
        database.conn=pymysql.connect(user='root',passwd='295637',host='localhost',db='secrawler', charset='utf8')
        database.cur=database.conn.cursor()
    @staticmethod
    def close():
        database.cur.close()
        database.conn.close()
    @staticmethod
    def insert(data, engineurl="engineurl(name,url)"):
        query="INSERT INTO "+engineurl+" VALUES(null,"+data+")"
        try:
            database.cur.execute(query)
            database.conn.commit()
        except Exception as e:
            print("dbinError:")
            print(e)
            return "error"
        return "success"
    @staticmethod
    def select(tbname, tbcondition=""):
        try:
            database.cur.execute("SELECT * FROM "+tbname+tbcondition)
        except Exception as e:
            print("dbseError:")
            print(e)
            return "error"
        return database.cur
