from flask import render_template, request, redirect, session,jsonify
from app_flask.modelos.modelo_eventos import Eventos
from app_flask import app

@app.route("/eventos")
def eventos():
    return rensder_template ("eventos.html")

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
    banda = {
        "id_evento": id
    }
    Evento.elimina_uno(evento)
    return redirect('/categorias')

@app.route('/formulario/editar/evento/<int:id>', methods=['GET'])
def despliega_formulario_editar_evento(id):
    if "usuario_id" not in session:
        return redirect('/')
    datos = {
        "id_evento" : id
    }
    evento = Evento.obtener_uno(datos)
    return render_template('formulario_editar_ evento.html',  evento =  evento)

@app.route('/categorias/<int:id>')
def get_categorias(id):
    # aca va la logica de buscar las categorias en la base de datos, con la id que le pasamos
    data = {
        "id" : id
    }
    lista_categorias = Eventos.obtener_todos_api(data)
    return (jsonify(lista_categorias))
