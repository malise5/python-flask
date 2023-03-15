from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate

from models import db, Production

#show the flask where the current app is running
app = Flask(__name__)

#Generates and connects to the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.before_request
def runs_before_request():
    current_user = {"user_id": 1, "username": "admin"}
    print(current_user)


#Routes
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#DYNAMIC ROUTES
@app.route('/productions/<string:title>')
def production(title):
    # production = Production.query.filter_by(title=title).first()
    production = Production.query.filter(Production.title == title).first()

    #build the response 
    production_response = {
        "title": production.title,
        "genre": production.genre,
        "director": production.director,
        "description": production.description,
        "image": production.image,
        "budget": production.budget,
        "ongoing": production.ongoing
    }

    #convert the response to json
    response = make_response(
        jsonify(production_response), 
        200
    )
    return response

    #
# @app.route('/context')
# def context():
    
    


