from main import app

import asyncio
from typing import Generator
from tortoise.contrib.test import finalizer, initializer
import pytest
from fastapi.testclient import TestClient
from spec.store import testStore
from services.step import StepService, StepService2
from models.user import user, user_in, users 
import copy

@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["models.user"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()

store = copy.deepcopy(testStore)
# def test_read_main():
#     client = TestClient(app)
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

#Getting an invalid user's step data
def test_get_nonexisting_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    '''returns 404'''
    service = StepService2(users)
    app.step = service
    client = TestClient(app)

    response = client.get("users/toString/steps")
    assert response.status_code == 404
    assert response.json() == {"detail":"User doesn't exist"}

def test_get_nonexisting_user_payload(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    '''returns 404 with expected payload'''
    service = StepService2(users)
    app.step = service
    client = TestClient(app)

    response = client.get("users/nonexistentUser/steps")
    assert response.status_code == 404
    assert response.json() == {"detail":"User doesn't exist"}


#Getting a valid user's step data
def test_get_existing_user_payload(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    '''returns 200 with expected step count'''
    service = StepService2(users)
    app.step = service
    client = TestClient(app)

    response = client.get("users/jenna/steps")
    jsonRes = response.json()
    assert response.status_code == 200
    assert jsonRes['ts'] == 1503270344121
    assert jsonRes['cumulativeSteps'] == 11