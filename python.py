from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("logreg.html")






# FLASK
uri = "mongodb+srv://boab:1234@cluster0.d3aixga.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.user_database
coll = db.user


# Send a ping to confirm a successful connection

client.admin.command('ping')
print("Pinged your deployment. You successfully connected to MongoDB!")


# def bb():
    # name = input("Введите имя: ")
    # user_data = {"name": name}
    # coll.insert_one(user_data)

class arc():
    name = input("Введите имя: ")
    user_data = {"name": name}
    coll.insert_one(user_data)

    email = input("ur email")
    email_data = {"email": email}
    coll.insert_one(email_data)

if __name__ == "__main__":
    app.run(debug=True, port=8080)



