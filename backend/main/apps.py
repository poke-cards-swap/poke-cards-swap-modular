import os

from flask import Flask
from flask_cors import CORS


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

    @app.route("/health", methods=["GET"])
    def health():  # pylint: disable=unused-variable
        return "", 204

    return app
