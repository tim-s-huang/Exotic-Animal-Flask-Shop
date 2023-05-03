from flask import Flask

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET KEY'] = 'I love cardiff university'
    
    from .pages import pages

    app.register_blueprint(pages, url_prefix='/')

    return app




