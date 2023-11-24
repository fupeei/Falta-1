from flask import render_template
from app_flask import app

@app.route("/")
def presentacion():
    return render_template("presentacion.html")