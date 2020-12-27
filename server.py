import calendar
import json
from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        month = request.form["month"]
        date = request.form["date"]
        info = {"email": email, "month": int(month), "date": int(date)}
        flash("you will be emailed when the date becomes available!", "info")
        # the flash doesn't work at all! All good though because this will be entirely reworked
        update_web_form_data(info)
    return render_template("base.html")

def update_web_form_data(json_data):
    with open('wb_interactions/web_form_data.json') as json_file:
        web_form_data = json.load(json_file)
        web_form_data.append(json_data)

    with open('wb_interactions/web_form_data.json', 'w') as outfile:
        json.dump(web_form_data, outfile)

if __name__ == "__main__":
    app.run()