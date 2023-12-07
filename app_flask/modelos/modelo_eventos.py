from flask import render_template, request, redirect, session
from app_flask.modelos.modelo_eventos import Eventos
from app_flask import app
from app_flask import BASE_DATOS
@app.route("/eventos")
def eventos():
    return render_template ("eventos.html")

@app.route("/mas/info")
def mas_info():
    return render_template ("mas_info.html")

@app.route('/formulario/evento', methods=['GET'])
def desplegar_crear_evento():
    if "id_usuario" not in session:
        return redirect('/')
    return render_template('crear_evento.html')


@app.route('/crear/evento', methods=['POST'])
def crear_evento():
    if Eventos.validar_eventos(request.form) == False:
        return redirect('/formulario/evento')
    nuevo_evento = {
        **request.form,
        "id_usuario": session['id_usuario']
    }
    Eventos.crear_uno(nuevo_evento)
    return redirect('/eventos')

@app.route('/eliminar/evento/<int:id>', methods=['POST'])
def eliminar_eventos(id):
    evento = {
        "id_evento": id
    }
    Eventos.elimina_uno(evento)
    return redirect('/categorias')

@app.route('/formulario/editar/evento/<int:id>', methods=['GET'])
def despliega_formulario_editar_evento(id):
    if "usuario_id" not in session:
        return redirect('/')
    datos = {
        "id_evento" : id
    }
    evento = Eventos.obtener_uno(datos)
    return render_template('formulario_editar_ evento.html',  evento =  evento)

@app.route('/unirse/evento/<int:id>', methods=['POST'])
def unirse_evento(id):
    datos_union = {
        "id_participante": None,
        "usuario_id_usuario": session['id_usuario'],
        "evento_id_evento": id
    }
    Eventos.unirse_a_evento(datos_union)
    return redirect('/categorias')

@app.route('/salir/evento/<int:id>', methods=['POST'])
def salir_evento(id):
    datos_salida = {
        "usuario_id_usuario": session['id_usuario'],
        "evento_id_evento": id
    }
    Eventos.salir_de_evento(datos_salida)
    return redirect('/categorias')

@app.route('/eventos/<int:id>', methods=['GET'])
def despliega_evento(id):
    datos = {
        "id_evento": id
    }
    evento = Eventos.obtener_uno(datos)
    return render_template('evento.html', evento = evento)


@app.route('/eventos/<int:id>/editar', methods=['POST'])
def editar_evento(id):
    if Eventos.validar_eventos(request.form) == False:
        return redirect('/eventos/' + str(id) + '/editar')
    Eventos.actualizar_uno(request.form)
    return redirect('/eventos/' + str(id))






