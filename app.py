from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import environ
from db import conexion
from flask_restful import Api

from utils.enviar_correo import enviar_correo_adjuntos
from controllers.usuario_controller import RegistroController
from controllers.categoria_controller import ImagenesController
load_dotenv()

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['UPLOAD_FOLDER'] =  '/imagenes'
conexion.init_app(app)

api = Api(app)

Migrate(app, conexion)

@app.route('/prueba')
def enviar_correo_prueba():
    #aqui se coloca el correo del destinatario
    enviar_correo_adjuntos('wilson_dani1@hotmail.com', 'Correo con imagenes')

    return {
        'message': 'Correo enviado exitosamente'
    }


api.add_resource(RegistroController, '/registro')
api.add_resource(ImagenesController, '/imagenes') #, '/imagenes/<nombre>'


if __name__ == '__main__':
     app.run(debug=True)