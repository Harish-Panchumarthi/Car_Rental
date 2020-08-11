from flask import Flask, render_template, request, redirect, flash, url_for, session
import sqlite3
import datetime
import time
import os

app=Flask(__name__)
app.secret_key = 'hskcarrental'

# GLOBAL VARAIBALES
user_name = ""

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/clogin')
def clogin():
  return render_template('customer_login.html')

@app.route('/about')
def about():
  return render_template('about.html')
@app.route('/about1')
def about1():
  return render_template('about1.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/contact1')
def contact1():
  return render_template('contact1.html')

@app.route('/book_car')
def book_car():
  return render_template('book_car.html')

@app.route('/alogin')
def alogin():
  return render_template('admin_login.html')

@app.route('/custsignup')
def custsignup():
  return render_template('customersignup.html')

@app.route('/adminsignup')
def adminsignup():
  return render_template('adminsignup.html')

@app.route('/custlogin',methods = ['POST', 'GET'])
def custlogin():
  if request.method == 'POST':

    con = sqlite3.connect('hskrental.db')
    uname = request.form['uname']
    pwd = request.form['pwd']
    # session['username'] = uname
    #global user_name = uname
    # print(session['username'])
    cursorObj = con.cursor()
    cur = con.cursor()
    cursorObj = con.cursor()
    login=cursorObj.execute("SELECT * FROM customer WHERE uname= ? and pwd= ?;",(uname,pwd))
    con.commit()
    if (len(login.fetchall()) > 0):
      session['uname'] = uname
      session['logged_in_user'] = 'customer'
      return render_template("book_car.html",uname=uname)
    else:
      flash('Invalid Username or Password. Please try again')
      return render_template("customer_login.html")

@app.route('/adminlogin',methods = ['POST', 'GET'])
def adminlogin():
  if request.method == 'POST':

    con = sqlite3.connect('hskrental.db')
    uname = request.form['uname']
    pwd = request.form['pwd']
    cursorObj = con.cursor()
    cur = con.cursor()
    cursorObj = con.cursor()
    login=cursorObj.execute("SELECT * FROM admin WHERE uname= ? and pwd= ?;",(uname,pwd))
    con.commit()
    if (len(login.fetchall()) > 0):
      return render_template("home3.html")
    else:
      return render_template("adminlogin.html")

  return render_template("home3.html")




@app.route('/custreg',methods = ['POST', 'GET'])
def custreg():
  if request.method == 'POST':

    con = sqlite3.connect('hskrental.db')
    fname = request.form['fname']
    lname = request.form['lname']
    uname = request.form['uname']
    gender = request.form['gender']
    age  = request.form['age']
    email = request.form['email']
    phone  = request.form['phone']
    pwd  = request.form['pwd']
    #rpwd  = request.form['rpwd']
    address=request.form['address']
    cursorObj = con.cursor()
    login=cursorObj.execute("SELECT * FROM customer WHERE uname= ?;",(uname,))
    con.commit()
    if (len(login.fetchall()) > 0):
              return render_template("customersignup.html")
    else:
              cursorObj.execute("INSERT INTO customer (fname,lname,uname,gender,age,email,phone,pwd,address) VALUES('"+fname+"', '"+lname+"','"+uname+"', '"+gender+"','"+age+"','"+email+"','"+phone+"','"+pwd+"','"+address+"')")

              con.commit()
              return render_template("thankyou.html")



@app.route('/adminreg',methods = ['POST', 'GET'])
def adminreg():
  if request.method == 'POST':

    con = sqlite3.connect('hskrental.db')
    fname = request.form['fname']
    lname = request.form['lname']
    uname = request.form['uname']
    gender = request.form['gender']
    age  = request.form['age']
    email = request.form['email']
    phone  = request.form['phone']
    pwd  = request.form['pwd']
    #rpwd  = request.form['rpwd']
    address=request.form['address']
    cursorObj = con.cursor()
    login=cursorObj.execute("SELECT * FROM admin WHERE uname= ?;",(uname,))
    con.commit()
    if (len(login.fetchall()) > 0):
              return render_template("adminsignup.html")
    else:
              cursorObj.execute("INSERT INTO admin (fname,lname,uname,gender,age,email,phone,pwd,address) VALUES('"+fname+"', '"+lname+"','"+uname+"', '"+gender+"','"+age+"','"+email+"','"+phone+"','"+pwd+"','"+address+"')")

              con.commit()
              return render_template("thankyou.html")


