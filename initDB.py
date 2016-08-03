import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.createTable()

    def checkRegistration(self, Topic):
        cur = self.con.cursor()
        params = (Topic,)
        cur.execute('Select * from Service where "Topic" = ?', params)
        result = cur.fetchone()
        print result
        cur.close()
        self.con.commit()
        if (result != None):
            return True
        else:
            return False


    def updateRegistration(self,Server,Topic):
        cur = self.con.cursor()
        cur.execute("UPDATE Service SET Server=? WHERE Topic=?", (Server, Topic))
        cur.close()
        self.con.commit()




    def createTable(self):
        try:
            self.conn.execute('''CREATE TABLE Service
                   (ID INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
                   Server           TEXT    NOT NULL,
                   Topic            TEXT     NOT NULL);''');
        except Exception, err:
            print err;
            self.conn.commit()


    def insertRegistration(self,Server,Topic):
        if(not self.checkRegistration(self.con,Topic)):
            cur = self.con.cursor()
            cur.execute("insert into Service (Server,Topic) values (?, ?)", (Server, Topic))
            self.con.commit()
        else:
            self.updateRegistration(self.con,Server,Topic)


    def closeconnection(self):
        self.conn.close()




#insertRegistration(conn,"Helloppp",'WTF')




