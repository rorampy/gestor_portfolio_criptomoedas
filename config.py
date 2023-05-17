
DEBUG = True

USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DB = 'gestor_portfolio_cripto'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_NOTIFICATIONS = True