from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, render_template

app = Flask(__name__)
html = open("logreg.html").read()
@app.route("/")
def hello():
    return html


# FLASK
uri = "mongodb+srv://boab:1234@cluster0.d3aixga.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.user_database
coll = db.user

name = input("Введите имя: ")
user_data = {"name": name}
coll.insert_one(user_data)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# def bb():
    # name = input("Введите имя: ")
    # user_data = {"name": name}
    # coll.insert_one(user_data)

if  __name__ == '__main__':
    app.run(debug=True)


