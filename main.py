from fastapi import FastAPI
from routes.user import User
from config.db import connectToDatabase
from config.createSchema import createSchema
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


app = FastAPI()
app.include_router(User)

register_tortoise(
    app,
    db_url="postgres://bob:admin@127.0.0.1:5432/test",
    modules={"models": ["models.user"]},
    generate_schemas=True,
    add_exception_handlers=True,
)