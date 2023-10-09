# import dependencies
from flask import Flask, redirect, render_template, request, url_for
import json

# import helper files
# constants
FLASK_APP_PATH = "/IMDB-Query/"

# helper functions

# flask app 
flask_app = Flask(__name__, template_folder='website/templates', static_url_path='/website/static')
flask_app.config.from_file("website/secrets.json", load=json.load)  

@flask_app.route("/", methods=["GET"])
def index():
    return render_template("index.html") # Jinja2's render_template instead of html hard code

@flask_app.route("/page1", methods=["GET", "POST"])
def page1():
    if request.method == "POST":
            q1_response = request.form.get("q1")
            q2_response = request.form.get("q2")
            q3_response = request.form.get("q3")
            print(f"\n Responses: {q1_response}, {q2_response}, {q3_response} \n")

    return render_template("page1.html")


if __name__ == "__main__":
    flask_app.run(debug = True)