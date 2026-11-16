import pytest
from app import create_app
from models import db

@pytest.fixture()
def client():
    test_app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test-only-secret",
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
    })
    with test_app.test_client() as test_client:
        yield test_client
    with test_app.app_context():
        db.session.remove()
        db.drop_all()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_create_and_list_task(client):
    created = client.post("/api/tasks", json={"title": "Learn Azure"})
    assert created.status_code == 201
    task_id = created.json["id"]

    listed = client.get("/api/tasks")
    assert listed.status_code == 200
    assert listed.json[0]["id"] == task_id

def test_create_requires_title(client):
    response = client.post("/api/tasks", json={"title": " "})
    assert response.status_code == 400

def test_update_and_delete_task(client):
    created = client.post("/api/tasks", json={"title": "Practice"})
    task_id = created.json["id"]

    updated = client.patch(
        f"/api/tasks/{task_id}",
        json={"status": "Completed"},
    )
    assert updated.status_code == 200
    assert updated.json["status"] == "Completed"

    deleted = client.delete(f"/api/tasks/{task_id}")
    assert deleted.status_code == 204
