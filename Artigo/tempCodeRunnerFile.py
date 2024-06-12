from flask import Flask
from routes import artigo_blueprint
from models import db, init_app
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hQwAvEIT-uEz0xaigHxx8g'
file_path = os.path.abspath(os.path.join(os.getcwd(), 'database','artigo.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(artigo_blueprint)
init_app(app)

migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run(debug=True, port=5002)