from main import app
from fastapi.testclient import TestClient
from spec.store import testStore
from step import StepService
import copy

store = copy.deepcopy(testStore)
def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

#Getting an invalid user's step data
def test_get_nonexisting_user():
    '''returns 404'''
    service = StepService(store)
    app.step = service
    client = TestClient(app)

    response = client.get("users/toString/steps")
    assert response.status_code == 404
    assert response.json() == {"detail":"User doesn't exist"}

def test_get_nonexisting_user_payload():
    '''returns 404 with expected payload'''
    service = StepService(store)
    app.step = service
    client = TestClient(app)

    response = client.get("users/nonexistentUser/steps")
    assert response.status_code == 404
    assert response.json() == {"detail":"User doesn't exist"}


#Getting a valid user's step data
def test_get_existing_user_payload():
    '''returns 200 with expected step count'''
    service = StepService(store)
    app.step = service
    client = TestClient(app)

    response = client.get("users/jenna/steps")
    jsonRes = response.json()
    assert response.status_code == 200
    assert jsonRes['ts'] == 1503256778463
    assert jsonRes['cumulativeSteps'] == 12323