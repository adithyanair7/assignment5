import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Spice"

def test_add_sheep():
    new_sheep = {"id": 2, "name": "Luna", "breed": "Suffolk", "sex": "Female"}
    response = client.post("/sheep/", json=new_sheep)
    assert response.status_code == 201
    assert response.json()["name"] == "Luna"

def test_update_sheep():
    updated_sheep = {"id": 1, "name": "Spice", "breed": "Gotland", "sex": "Male"}
    response = client.put("/sheep/1", json=updated_sheep)
    assert response.status_code == 200
    assert response.json()["sex"] == "Male"

def test_delete_sheep():
    response = client.delete("/sheep/1")
    assert response.status_code == 204

def test_get_all_sheep():
    response = client.get("/sheep/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_nonexistent_sheep():
    response = client.get("/sheep/999")
    assert response.status_code == 404

def test_update_nonexistent_sheep():
    updated_sheep = {"id": 999, "name": "Ghost", "breed": "Unknown", "sex": "Unknown"}
    response = client.put("/sheep/999", json=updated_sheep)
    assert response.status_code == 404

def test_delete_nonexistent_sheep():
    response = client.delete("/sheep/999")
    assert response.status_code == 404
