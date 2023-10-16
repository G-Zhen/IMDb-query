# import dependencies
from flask import Flask, redirect, render_template, request, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from flask_mysqldb import MySQL
import json
import mysql.connector
# import helper files
import models

# constants
FLASK_APP_PATH = "/IMDb-Query/"

# flask app configurations
flask_app = Flask(__name__, template_folder='website/templates', static_url_path='/website/static')
flask_app.config.from_file("website/secrets.json", load=json.load)  

# Database configuration
db_config = flask_app.config.get("database")
db_host = db_config.get("database_HOST")
db_user = db_config.get("database_USER")
db_password = db_config.get("database_PASSWORD")
db_database = db_config.get("database_DB")

# Initialize SQLAlchemy
models.db.init_app(flask_app)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_user}:{db_password}@{db_host}/{db_database}"

# Create a MySQL connection
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# helper functions
def execute_sql_script(script_path, database_uri):
    with open(script_path, 'r') as script_file:
        sql_script = script_file.read()
    
    engine = create_engine(database_uri)
    connection = engine.connect()
    
    try:
        connection.execute(sql_script)
    finally:
        connection.close()

def test_DB_connection() -> str:
    """Tests database connection. Returns HTML to render on the page."""
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return "<h1>Database successfully connected.</h1>"
    except Exception as e:
        errorMsg = "<p>Error: " + str(e) + "</p>"
        header = "<h1>Database connection failed</h1>"
        return header + errorMsg

def create_app_User()-> (models.User):
    """Create a new user for users table in database"""
    # create user and insert ID
    user = models.User()
    db.session.add(user)
    db.session.commit()
    return user

def get_app_user(userid)-> models.User:
    """Get a user from the users table in database"""
    user = models.User.query.get(userid)
    return user


def insert_pg1_response(q1r, q2r, q3r, user) -> None:
    """Insert the page 1 responses to the database"""
    response = models.Page1Response(user=user, q1=q1r, q2=q2r, q3=q3r)
    db.session.add(response)
    db.session.commit()

# app functions
@flask_app.route("/", methods=["GET"])
def index():
    '''Home page'''
    user, userID = create_app_User()
    return render_template("index.html") # Jinja2's render_template uses an html file instead of hard coding html in python files

@flask_app.route("/page1", methods=["GET", "POST"])
def page1():
    # get the html textbox responses
    if request.method == "POST":
        q1_response = request.form.get("q1")
        q2_response = request.form.get("q2")
        q3_response = request.form.get("q3")
        print(f"\n Responses: {q1_response}, {q2_response}, {q3_response} \n")

        # send responses to database
        user = get_app_user()
        insert_pg1_response(user, q1_response, q2_response, q3_response)

    return render_template("page1.html")


if __name__ == "__main__":
    # Execute the SQL script to create the database and tables
    execute_sql_script('website/models.sql', flask_app.config['SQLALCHEMY_DATABASE_URI'])
    
    # run app
    flask_app.run(debug = True)
    