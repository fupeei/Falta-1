from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS

class Categorias:
    def __init__(self, datos):
        self.id_categoria = datos['id_categoria']
        self.nombre_categoria = datos['nombre_categoria']
        self.tipo_id_tipo = datos['tipo_id_tipo']
        
    @classmethod
    def obtener_categoria(cls):
        query = """
                SELECT *
                FROM categorias;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        categorias = []
        for categoria in resultado:
            categorias.append(cls(categoria))
        return categorias
    
    @classmethod
    def obtener_categorias_tipo(cls, id_tipo):
        query = """
                SELECT *
                FROM categorias WHERE tipo_id_tipo = %(tipo_id_tipo)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, {'tipo_id_tipo':id_tipo})
        categorias = []
        for categoria in resultado:
            categorias.append(cls(categoria))
        return categorias