import json
from json.decoder import JSONDecodeError

from flask import Blueprint, request, jsonify

routes = Blueprint('prescriptions', __name__)

MALFORMED_REQUEST_ERROR = 1
PHYSICIAN_NOT_FOUND = 2
PATIENT_NOT_FOUND = 3
CLINIC_NOT_FOUND = 7
PRESCRIPTION_NOT_FOUND = 8

errors = {
    MALFORMED_REQUEST_ERROR: {"code": "01", "message": "malformed request"},
    PHYSICIAN_NOT_FOUND: {"code": "02", "message": "physician not found"},
    PATIENT_NOT_FOUND: {"code": "03", "message": "patient not found"},
    CLINIC_NOT_FOUND: {"code": "07", "message": "clinic not found"},
    PRESCRIPTION_NOT_FOUND: {"code": "08", "message": "prescription not found"}
}


def validate_prescription(presciption: dict):
    if not presciption.get('clinic'): return create_error(errors.get(CLINIC_NOT_FOUND))
    if not presciption.get('physician'): return create_error(errors.get(PHYSICIAN_NOT_FOUND))
    if not presciption.get('patient'): return create_error(errors.get(PATIENT_NOT_FOUND))
    if not presciption.get('text'): return create_error(errors.get(PRESCRIPTION_NOT_FOUND))
    return None


def create_error(error: dict) -> dict:
    return {"error": error}


@routes.route('/prescriptions', methods=['POST'])
def prescriptions():
    try:
        prescription = json.loads(request.data.decode('utf8'))
        error = validate_prescription(prescription)
        if error: return error, 428

    except JSONDecodeError:
        return create_error(errors.get(MALFORMED_REQUEST_ERROR)), 400

    return jsonify(status="Ok")