@app.route('/listadmin')
def listadmin():
  con = sqlite3.connect("hskrental.db")
  con.row_factory = sqlite3.Row

  cur = con.cursor()
  cur.execute("select * from admin")

  rows = cur.fetchall();
  cur.close()
  print(rows);
  # return render_template("details1.html",rows = rows)
  return render_template("manage_admin.html",rows = rows)

@app.route('/listcustomer')
def listcustomer():
  con = sqlite3.connect("hskrental.db")
  con.row_factory = sqlite3.Row

  cur = con.cursor()
  cur.execute("select * from customer")
  rows = cur.fetchall();
  cur.close()
  # return render_template("details.html",rows = rows)
  return render_template("manage_users.html",rows = rows)

@app.route('/deletecustomer',methods = ['POST', 'GET'])
def deletecustomer():
  if request.method == 'POST':

    con = sqlite3.connect('hskrental.db')
    id  = request.form['id']
    cursorObj = con.cursor()
    cur = con.cursor()
    cursorObj.execute("DELETE FROM customer where id="+id+"")
    con.commit()
  return render_template("home2.html")

@app.route('/deleteadmin',methods = ['POST', 'GET'])
def deleteadmin():
  if request.method == 'POST':

    con = sqlite3.connect('hskrental.db')
    id  = request.form['id']
    cursorObj = con.cursor()
    cur = con.cursor()
    cursorObj.execute("DELETE FROM admin where id="+id+"")
    con.commit()
  return render_template("home3.html")
@app.route('/resetcustpwd',methods = ['POST', 'GET'])
def resetcustpwd():
  if request.method == 'POST':


    con = sqlite3.connect('hskrental.db')
    newpwd = request.form['pwd']
    id  = request.form['id']
    cursorObj = con.cursor()
    cur = con.cursor()
    cursorObj.execute('UPDATE customer SET pwd = ? where id =?;',(newpwd,id))
    con.commit()

  return render_template("index.html")
@app.route('/resetadminpwd',methods = ['POST', 'GET'])
def resetadminpwd():
  if request.method == 'POST':


    con = sqlite3.connect('hskrental.db')
    newpwd = request.form['pwd']
    id  = request.form['id']
    cursorObj = con.cursor()
    cur = con.cursor()
    cursorObj.execute('UPDATE admin SET pwd = ? where id =?;',(newpwd,id))
    con.commit()

  return render_template("index.html")

# sandeep

@app.route('/listcars')
def listcars():
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  cursor.execute("SELECT * FROM vehicle")
  customerlist = cursor.fetchall()
  cursor.close()
  # print(customerlist)
  return render_template('manage_car.html', records=customerlist)

@app.route('/findallcars')
def findallcars():
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  cursor.execute("SELECT * FROM vehicle Where vstatus='AVAILABLE'")
  customerlist = cursor.fetchall()
  cursor.close()
  # print(customerlist)
  return render_template('allcar_list.html', records=customerlist)

@app.route('/findcar',methods=['POST'])
def findcar():
  if request.method == 'POST':
    con = sqlite3.connect('hskrental.db')
    cursor = con.cursor()
    pickdate = request.form['startDate2']
    dropdate = request.form['endDate2']
    location = request.form['location']
    uname = session['uname']
    print(session['uname'])
    # print(location)
    # print(pickdate)
    # print(dropdate)
    cursor.execute("SELECT * FROM vehicle WHERE location ='"+location+"' AND vstatus='AVAILABLE'")
    carlistbylocation = cursor.fetchall()

    if (len(carlistbylocation) > 0):
      return render_template('car_list.html', records=carlistbylocation,start_date=pickdate,end_date=dropdate,uname=uname)
    else:
      flash('No Cars Found, Please try again')
      return render_template("book_car.html",uname=session['uname'])
    # print(carlistbylocation)
  cursor.close()



