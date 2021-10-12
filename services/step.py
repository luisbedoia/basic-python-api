from models.user import User_Pydantic, UserIn_Pydantic, Users
class StepService:
    def __init__(self, store: dict):
        self.store = store

    def get(self, username: str):
        '''If user exist, returns the user info object, else returns None'''
        if username in self.store:
            return self.store[username]
        else:
            return None

    def add(self, username: str, ts: float, newSteps: int):
        '''If user exists, replace its timestamp ts and add newSteps to cumulativeSteps, else inserts a new user with incoming data'''
        if username and ts and newSteps:
            if username in self.store:
                self.store[username]['ts'] = ts
                self.store[username]['cumulativeSteps'] = self.store[username]['cumulativeSteps'] + newSteps
                return True
            else:
                self.store[username] = {
                    'ts': ts,
                    'cumulativeSteps': newSteps
                }
                return True
        else:
            return False

class StepService2:
    def __init__(self, Users:Users):
        self.Users = Users

    async def get(self, username: str):
        '''If user exist, returns the user info object, else returns None'''
        user_username = await self.Users.filter(username=username).first()
        if user_username:
            return user_username
        else:
            return None

    async def add(self, username: str, ts: float, newSteps: int):
        '''If user exists, replace its timestamp ts and add newSteps to cumulativeSteps, else inserts a new user with incoming data'''
        if username and ts and newSteps:
            user_username = await self.Users.filter(username=username).first()
            if user_username:
                update = {
                    'username': username,
                    'ts': ts,
                    'cumulativeSteps': user_username.cumulativeSteps + newSteps
                }
                await self.Users.filter(username=username).update(**update)
                return True
            else:
                user = {
                    'username': username,
                    'ts': ts,
                    'cumulativeSteps': newSteps
                }
                new_user = await self.Users.create(**user)
                return True
        else:
            return False