import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from beanie import init_beanie
from models import Human, Pet


async def example():
    client = AsyncIOMotorClient("mongodb://mongo:password@host:27000")
    await init_beanie(database=client.db_name, document_models=[Human, Pet])

    cat = Pet(name="Whiskers")
    dog = Pet(name="Barky")

    await cat.insert()
    await dog.insert()

    husband = Human(name="Mike", pets=[cat, dog])
    wife = Human(name="Maria", pets=[cat])

    await husband.insert()
    await wife.insert()

    # Fetch models
    
    humans = await Human.find_all(fetch_links=True).to_list()
    print(humans)

if __name__ == "__main__":
    asyncio.run(example())
