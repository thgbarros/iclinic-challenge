import json


def test_json_none(client):
    response = client.post('/prescriptions')
    error = json.loads(response.data)
    assert error.get("error") is not None
    error = error.get("error")

    assert error.get("code") == "01"
    assert error.get("message") == "malformed request"
    assert response.status_code == 400


def test_without_prescription(client):
    response = client.post('/prescriptions', data=json.dumps({
        "clinic": {"id": 1},
        "physician": {"id": 1},
        "patient": {"id": 1},
    }))

    error = json.loads(response.data)
    assert error.get("error") is not None
    error = error.get("error")

    assert error.get("code") == "08"
    assert error.get("message") == "prescription not found"
    assert response.status_code == 428


def test_without_physician(client):
    response = client.post('/prescriptions', data=json.dumps({
        "clinic": {"id": 1},
        "patient": {"id": 1},
        "text": "Dipirona 1x ao dia"
    }))

    error = json.loads(response.data)
    assert error.get("error") is not None
    error = error.get("error")

    assert error.get("code") == "02"
    assert error.get("message") == "physician not found"
    assert response.status_code == 428


def test_without_patient(client):
    response = client.post('/prescriptions', data=json.dumps({
        "clinic": {"id": 1},
        "physician": {"id": 1},
        "text": "Dipirona 1x ao dia"
    }))

    error = json.loads(response.data)
    assert error.get("error") is not None
    error = error.get("error")

    assert error.get("code") == "03"
    assert error.get("message") == "patient not found"
    assert response.status_code == 428


def test_without_clinic(client):
    response = client.post('/prescriptions', data=json.dumps({
        "physician": {"id": 1},
        "patient": {"id": 1},
        "text": "Dipirona 1x ao dia"
    }))

    error = json.loads(response.data)
    assert error.get("error") is not None
    error = error.get("error")

    assert error.get("code") == "07"
    assert error.get("message") == "clinic not found"
    assert response.status_code == 428


def test_prescriptions_valid_json(client):
    response = client.post('/prescriptions', data=json.dumps({
        "clinic": {"id": 1},
        "physician": {"id": 1},
        "patient": {"id": 1},
        "text": "Dipirona 1x ao dia"
    }))
    assert response.status_code == 200