@app.route("/addcarform",methods=['GET','POST'])

def addcarform():
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  model = request.form["model"]
  rno = request.form["rno"]
  seating = request.form["seating"]
  vtype = request.form["vtype"]
  priceperday = request.form["priceperday"]
  location = request.form["location"]
  vstatus = "available"

  cursor.execute("INSERT INTO vehicle (model,rno,seating,vtype,priceperday,vstatus,location) VALUES ('"+model+"', '"+rno+"', '"+seating+"','"+vtype+"','"+priceperday+"','"+vstatus+"','"+location+"')")
  con.commit()
  cursor.close()
  #flash("Adding New Car is successfull !!!")
  return redirect(url_for('listcars'))


@app.route('/delcar/<vid>', methods=['GET','POST'])
def delrec(vid):
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  # vid = str(request.form["vid"])
  cursor.execute("DELETE FROM vehicle WHERE vid = '"+vid+"'")
  con.commit()
  cursor.close()
  # flash("Car Successfully Deleted !!!")
  return redirect(url_for('listcars'))

@app.route('/updaterec', methods=['GET','POST'])
def updaterec():
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  vid = request.form["vid"]
  model = request.form["model"]
  rno = request.form["rno"]
  seating = request.form["seating"]
  vtype = request.form["vtype"]
  priceperday = request.form["priceperday"]
  location = request.form["location"]
  vstatus = request.form["vstatus"]

  cursor.execute("UPDATE vehicle SET model='"+model+"',rno='"+rno+"',seating='"+seating+"',vtype='"+vtype+"',priceperday='"+priceperday+"',vstatus='"+vstatus+"',location='"+location+"' WHERE vid='"+vid+"'")
  con.commit()
  cursor.close()
  #flash("Car updated successfully")
  return redirect(url_for('listcars'))

@app.route('/reservation',methods = ['GET','POST'])
def reservation():
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  # username = session['username']
  username = request.form["uname"]
  cursor.execute("SELECT fname, lname, email, phone, id FROM customer WHERE uname = '"+username+"'")
  custdata = cursor.fetchall()
  custdata_list = list(custdata)
  firstname = custdata_list[0][0]
  lastname = custdata_list[0][1]
  email = custdata_list[0][2]
  phone = custdata_list[0][3]
  userid = custdata_list[0][4]
  startdate = request.form["start_date"]
  enddate = request.form["end_date"]
  starttime = '10:00 AM'
  returntime = '10:00 AM'
  pickloc = request.form["location"]
  droploc = request.form["location"]
  price = request.form["priceperday"]
  carid = request.form["vid"]
  model = request.form["model"]

  print(startdate)
  print(enddate)
  print(starttime)
  print(returntime)
  print(pickloc)
  print(droploc)

  if (carid !="" and userid !=""):
      cursor.execute("UPDATE vehicle SET vstatus='booked' WHERE vid = '"+carid+"'")
      #cursor.execute("INSERT INTO booking (customerid,startdate,enddate,starttime,returntime,pickloc,droploc,carid) VALUES ('"+userid+"', '"+startdate+"','"+enddate+"','"+starttime+"','"+returntime+"','"+pickloc+"','"+dropLoc+"', '"+carid+"')")
      cursor.execute('INSERT INTO booking (customerid,startdate,enddate,starttime,returntime,pickloc,droploc,carid) VALUES(?,?,?,?,?,?,?,?);',(userid,startdate,enddate,starttime,returntime,pickloc,droploc,carid))
      con.commit()
      #cursor.execute("SELECT bookingid FROM booking where customerid = '"+userid+"' AND carid = '"+carid+"' AND pickloc = '"+pickloc+"'")
      cursor.execute("SELECT bookingid FROM booking where customerid = ? AND carid = ? AND pickloc = ?;",(userid,carid,pickloc))
      bookingid_list = cursor.fetchall()
      bookingid = bookingid_list[0][0]
      cursor.close()
      return render_template("/bookingConfirm.html",bookingid=bookingid,firstname=firstname,lastname=lastname,phone=phone,pickloc=pickloc,droploc=droploc,model=model,startdate=startdate,enddate=enddate,starttime=starttime,returntime=returntime,price=price,carid=carid)

  else:
      flash("Car is unavailable for booking at this time")
      return redirect('/findcar',uname=uname)

