from tortoise import Tortoise
import asyncio


async def connectToDatabase():
    # await Tortoise.init(
    #     db_url='postgres://bob:admin@localhost:5432/test',
    #     modules={'models': ['app.models']}
    # )

    await Tortoise.init(
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": "test",
                        "host": "127.0.0.1",
                        "password": "saira",
                        "port": 5432,
                        "user": "arias",
                    }
                }
            },
            "apps": {
                "models": {
                    "models": ["models.user"],
                    "default_connection": "default",
                }
            },
        }
    )