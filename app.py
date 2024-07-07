from flaskr import create_app
from flask import render_template
from pymongo import MongoClient
from bson import ObjectId

app = create_app()

client = MongoClient('mongodb://localhost:27017/')
db = client['proto']
users = db['users']

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Simple python flask webapp'

@app.route('/')
def home():
    data = {
        'user_count': users.count_documents({}),
    }
    return render_template('home.html', data=data)

app.run(debug=True)