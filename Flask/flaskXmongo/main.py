from flask import Flask,render_template,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
# app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///test.db'


@app.route('/')
def index():
        mongo.db.inventory.insert_one({"a":1})
        return render_template('index.html')
    
if __name__=='__main__':
    app.run(debug=True)