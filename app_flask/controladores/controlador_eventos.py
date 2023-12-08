from flask import render_template, request, redirect, session
from app_flask.modelos.modelo_eventos import Eventos
from flask import Blueprint
from flask import jsonify

eventos_bp =Blueprint('eventos_bp', __name__) 

# Removed unused import statement
@eventos_bp.route("/crear_evento")
def crearevento():
    return render_template("crear_evento.html")
@eventos_bp.route("/eventos")
def eventos():
    return render_template("eventos.html")

@eventos_bp.route("/mas/info")
def mas_info():
    return render_template("mas_info.html")

@eventos_bp.route('/formulario/evento', methods=['GET'])
def desplegar_crear_evento():
    if "id_usuario" not in session:
        return redirect('/')
    return render_template('crear_evento.html')


@eventos_bp.route('/eliminar/evento/<int:id>', methods=['POST'])
def eliminar_eventos(id):
    evento = {
        "id_evento": id
    }
    Eventos.elimina_uno(evento)
    return redirect('/categorias')

@eventos_bp.route('/formulario/editar/evento/<int:id>', methods=['GET'])
def despliega_formulario_editar_evento(id):
    if "usuario_id" not in session:
        return redirect('/')
    datos = {
        "id_evento" : id
    }
    evento = Eventos.obtener_uno(datos)
    return render_template('formulario_editar_ evento.html',  evento =  evento)

@eventos_bp.route('/unirse/evento/<int:id>', methods=['POST'])
def unirse_evento(id):
    datos_union = {
        "id_participante": None,
        "usuario_id_usuario": session['id_usuario'],
        "evento_id_evento": id
    }
    Eventos.unirse_a_evento(datos_union)
    return redirect('/categorias')

@eventos_bp.route('/salir/evento/<int:id>', methods=['POST'])
def salir_evento(id):
    datos_salida = {
        "usuario_id_usuario": session['id_usuario'],
        "evento_id_evento": id
    }
    Eventos.salir_de_evento(datos_salida)
    return redirect('/categorias')

@eventos_bp.route('/eventos/<int:id>', methods=['GET'])
def despliega_evento(id):
    datos = {
        "id_evento": id
    }
    evento = Eventos.obtener_uno(datos)
    return render_template('evento.html', evento = evento)


@eventos_bp.route('/eventos/<int:id>/editar', methods=['POST'])
def editar_evento(id):
    if Eventos.validar_eventos(request.form) == False:
        return redirect('/eventos/' + str(id) + '/editar')
    Eventos.actualizar_uno(request.form)
    return redirect('/eventos/' + str(id))
