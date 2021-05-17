import urllib
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
#auth=firebase.auth()
storage=firebase.storage()

#Storage
filename=input("Enter the name of the file you want to upload")
cloudfilename=input("Enter the name of the file on the cloud") #folder/route/file.extension
storage.child(cloudfilename).put(filename)

print(storage.child(cloudfilename).get_url(None)) #We get the url of the uploaded file

#Download
cloudfilename=input("Enter the name of the file you want to download")
storage.child(cloudfilename).download("path", "file.extension") # file.extension is name when downloaded

#Download a file automatically
storage.child("file.extension").download("path", "file.extension")

#Reading txt or json file as string
cloudfilename=input("Enter the name of the file you want to see")
url=storage.child(cloudfilename).get_url(None)
f=urllib.request.urlopen(url).read()
print(f)