@app.route('/updatecustomer',methods = ['POST', 'GET'])
def updatecustomer():
  if request.method == 'POST':

    con = sqlite3.connect('hskrental.db')
    id = request.form['id']
    fname = request.form['fname']
    lname = request.form['lname']
    uname = request.form['uname']
    gender = request.form['gender']
    age  = request.form['age']
    email = request.form['email']
    phone  = request.form['phone']
    # pwd  = request.form['password']
    address=request.form['address']
    cursor = con.cursor()
    cursor.execute("UPDATE customer SET fname='"+fname+"',lname='"+lname+"',uname='"+uname+"',gender='"+gender+"',age='"+age+"',email='"+email+"',phone='"+phone+"',address='"+address+"' WHERE id='"+id+"'")
    con.commit()
    cursor.close()
    return redirect(url_for('listcustomer'))

@app.route('/updateadmin',methods = ['POST', 'GET'])
def updateadmin():
  if request.method == 'POST':
    con = sqlite3.connect('hskrental.db')
    id = request.form['id']
    fname = request.form['fname']
    lname = request.form['lname']
    uname = request.form['uname']
    gender = request.form['gender']
    age  = request.form['age']
    email = request.form['email']
    phone  = request.form['phone']
    # pwd  = request.form['password']
    #rpwd  = request.form['rpwd']
    address=request.form['address']
    cursor = con.cursor()
    cursor.execute("UPDATE admin SET fname='"+fname+"',lname='"+lname+"',uname='"+uname+"',gender='"+gender+"',age='"+age+"',email='"+email+"',phone='"+phone+"',address='"+address+"' WHERE id='"+id+"'")
    con.commit()
    cursor.close()
    return redirect(url_for('listadmin'))


@app.route('/deladmin/<id>', methods=['GET','POST'])
def deladmin(id):
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  cursor.execute("DELETE FROM admin WHERE id = '"+id+"'")
  con.commit()
  cursor.close()
  # flash("Car Successfully Deleted !!!")
  return redirect(url_for('listadmin'))

@app.route('/delcustomer/<id>', methods=['GET','POST'])
def delcustomer(id):
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  cursor.execute("DELETE FROM customer WHERE id = '"+id+"'")
  con.commit()
  cursor.close()
  # flash("Car Successfully Deleted !!!")
  return redirect(url_for('listcustomer'))

@app.route('/findallreservation')
def findallreservation():
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  cursor.execute("SELECT * FROM booking")
  customerlist = cursor.fetchall()
  cursor.close()
  print(customerlist)
  return render_template('manage_bookings.html', rows=customerlist)

@app.route('/findreservation',methods=['POST', 'GET'])
def findreservation():

  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  uname = session['uname']

  print(uname)

  cursor.execute("SELECT id FROM customer WHERE uname ='"+uname+"'")
  id_list = cursor.fetchall()
  con.commit()
  userid = id_list[0][0]

  print(userid)
  cursor.execute("SELECT * FROM booking WHERE customerid =?;" ,(userid,))
  carlistbylocation = cursor.fetchall()
  con.commit()

  print(carlistbylocation)
  cursor.close()

  return render_template('manage_user_bookings.html', rows=carlistbylocation)

@app.route('/delreservation/<bookingid>/<carid>', methods=['GET','POST'])
def delreservation(bookingid, carid):
  con = sqlite3.connect('hskrental.db')
  cursor = con.cursor()
  cursor.execute("DELETE FROM booking WHERE bookingid = '"+bookingid+"'")
  con.commit()
  cursor.execute("UPDATE vehicle SET vstatus='AVAILABLE' WHERE vid = '"+carid+"'")
  con.commit()
  cursor.close()
  if(session['logged_in_user'] == 'customer') :
    return redirect(url_for('findreservation'))

  return redirect(url_for('findallreservation'))

if __name__=='__main__':
  app.run(debug=True)
