from flask import Blueprint, request, render_template
from animeAPI import grab_data
views = Blueprint(__name__, "views")


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = grab_data()
        return render_template("result.html", title=data[0], synopsis=data[1], rating=data[2], episodes=data[3], status=data[4], year=data[5], image=data[6],  test="hello")

    return render_template("index.html")
