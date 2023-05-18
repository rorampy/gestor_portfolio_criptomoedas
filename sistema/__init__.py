from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.secret_key = 'solutions intelis'
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# chamando as rotas em views
from sistema.views import index_view
from sistema.models import moedas_model