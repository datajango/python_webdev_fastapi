from starlette.responses import HTMLResponse
from starlette.testclient import TestClient
from server.main import app

def test_app():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
