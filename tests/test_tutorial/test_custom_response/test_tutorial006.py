from fastapi.testclient import TestClient

from docs_src.custom_response.tutorial006 import app

client = TestClient(app)


def test_get():
    response = client.get("/typer", allow_redirects=False)
    assert response.status_code == 307, response.text
    assert response.headers["location"] == "https://typer.tiangolo.com"
