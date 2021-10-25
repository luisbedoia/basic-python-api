from fastapi import FastAPI
from app.routes.user import User
from app.config.db import connectToDatabase
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from tortoise import Tortoise
from dotenv import load_dotenv
import os
load_dotenv()



app = FastAPI()
app.include_router(User)
db_url = os.environ.get("DB_URL")
register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["app.models.user"]},
    generate_schemas=True,
    add_exception_handlers=True,
)