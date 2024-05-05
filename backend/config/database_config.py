# it is the mongodb driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://127.0.0.1:27017'
)

database = client.TodoList
collection = database.todos