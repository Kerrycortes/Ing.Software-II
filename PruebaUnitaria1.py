from backend import app
import json

def test_get_all():
    tester = app.test_client()
    response = tester.get('/productos')
    assert response.status_code == 200