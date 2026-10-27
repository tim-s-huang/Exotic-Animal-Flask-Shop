from flask import Flask
import os

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-change-me')
    
    from .pages import pages

    app.register_blueprint(pages, url_prefix='/')

    return app




