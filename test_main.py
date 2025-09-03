from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API, Call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/Shohei Ohtani")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "shohei ohtani",
            "大谷 翔平",
            "hepburn",
            "shōhei",
            "[ oːtaɲi ɕoːheː ]",
            "show-hey oh-tah-nee",
            "july",
            "professional baseball",
            "los angeles",
            "major league baseball",
            "mlb",
        ]
    }
