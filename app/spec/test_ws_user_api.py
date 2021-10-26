# # import asyncio
# # import pytest
# # from app.main import app
# # from typing import Generator
# # from tortoise.contrib.test import finalizer, initializer
# # from fastapi.testclient import TestClient
# # from app.services.step import StepService
# # from app.models.user import user, user_in, users
# # from app.routes.user import User

# # @pytest.fixture(scope="module")
# # def client() -> Generator:
# #     initializer(["app.models.user"])
# #     with TestClient(app) as c:
# #         yield c
# #     finalizer()

# # @pytest.fixture(scope="module")
# # def event_loop(client: TestClient) -> Generator:
# #     yield client.task.get_loop()

# # # WebSocket API

# # def test_websocket():
# #     '''Connects to de ws and receives a message'''
# #     client = TestClient(app)
# #     with client.websocket_connect("/ws") as websocket:
# #         data = websocket.receive_json()
# #         assert data == "connected"

# # # Getting an invalid user's step data


# # def test_add_steps_existing_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
# #     '''Adds a existing user the newSteps'''
# #     service = StepService(users)
# #     User.step = service
# #     app.include_router(User)
# #     client = TestClient(app)
# #     update = {
# #         "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
# #         "username": 'jenna',
# #         "ts": 1503270344121,
# #         "newSteps": 11,
# #     }

# #     with client.websocket_connect("/ws") as websocket:
# #         websocket.send_json(update)
# #     response = service.get("users/jenna/steps")
# #     assert response["cumulative_steps"] == 12323 + 11


# # def test_add_steps_nonexisting_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
# #     '''Adds a new user to store'''
# #     service = StepService(users)
# #     User.step = service
# #     app.include_router(User)
# #     client = TestClient(app)

# #     update = {
# #         "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
# #         "username": 'jose',
# #         "ts": 1503270344121,
# #         "newSteps": 11,
# #     }

# #     with client.websocket_connect("/ws") as websocket:
# #         websocket.send_json(update)
# #     response = service.get("users/jenna/steps")
# #     assert response["cumulative_steps"] == 11
# from app.main import app
# import asyncio
# from typing import Generator
# from tortoise.contrib.test import finalizer, initializer
# import pytest
# from fastapi.testclient import TestClient
# from app.services.step import StepService
# from app.models.user import user, user_in, users
# from app.routes.user import User

# @pytest.fixture(scope="module")
# def client() -> Generator:
#     initializer(["app.models.user"])
#     service = StepService(users)
#     User.step = service
#     app.include_router(User)
#     with TestClient(app) as c:
#         yield c
#     finalizer()


# @pytest.fixture(scope="module")
# def event_loop(client: TestClient) -> Generator:
#     yield client.task.get_loop()

# def test_websocket(client: TestClient, event_loop: asyncio.AbstractEventLoop):
#     '''Connects to de ws and receives a message'''
#     update = {
#         "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
#         "username": 'jose',
#         "ts": 1503270344121,
#         "new_steps": 11,
#     }
#     with client.websocket_connect("/ws") as websocket:
#         # data = websocket.receive_json()
#         response = websocket.send_json(update)
#         print(response)
#         # assert data == "connected"
    

# #Getting a valid user's step data
# def test_get_existing_user_payload(client: TestClient, event_loop: asyncio.AbstractEventLoop):
#     '''returns 200 with expected step count'''

#     response = client.get("users/jenna/steps")
#     jsonRes = response.json()
#     assert response.status_code == 200
#     assert jsonRes['ts'] == 1503256778463.0
#     assert jsonRes['cumulative_steps'] == 12323

# # #Getting an invalid user's step data
# # def test_get_nonexisting_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):
# #     '''returns 404'''

# #     update = {
# #         "update_id": 'c0efd8a1-b3b8-49b7-92b1-69edc8bd6c0c',
# #         "username": 'jose',
# #         "ts": 1503270344121,
# #         "new_steps": 11,
# #     }

# #     with client.websocket_connect("/ws") as websocket:
# #         ws_res = websocket.send_json(update)
        

# #     response = client.get("users/jose/steps")
# #     assert response.status_code == 200