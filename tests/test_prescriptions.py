def test_prescriptions(client):
    response = client.post('/prescriptions')
    assert response.status_code == 200
