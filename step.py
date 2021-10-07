class StepService:
    def __init__(self,store:dict):
        self.store = store
    def get(self,username:str):
        '''If user exist, returns the user info object, else returns None'''
        if username in self.store:
            return self.store[username]
        else:
            return None

    def add(self,username:str,ts:float,newSteps:int):
        '''If user exists, replace its timestamp ts and add newSteps to cumulativeSteps, else inserts a new user with incoming data'''
        print(username)
        print(ts)
        print(newSteps)
        if username and ts and newSteps:
            if username in self.store:
                self.store[username]['ts'] = ts
                self.store[username]['cumulativeSteps'] = self.store[username]['cumulativeSteps'] + newSteps
                return True
            else:
                self.store[username]={
                        'ts':ts,
                        'cumulativeSteps': newSteps
                        }
                return True
        else:
            return False
