from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    from models import db
    db.init_app(app)

    from auth.auth import oauth, auth
    app.register_blueprint(auth, url_prefix="/auth")
    oauth.init_app(app)

    return app
