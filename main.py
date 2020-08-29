import pymongo


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





book_ticket()
