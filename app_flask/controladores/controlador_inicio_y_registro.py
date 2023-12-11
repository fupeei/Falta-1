from flask import render_template, session, redirect, request, flash
from app_flask.modelos.modelo_inicio_y_registro import Usuario
from app_flask import app
from flask import Blueprint
from flask_bcrypt import Bcrypt

inicio_de_sesion_bp = Blueprint('inicio_de_sesion_bp', __name__)

bcrypt = Bcrypt(app)

@inicio_de_sesion_bp.route("/inicio/sesion")
def inicio_de_sesion():
    return render_template ("inicio_sesion.html")


@inicio_de_sesion_bp.route('/procesa/registro', methods=['POST'])
def procesa_registro():
    if Usuario.validar_registro(request.form) == False:
        return redirect('/')
    password_encriptado = bcrypt.generate_password_hash(request.form['password'])
    nuevo_usuario = {
        **request.form,
        'contraseña' : password_encriptado
    }
    id_usuario = Usuario.crear_usuario(nuevo_usuario)
    session['id_usuario'] = id_usuario
    session['nombre_usuario'] = nuevo_usuario['nombre_usuario']
    session['apellido'] = nuevo_usuario['apellido']
    
    return redirect('/categorias')

@inicio_de_sesion_bp.route('/procesa/login', methods=['POST'])
def procesa_login():
    usuario_login = Usuario.obtener_uno(request.form)
    if usuario_login == None:
        flash('Este correo no existe', 'error_login')
        return redirect('/')
    if not bcrypt.check_password_hash(usuario_login.contraseña, request.form['password']):
        flash('Credenciales incorrectas', 'error_login')
        return redirect('/')
    session['id_usuario'] = usuario_login.id_usuario
    session['nombre'] = usuario_login.nombre_usuario
    session['apellido'] = usuario_login.apellido
    session['email'] = usuario_login.email
    session['localidad'] = usuario_login.localidad
    session['telefono'] = usuario_login.telefono
    return redirect('/categorias')
   

@inicio_de_sesion_bp.route('/procesa/logout', methods=['POST'])
def procesa_logout():
    session.clear()
    return redirect('/')

@inicio_de_sesion_bp.route("/registro")
def registrarse():
    return render_template ("registrarse.html")


