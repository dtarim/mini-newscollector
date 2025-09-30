from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Mini News Collector is running!"}

def test_refresh_and_articles():
    # Önce refresh çağır
    response = client.post("/refresh")
    assert response.status_code == 200

    # Sonra articles endpointini test et
    response = client.get("/articles")
    assert response.status_code == 200
    data = response.json()
    assert "articles" in data
    assert isinstance(data["articles"], list)  #just checked for not working progress and new test result in github actions!!