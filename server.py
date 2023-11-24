from app_flask import app
from app_flask.controladores import controlador_presentacion
from app_flask.controladores import controlador_inicio_y_registro
from app_flask.controladores import controlador_categorias
from app_flask.controladores import controlador_eventos



if __name__ == "__main__":
    app.run(debug=True)