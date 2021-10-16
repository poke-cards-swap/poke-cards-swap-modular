from flask import Blueprint


root_blueprint = Blueprint("root", __name__)


@root_blueprint.route("/", methods=["GET"])
def index():
    return 200, "OK"
