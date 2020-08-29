import pymongo
from bson.objectid import ObjectId
from flask import Flask, redirect, url_for, request, render_template,flash,session

app = Flask(__name__)
app.secret_key = "jvcewihvdkc oeoerjfvgermcverio"


client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['tickets']
coll=mydb.collection
ind=mydb.indexes

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
        Tno=i[showtime]

    user={
            'Name':name,
            'Mobile Number':num,
            'Showtiming':showtime,
            'date':date,
            'Ticket No':Tno
            }

    if ((showtime=='12:00' and Tno<21) or (showtime=='17:00' and Tno<41) or (showtime=='19:00' and Tno<61) or (showtime=='21:00' and Tno<81) ):
        coll.insert_one(user)

        ind.update_one(
        {'id':'ind'},
        {"$set":{showtime:Tno+1}}
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
    for i in coll.find({'Showtiming':time}):
        list1.append(i)

    return render_template('view1.html',time=time,list1=list1)

@app.route('/delete1')
def delete1():
    return render_template('delete.html')

@app.route('/delete',methods=['GET','POST'])
def delete():
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
    for i in coll.find({'Ticket No':int(Tno)}):
        detail.append(i['Ticket No'])
        detail.append(i['Name'])
        detail.append(i['Mobile Number'])
        detail.append(i['Showtiming'])
        detail.append(i['date'])
    flash(detail)
    return render_template('details.html')


@app.route('/expired',methods=['GET','POST'])
def expired():
    coll.find({})

# @app.route('/view all tickets')
# def view_all(time):
#     for i in coll.find({'showtime':time}):
#         print(i)

if __name__ == '__main__':
    app.debug = True
    app.run()
