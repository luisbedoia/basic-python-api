from main import app
from fastapi.testclient import TestClient
from spec.store import testStore
from step import StepService
import copy

# WebSocket API

store = copy.deepcopy(testStore)

def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket():
    '''Connects to de ws and receives a message'''
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}

# Getting an invalid user's step data


def test_add_steps_existing_user():
    '''Adds a existing user the newSteps'''
    service = StepService(store)
    app.step = service
    client = TestClient(app)

    update = {
        "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
        "username": 'jenna',
        "ts": 1503270344121,
        "newSteps": 11,
    }

    with client.websocket_connect("/ws/update") as websocket:
        websocket.send_json(update)
    assert service.get('jenna')["cumulativeSteps"] == 12323 + 11


def test_add_steps_nonexisting_user():
    '''Adds a new user to store'''
    service = StepService(store)
    app.step = service
    client = TestClient(app)

    update = {
        "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
        "username": 'jose',
        "ts": 1503270344121,
        "newSteps": 11,
    }

    with client.websocket_connect("/ws/update") as websocket:
        websocket.send_json(update)
    assert service.get('jose')["cumulativeSteps"] == 11