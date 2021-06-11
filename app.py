from api.get_api import get_availability_by_pin, get_vaccine_slots
from flask import Flask, render_template, request, url_for, redirect, flash
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)


@app.route("/", methods=["GET", "POST"])
def index():
    msg_str = ""
    pincode = ""
    vaccine_slots_data = {}
    if request.method == "POST":
        pincode = request.form["pincode"]
        if not pincode:
            flash("Pincode is required !")
        else:
            vaccine_slots_data, msg_str = get_vaccine_slots(pincode)
    return render_template(
        "index.html",
        errors=msg_str,
        data=vaccine_slots_data,
        len=len(vaccine_slots_data),
    )
