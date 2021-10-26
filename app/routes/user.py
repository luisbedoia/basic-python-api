from fastapi import APIRouter, HTTPException, WebSocket
from app.services.step import StepService
import json

from app.models.user import user, user_in, users

service = StepService(users)

User = APIRouter()

User.step = service

@User.get("/users/{user}/steps")
async def get_steps(user:str):
    response = await User.step.get(user)
    if response:
        return response
    else:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    
    

@User.websocket("/ws")
async def add_steps(websocket: WebSocket):
    print("WS connection started")
    await websocket.accept()
    await websocket.send_json("connected")
    while True:
        try:            
            data = await websocket.receive_text()
            data = json.loads(data)
            print(data)
            await User.step.add(data['username'],data['ts'],data['new_steps'])
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')