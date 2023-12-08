from flask import render_template
from flask import Blueprint

presentacion_bp = Blueprint('presentacion_bp', __name__)

@presentacion_bp.route("/")
def presentacion():
    return render_template("presentacion.html")