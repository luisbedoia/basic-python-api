import tortoise
from db import connectToDatabase

async def main():
    await connectToDatabase()
    await tortoise.Tortoise.generate_schemas()

if __name__ == '__main__':
    tortoise.run_async(main())