from typing import Optional
from fastapi import FastAPI, HTTPException, WebSocket
from step import StepService
from spec.store import testStore
import json

store = testStore
service = StepService(store)

app = FastAPI()
app.step = service

@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/users/{user}/steps")
def get_steps(user:str):
    response = app.step.get(user)
    if response == None:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    else:
        return response

@app.websocket("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()

@app.websocket("/ws/update")
async def websocket(websocket: WebSocket):
    print("WS connection started")
    await websocket.accept()
    while True:
        try:            
            data = await websocket.receive_text()
            data = json.loads(data)
            print("New message")
            app.step.add(data['username'],data['ts'],data['newSteps'])
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')
