from flask import Blueprint, render_template, redirect, request, flash, url_for


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html.j2")

