from app.models.user import user, user_in, users
class StepService:
    def __init__(self, User:users):
        self.User = users

    async def get(self, username: str) -> user or None:
        '''If user exist, returns the user info object, else returns None'''
        user_username = await self.User.filter(username=username).first()
        if user_username:
            return user_username
        else:
            return None

    async def add(self, username: str, ts: float, new_steps: int) -> bool:
        '''If user exists, replace its timestamp ts and add new_steps to cumulative_steps, else inserts a new user with incoming data'''
        if username and ts and new_steps:
            user_username = await self.User.filter(username=username).first()
            if user_username:
                update = {
                    'username': username,
                    'ts': ts,
                    'cumulative_steps': user_username.cumulative_steps + new_steps
                }
                await self.User.filter(username=username).update(**update)
                return True
            else:
                user = {
                    'username': username,
                    'ts': ts,
                    'cumulative_steps': new_steps
                }
                new_user = await self.User.create(**user)
                return True
        else:
            return False