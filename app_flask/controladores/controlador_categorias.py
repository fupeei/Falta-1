from flask import render_template
from app_flask import app

@app.route("/categorias")
def categorias():
    return render_template ("categorias.html")