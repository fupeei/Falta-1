from flask import render_template
from app_flask import app

@app.route("/crear_evento")
def crearevento():
    return render_template("crear_evento.html")