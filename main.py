import pymongo
from bson.objectid import ObjectId
from flask import Flask, redirect, url_for, request, render_template,flash,session

app = Flask(__name__)
app.secret_key = "jvcewihvdkc oeoerjfvgermcverio"


client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['tickets']
coll=mydb.collection

#
#
#
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
    showtime=request.form['time']
    print(name,num,showtime)
    user={
            'Name':name,
            'Mobile Number':num,
            'Showtiming':showtime
            # "$currentDate":{'booked at':True}
            }
    coll.insert_one(user)
    return "Booked"

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

# @app.route('/view all tickets')
# def view_all(time):
#     for i in coll.find({'showtime':time}):
#         print(i)

if __name__ == '__main__':
    app.run()
