from flask import render_template, request, redirect, session
from app_flask.modelos.modelo_eventos import Eventos
from flask import Blueprint

perfil_bp = Blueprint('perfil_bp', __name__)

@perfil_bp.route("/perfil")
def desplegar_perfil():
    if "id_usuario" not in session:
        return redirect('/')
    datos = {
        "id" : session['id_usuario']
    } 
    lista_eventos = Eventos.obtener_eventos_unido_usuario(datos)
    return render_template ("perfil.html", lista_eventos= lista_eventos)