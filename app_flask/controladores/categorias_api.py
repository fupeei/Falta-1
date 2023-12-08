from flask import jsonify
from app_flask.modelos.modelo_eventos import Eventos
from app_flask import app

@app.route('/api/categorias/<int:id>)')
def api_obtener_categorias(id):
    data = {
        "tipo_id_tipo" : id
    }
    lista_categorias = Eventos.obtener_todos_api(data)
    return (jsonify(lista_categorias))