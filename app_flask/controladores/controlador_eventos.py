from flask import render_template
from app_flask import app

@app.route("/eventos")
def eventos():
    return render_template ("eventos.html")

@app.route("/mas/info")
def mas_info():
    return render_template ("mas_info.html")