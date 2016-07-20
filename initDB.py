import sqlite3

conn = sqlite3.connect('test.db')


def checkRegistration(con,Topic):
    cur = con.cursor()
    params=(Topic,)
    cur.execute('Select * from Service where "Topic" = ?',params)
    result=cur.fetchone()
    print result
    cur.close()
    con.commit()
    if(result!=None):
        return True
    else:
        return False


def updateRegistration(con,Server,Topic):
    cur = con.cursor()
    cur.execute("UPDATE Service SET Server=? WHERE Topic=?", (Server, Topic))
    cur.close()
    con.commit()




def createTable(conn):
    try:
        conn.execute('''CREATE TABLE Service
               (ID INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL,
               Server           TEXT    NOT NULL,
               Topic            TEXT     NOT NULL);''');
    except Exception, err:
        print err;
    conn.commit()


def insertRegistration(con,Server,Topic):
    if(not checkRegistration(con,Topic)):
        cur = con.cursor()
        cur.execute("insert into Service (Server,Topic) values (?, ?)", (Server, Topic))
        con.commit()
    else:
        updateRegistration(con,Server,Topic)


createTable(conn)
insertRegistration(conn,"Helloppp",'WTF')


conn.close()

