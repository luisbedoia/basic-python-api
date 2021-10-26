from app.main import app
import asyncio
from typing import Generator
from tortoise.contrib.test import finalizer, initializer
import pytest
from fastapi.testclient import TestClient
from app.services.step import StepService
from app.models.user import user, user_in, users

@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["app.models.user"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()

#Getting an invalid user's step data
def test_get_nonexisting_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    '''returns 404'''
    service = StepService(users)
    app.step = service
    client = TestClient(app)

    response = client.get("users/toString/steps")
    assert response.status_code == 404
    assert response.json() == {"detail":"User doesn't exist"}

def test_get_nonexisting_user_payload(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    '''returns 404 with expected payload'''
    service = StepService(users)
    app.step = service
    client = TestClient(app)

    response = client.get("users/nonexistentUser/steps")
    assert response.status_code == 404
    assert response.json() == {"detail":"User doesn't exist"}


#Getting a valid user's step data
def test_get_existing_user_payload(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    '''returns 200 with expected step count'''
    service = StepService(users)
    app.step = service
    client = TestClient(app)

    response = client.get("users/jenna/steps")
    jsonRes = response.json()
    assert response.status_code == 200
    assert jsonRes['ts'] == 1503256778463.0
    assert jsonRes['cumulative_steps'] == 12323