import pymongo
from bson.objectid import ObjectId
from flask import Flask, redirect, url_for, request, render_template,flash,session
import datetime
import pytz

app = Flask(__name__)
app.secret_key = "jvcewihvdkc oeoerjfvgermcverio"


client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['tickets']
coll=mydb.collection
ind=mydb.indexes

## this function will mark tickets as expired if there is a difference of 8 hrs  & will delete it automatically
def expired():
    for i in coll.find({}):
        Tno=i['Ticket No']
        str1=(i['date'])+' '+(i['Showtiming'])
        tz = pytz.timezone('Asia/Kolkata')

        a= datetime.datetime.strptime(str1, '%Y-%m-%d %H:%M')
        a= a.replace(tzinfo=tz)
        b= datetime.datetime.now(tz)
        if (b>a):
            time_elapsed = b - a
            str2=str(time_elapsed)
            if (len(str2.split(':')[0])>2 ):
                coll.delete_one({'Ticket No':int(Tno)})
            else:
                str2=str2.split(':')[0]
                if (int(str2)>7):
                    coll.delete_one({'Ticket No':int(Tno)})


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/book')
def book():
    return render_template('booktickets.html')

@app.route('/bookticket',methods=['GET','POST'])
def bookticket():

    name=request.form['fname']
    num=request.form['Mnum']
    date=request.form['date']
    showtime=request.form['time']

    for i in ind.find({}):
        Tno=i['num']

    user={
            'Ticket No':Tno,
            'Name':name,
            'Mobile Number':num,
            'Showtiming':showtime,
            'date':date
            }
    expired()
## using index database to generate unique ticket no.
    c=0
    for i in coll.find({'Showtiming':showtime}):
        c+=1
## will prevent ticket booking if already 20 tickets are booked for that show
    if (c<21):
        coll.insert_one(user)

        ind.update_one(
        {'id':'ind'},
        {"$set":{'num':Tno+1}}
        )
        flash('Ticket Booked')
    else :
        flash('House Full')
    return render_template('booktickets.html')

@app.route('/update1')
def update1():
    return render_template('update.html')

@app.route('/update',methods=['GET','POST'])
def update():
## will recieve ticket no. and showtime from form & update timings accordingly
    Tno=request.form['Tno']
    time=request.form['time']
    coll.update_one(
    {'Ticket No':int(Tno)},
    {"$set":{'Showtiming':time}}
    )
    flash("Timing Changed to "+ time)
    return render_template('update.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/viewall',methods=['GET','POST'])
def viewall():
    time=request.form['time']
    list1=[]
## searching through database with enetered showtime tickets and displaying them
    for i in coll.find({'Showtiming':time}):
        list1.append((i['Ticket No'],i['Name']))

    l=len(list1)
    print(list1)
    return render_template('view1.html',l=l,time=time,list1=list1)

@app.route('/delete1')
def delete1():
    return render_template('delete.html')

@app.route('/delete',methods=['GET','POST'])
def delete():
## searching through database with enetered ticket no. and deleting it

    Tno=request.form['Tno']
    coll.delete_one({'Ticket No':int(Tno)})
    flash('Deleted!')
    return render_template('delete.html')

@app.route('/details1')
def details1():
    return render_template('details.html')

@app.route('/details',methods=['GET','POST'])
def details():
    Tno=request.form['Tno']
    detail=[]
    ##displaying user data in list form after searching through database with enetered ticket no.

    for i in coll.find({'Ticket No':int(Tno)}):
        detail.append(i['Ticket No'])
        detail.append(i['Name'])
        detail.append(i['Mobile Number'])
        detail.append(i['Showtiming'])
        detail.append(i['date'])
    flash(detail)
    return render_template('details.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
