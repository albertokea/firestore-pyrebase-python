import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDV5_pzNQYWlfddNEXOkNHcgKBwSckuJFM",
    'authDomain': "ops-activity-forms.firebaseapp.com",
    'projectId': "ops-activity-forms",
    'storageBucket': "ops-activity-forms.appspot.com",
    'messagingSenderId': "366847494297",
    'appId': "1:366847494297:web:90ab642d6db3aa16399008",
    'measurementId': "G-5GM9T4K9Q3",
    "databaseURL" : ""
}

firebase = pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
#auth=firebase.auth()
#storage=firebase.storage()

#Create
#Push to the db
data={'age':25, 'address':'New York', 'employed': True, 'name':'John Smith'}
db.child("employees").child("newYorkArea").push(data) #Every child is a new "folder" in the database

#Push with my own id
data={'age':25, 'address':'New York', 'employed': True, 'name':'John Smith'}
db.child("employees").child("newYorkArea").child("myOwnId").set(data) #Every child is a new "folder" in the database

#Update
db.child("people").child("dataId").update({'name':'Peter'})

#Values
people=db.child("people").get()
for person in people.each():
    print(person.val()) #Muestra los valores de los campos del registro
    print(person.key()) #Muestra el id

#Update only if name == Mark
people=db.child("people").get()
for person in people.each():
    if person.val()['name']=='Mark':
        db.child("people").child(person.key()).update({'name':'Jane'})
    
#Delete
#Delete with known id
db.child("people").child("person").remove()

#Delete with unknown id
people=db.child("people").get()
for person in people.each():
    if person.val()['name']=='Mark':
        db.child("people").child(person.key()).child("age").remove()

#Read
people=db.child("people").child("id").get()

#After setting some indexes in firebase console
people=db.child("people").order_by_child("name").equal_to("Jane").get() #Example 1
people=db.child("people").order_by_child("age").start_at(18).end_at(30).get() #Example 2
people=db.child("people").order_by_child("employed").equal_to(True).get() #Example 3
