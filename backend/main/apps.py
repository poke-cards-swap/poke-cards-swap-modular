# pylint: disable=import-outside-toplevel,too-many-locals
import os

from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix


def create_cards_app():
    app = Flask("gateway", instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    CORS(app)

    app.config.from_pyfile("config.py", silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from gateway import (
        root_blueprint,
    )

    app.register_blueprint(root_blueprint)

    @app.route("/health", methods=["GET"])
    def health():  # pylint: disable=unused-variable
        return "", 204

    return app


def create_cards_app_with_proxy():
    app = create_cards_app()

    return ProxyFix(app, x_for=1, x_host=1)
