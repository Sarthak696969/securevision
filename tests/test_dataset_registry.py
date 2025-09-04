from fastapi.testclient import TestClient
from securevision.api.main import app

def test_register_and_list():
    c = TestClient(app)
    r = c.post("/datasets/register", headers={"x-api-key":"dev"}, json={"name":"gtsrb","type":"gtsrb","version":"1.0"})
    assert r.status_code == 200
    r = c.get("/datasets", headers={"x-api-key":"dev"})
    assert r.status_code == 200
