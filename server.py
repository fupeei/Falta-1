from app_flask import app
from app_flask.controladores.controlador_eventos import eventos_bp
from app_flask.controladores.controlador_categorias import categorias_bp
from app_flask.controladores.controlador_presentacion import presentacion_bp
from app_flask.controladores.controlador_inicio_y_registro import inicio_de_sesion_bp


app.register_blueprint(inicio_de_sesion_bp)
app.register_blueprint(presentacion_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(eventos_bp)
if __name__ == "__main__":
    app.run(debug=True)