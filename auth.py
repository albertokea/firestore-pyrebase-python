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

#db=firebase.database()
auth=firebase.auth()
#storage=firebase.storage()

#Authentication
#Login
email=input('Enter your email')
password=input('Enter your password')
try:
    auth.sign_in_with_email_and_password(email, password)
    print("Succesfully sign in!")
except:
    print("Invalid user or password. Try again")

#Sign up
email=input('Enter your email')
password=input('Enter your password')
confirmpass=input("Confirm password")
if password == confirmpass:
    try:
        auth.create_user_with_email_and_password(email, password)
        print("Success!!")
    except:
        print("Email already exist")
