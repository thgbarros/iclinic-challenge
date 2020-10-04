from flask import Blueprint, jsonify

routes = Blueprint('prescriptions', __name__)


@routes.route('/prescriptions', methods=['POST'])
def patient():
    return jsonify(status="Ok")
