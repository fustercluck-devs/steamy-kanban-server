from flask import Flask, request
import requests


def create_app():
    app = Flask(__name__)
    return app


def register_routes(app):
    @app.route("/")
    def hello():
        name = request.args.get("name", default="World")
        return f"Hello, {name}!"

    @app.route("/v1/steamfacade/appdetails")
    def retrieve_data_for_app_id():
        app_id = request.args.get("appids")
        resp = requests.get(
            f"https://store.steampowered.com/api/appdetails?appids={app_id}"
        )
        return resp.json()


def setup_app():
    app = create_app()
    register_routes(app)
    return app
