from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_cars():
    response = client.get("/cars")
    assert response.status_code == 200
    assert isinstance(response.json(),list)

def test_car_not_found():
    response = client.get("/cars/Unknown/Unknown")
    assert response.status_code == 404

def test_add_car(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    inventory = tmp_path / "cars.json"
    inventory.write_text("[]")

    response = client.post(

        "/cars",
        json={
            "brand": "Bugatti",
            "model": "Chiron"

        }


    )
    assert response.status_code in (200, 201)