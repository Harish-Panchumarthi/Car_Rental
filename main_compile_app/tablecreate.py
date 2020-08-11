import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('hskrental.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    # cursorObj.execute("CREATE TABLE customer(id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,uname TEXT,gender TEXT,age INTEGER,email TEXT,phone INTEGER,pwd TEXT,address TEXT)")
    # cursorObj.execute("CREATE TABLE admin(id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,uname TEXT,gender TEXT,age INTEGER,email TEXT,phone INTEGER,pwd TEXT,address TEXT)")
    # cursorObj.execute("CREATE TABLE vehicle(vid INTEGER PRIMARY KEY,model TEXT,rno TEXT,seating TEXT,vtype TEXT,priceperday TEXT,vstatus TEXT,location Text, img TEXT)")
    # cursorObj.execute("CREATE TABLE customerfeedback(userId INTEGER PRIMARY KEY,firstname TEXT,lastname TEXT,emailId TEXT,starrating TEXT,comments TEXT,Date TEXT)")
    # cursorObj.execute("CREATE TABLE logindetails(user TEXT,uId INTEGER PRIMARY KEY,Date TEXT,Time TEXT)")
    # cursorObj.execute("CREATE TABLE Pay(Pid INTEGER PRIMARY KEY,ptype TEXT,status TEXT,bId TEXT,total TEXT)")
    #cursorObj.execute("CREATE TABLE booking(bookingid INTEGER PRIMARY KEY,startdate TEXT,enddate TEXT,starttime TEXT,returntime TEXT,pickloc TEXT,droploc TEXT,carid INTEGER,customerid INTEGER)")

    cursorObj.execute("SELECT * FROM vehicle")
    r = cursorObj.fetchall()
    con.commit()
    # print(r)
con = sql_connection()

sql_table(con)
