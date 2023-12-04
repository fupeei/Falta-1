from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX

class Usuario:
    def __init__(self, datos):
        self.id_usuario = datos['id_usuario']
        self.nombre_usuario = datos['nombre_usuario']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.contraseña = datos['contraseña']
        self.localidad = datos['localidad']
        self.telefono = datos['telefono']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']


    @classmethod
    def crear_usuario(cls, datos):
        query = """
                INSERT INTO usuarios(nombre_usuario, apellido, email, contraseña, localidad, telefono)
                VALUES ( %(nombre_usuario)s, %(apellido)s, %(email)s, %(contraseña)s, %(localidad)s, %(telefono)s );
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
    
    @classmethod
    def obtener_uno(cls, datos):
        query = """
                SELECT *
                FROM usuarios
                WHERE email = %(email)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) == 0:
            return None
        return cls(resultado[0])
    
    @staticmethod
    def validar_registro(datos):
        es_valido = True
        if len(datos['nombre_usuario']) < 2:
            es_valido = False
            flash('Por favor escribe tu nombre.', 'error_nombre')
        if len(datos['apellido']) < 2:
            es_valido = False
            flash('Por favor escribe tu apellido.', 'error_apellido')
        if not EMAIL_REGEX.match(datos['email']):
            es_valido = False
            flash('Por favor ingresa un correo válido', 'error_email')
        if datos['password'] != datos['password_confirmar']:
            es_valido = False
            flash('Tus contraseñas no coinciden.', 'error_password')
        if len(datos['password']) < 1:
            es_valido = False
            flash('Por favor proporciona una contraseña.', 'error_password')
        if len(datos['localidad']) < 2:
            es_valido = False
            flash('Por favor coloca una localidad.', 'error_localidad')
        if len(datos['telefono']) < 9:
            es_valido = False
            flash('Por favor coloca tu número de telefono', 'error_telefono')
        return es_valido