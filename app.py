from api.get_api import get_availability_by_pin
from flask import Flask, render_template, request, url_for, redirect, flash
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)


@app.route("/", methods=["GET", "POST"])
def index():
    errors = []
    pincode = ""
    data = {}
    if request.method == "POST":
        print("Inside")
        pincode = request.form["pincode"]
        # date = request.form["date"]

    if not pincode:
        flash("Pincode is required !")
    else:
        try:
            res = get_availability_by_pin(pincode)
            if res.status_code == 200:
                fetched_data = res.json()
                data = fetched_data["sessions"]
            else:
                flash(
                    "Slot availability data could not fetched, please try again in some time !"
                )
        except Exception:
            errors.append("Unable to get vaccine data")
    return render_template("index.html", errors=errors, data=data)
