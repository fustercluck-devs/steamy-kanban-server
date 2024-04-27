from flask import Flask

def create_app():
    app = Flask(__name__)
    return app
    
def register_routes(app):
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
def setup_app():
    app = create_app()
    register_routes(app)
    return app