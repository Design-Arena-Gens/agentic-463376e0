from fastapi.testclient import TestClient
from index import app

def test_root():
    client = TestClient(app)
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello from FastAPI on Vercel"}
