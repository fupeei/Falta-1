from flask import render_template
from app_flask import app

@app.route("/inicio/sesion")
def inicio_de_sesion():
    return render_template ("inicio_sesion.html")

@app.route("/registro")
def registrarse():
    return render_template ("registrarse.html")
