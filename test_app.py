import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Basic math test (as required)
def test_home():
    assert 1 + 1 == 2

# Test home route returns 200
def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200

# Test home route returns correct JSON
def test_home_route_json(client):
    response = client.get("/")
    data = response.get_json()
    assert data["status"] == "success"
    assert "message" in data

# Test health endpoint
def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"

# Test add endpoint
def test_add_route(client):
    response = client.get("/add/3/4")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 7

# Test add with zeros
def test_add_zeros(client):
    response = client.get("/add/0/0")
    data = response.get_json()
    assert data["result"] == 0
