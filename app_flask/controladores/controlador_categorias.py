from flask import render_template, request, redirect, session
from app_flask.modelos.modelo_categorias import Categorias
from flask import Blueprint
from flask import jsonify

categorias_bp =Blueprint('categorias_bp', __name__)
@categorias_bp.route("/categorias")
def categorias():
    return render_template ("categorias.html")

@categorias_bp.route('/obtener_categoria_tipo/<int:id>', methods=['GET'])
def obtener_categorias_tipo(id):
    print(id)
    categorias = Categorias.obtener_categorias_tipo(id_tipo = id)
    categorias_final = [
        {
            "id_categoria": categoria.id_categoria,
            "nombre_categoria": categoria.nombre_categoria,
            "tipo_id_tipo": categoria.tipo_id_tipo
        }
        for categoria in categorias
    ]
    return jsonify(categorias_final)

@categorias_bp.route('/all_categorias', methods=['GET'])
def api_obtener_categorias():
    categorias = Categorias.obtener_todos()
    return jsonify(categorias)