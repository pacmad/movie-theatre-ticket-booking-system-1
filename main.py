import pymongo
from bson.objectid import ObjectId


client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb=client['tickets']
coll=mydb.collection

def book_ticket():
    name=input('name ')
    num=input('Number ')
    showtime=input('time ')

    test={
        'name':name,
        'number':num,
        'showtime':showtime,
        # "$currentDate":{'booked at':True}
        }
    coll.insert_one(test)



def view_all(time):
    for i in coll.find({'showtime':time}):
        print(i)

def time():
    for i in coll.find():
        print(i)
        id=i['_id']
        print(id)
        print(id.generation_time)
    
book_ticket()
view_all("19:30")

time()
