from fastapi.routing import APIRouter
from main import app
from routes.user import User
from fastapi.testclient import TestClient
from spec.store import testStore
from services.step import StepService, StepService2
import copy

import asyncio
from typing import Generator
from tortoise.contrib.test import finalizer, initializer
import pytest
from models.user import user, user_in, users

@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["models.user"])
    with TestClient(app) as c:
        yield c
    finalizer()

@pytest.fixture(scope="module")
def service(User: APIRouter, ) -> Generator:
    service = StepService2(users)
    User.step = service
    app.include_router(User)
    client = TestClient(app)


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()

# WebSocket API

store = copy.deepcopy(testStore)


def test_websocket():
    '''Connects to de ws and receives a message'''
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == "connected"

# Getting an invalid user's step data


def test_add_steps_existing_user(client: TestClient, event_loop: asyncio.AbstractEventLoop, service):
    '''Adds a existing user the newSteps'''
    update = {
        "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
        "username": 'jenna',
        "ts": 1503270344121,
        "newSteps": 11,
    }

    with client.websocket_connect("/ws") as websocket:
        websocket.send_json(update)
    assert service.get('jenna')["cumulativeSteps"] == 11 + 11


def test_add_steps_nonexisting_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    '''Adds a new user to store'''
    service = StepService2(users)
    User.step = service
    app.include_router(User)
    client = TestClient(app)

    update = {
        "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
        "username": 'jose',
        "ts": 1503270344121,
        "newSteps": 11,
    }

    with client.websocket_connect("/ws") as websocket:
        websocket.send_json(update)
    assert service.get('jose')["cumulativeSteps"] == 11