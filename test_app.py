import pytest
from app import app

client = app.test_client()

def test_create_event():
    response = client.post('/events', json={
        "title": "Meeting",
        "description": "Discuss roadmap",
        "start_time": "2025-06-30T14:00:00",
        "end_time": "2025-06-30T15:00:00"
    })
    assert response.status_code == 201

def test_list_events():
    response = client.get('/events')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
