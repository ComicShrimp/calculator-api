from fastapi.testclient import TestClient

from calculator_api.main import app

client = TestClient(app)


def test_api_numeros_positivos() -> None:
    response = client.get("/subtracao?numeros=2&numeros=2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 0}


def test_api_numeros_negativos() -> None:
    response = client.get("/subtracao?numeros=-2&numeros=-2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 0}


def test_api_numeros_negativos_e_positivos() -> None:
    response = client.get("/subtracao?numeros=-2&numeros=2")
    assert response.status_code == 200
    assert response.json() == {"resultado": -4}


def test_api_string() -> None:
    response = client.get("/subtracao?numeros=ola&numeros=texto")
    assert response.status_code == 422


def test_api_sem_argumentos() -> None:
    response = client.get("/subtracao")
    assert response.status_code == 422
