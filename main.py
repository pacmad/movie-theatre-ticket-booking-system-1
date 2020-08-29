import pymongo
from bson.objectid import ObjectId
from flask import Flask, redirect, url_for, request, render_template,flash,session

app = Flask(__name__)
app.secret_key = "jvcewihvdkc oeoerjfvgermcverio"


client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['tickets']
coll=mydb.collection
ind=mydb.indexes
#
# def time():
#     for i in coll.find():
#         print(i)
#         id=i['_id']
#         print(id)
#         print(id.generation_time)
#
# book_ticket()
# view_all("19:30")


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
