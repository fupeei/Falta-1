from app_flask.config.mysqlconnection import connectToMySQL
from app_flask.modelos import modelo_inicio_y_registro
from flask import flash
from app_flask import BASE_DATOS

class Eventos:
    def __init__(self, datos):
        self.id_evento = datos['id_evento']
        self.tipo = datos['tipo']
        self.nombre_evento = datos['nombre_evento']
        self.participantes = datos['participantes']
        self.descrpcion = datos['descripcion']
        self.ubicacion = datos['ubicacion']
        self.fecha = datos['fecha']
        self.hora = datos['hora']
        self.categoria_id_categoria = datos['categoria_id_categoria']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        

    @classmethod
    def crear_uno(cls, datos):
        query = """
                INSERT INTO eventos(tipo, nombre_evento, participantes, descripcion, ubicacion, fecha, hora, categoria_id_categoria)
                VALUES (%(tipo)s, %(nombre_evento)s, %(participantes)s, %(descripcion)s, %(ubicacion)s, %(fecha)s, %(hora)s, %(categoria_id_categoria)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
    
    @classmethod
    def elimina_uno(cls, datos): #Eliminar evento 
        query = """
                DELETE FROM eventos
                WHERE id_evento = %(id_evento)s;
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
    
    @classmethod
    def actualizar_uno(cls, datos):
        query = """
                UPDATE eventos
                SET tipo = %(tipo)s, nombre_evento = %(nombre_evento)s, participantes = %(participantes)s, descripcion = %(descripcion)s,
                ubicacion = %(ubicacion)s, fecha = %(fecha)s, hora = %(hora)s, categoria_id_categoria = %(categoria_id_categoria)s
                WHERE id_evento = %(id_evento)s;
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
    
    @classmethod
    def unirse_a_evento(cls, datos_union):
        query = """
                INSERT INTO participantes(id_participante, usuario_id_usuario, evento_id_evento)
                VALUES (%(id_participante)s, %(usuario_id_usuario)s, %(evento_id_evento)s);
                """
        connectToMySQL(BASE_DATOS).query_db(query, datos_union) 
        
    @classmethod
    def salir_de_evento(cls, datos_salida):
        query = """
                DELETE FROM participantes
                WHERE usuario_id_usuario = %(usuario_id_usuario)s AND evento_id_evento = %(evento_id_evento)s;
                """
        connectToMySQL(BASE_DATOS).query_db(query, datos_salida)
        
    @classmethod
    def obtener_todos_api(cls,datos):
        query = """
                SELECT * FROM categorias
                WHERE tipo_id_tipo = %(id)s;
                """
        connectToMySQL(BASE_DATOS).query_db(query,datos)
      


    @staticmethod
    def validar_bandas(datos):
        es_valido = True
        if len(datos['tipo']) < 3:
            flash('Por favor proporciona bien el nombre del evento.', 'error_banda')
            es_valido = False
        if len(datos['nombre_evento']) < 3:
            flash('Por favor proporciona el nombre_evento del evento.', 'error_nombre_evento')
            es_valido = False
        if  len(datos['participantes']) < 3:
            flash('Por favor proporciona la participantes del evento.', 'error_participantes')
            es_valido = False
        if  len(datos['descripcion']) < 3:
            flash('Por favor proporciona la descripcion del evento.', 'error_descripcion')
            es_valido = False
        if  len(datos['ubicacion']) < 3:
            flash('Por favor proporciona la ubicacion del evento.', 'error_ubicacion')
            es_valido = False
        if  len(datos['fecha']) < 3:
            flash('Por favor proporciona la fecha del evento.', 'error_fecha')
            es_valido = False
        if  len(datos['hora']) < 3:
            flash('Por favor proporciona la hora del evento.', 'error_hora')
            es_valido = False
        if  len(datos['categoria_id_categoria']) < 3:
            flash('Por favor proporciona la categoria del evento.', 'error_categoria_id_categoria')
            es_valido = False
        return es_valido
    