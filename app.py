# import dependencies
from flask import Flask, redirect, render_template, request, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Page1Response
import json

# import helper files
# constants
FLASK_APP_PATH = "/IMDB-Query/"
DB_NAME = "imdb_DB.db"

# flask app config
flask_app = Flask(__name__, template_folder='website/templates', static_url_path='/website/static')

#loading JSON
with open("website/secrets.json", "r") as config_file:
    config_data = json.load(config_file)
    print("json: ", config_data)

# DATABASE 
flask_app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(flask_app) # Initialize flask app with SQLAlchemy

# HELPER FUNCTIONS

# FLASK FUNCTIONS
@flask_app.route("/", methods=["GET"])
def index():
    """Home page"""
    userID = 1234
    return render_template("index.html", userID=userID) # Jinja2's render_template instead of html hard code

@flask_app.route("/page1", methods=["GET", "POST"])
def page1():
    if request.method == "POST":
        q1_response = request.form.get("q1")
        q2_response = request.form.get("q2")
        q3_response = request.form.get("q3")
        print(f"\n Responses: {q1_response}, {q2_response}, {q3_response} \n")

        try:
            # Create a new user 
            newUser = User()  # Create a new User object
            db.session.add(newUser)  # Add the user to the db

            # Create a new Page1Response object
            response = Page1Response(
                q1=q1_response,
                q2=q2_response,
                q3=q3_response,
                user=newUser  # Associate the response with the user
            )

            db.session.add(response)  # Add the response to the db

            # Commit the changes to the database
            db.session.commit()

        except Exception as e:
            error = "<h1>Database error: </h1>" + "<p>" + str(e) + "</p>"
            return error

    return render_template("page1.html")


if __name__ == "__main__":
    # create tables from models if they don't exist
    with flask_app.app_context():
        db.create_all()
        print("database created")

    flask_app.run(debug = True)