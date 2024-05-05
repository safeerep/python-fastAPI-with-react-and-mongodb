from model import todo_model
from config import database_config

collection = database_config.collection

# to get all todos
async def fetch_all_todos():
    todos = []
    async for doc in collection.find():
        doc["_id"] = str(doc['_id'])
        todos.append(doc)
    return {
        "message": "successfully fetched the todos",
        "todos": todos
    }

# to create a new todo
async def create_todo(todo):
    todo_dict = todo.dict()
    result = await collection.insert_one(todo_dict)
    # converting ObjectId to string to avoid error
    # then, modifying the todo dictionary to include the _id field
    todo_dict['_id'] = str(result.inserted_id)
    todos = []
    async for doc in collection.find():
        doc["_id"] = str(doc['_id'])
        todos.append(doc)
    return ({
        "message": "successfully created new todo",
        "todo": todo_dict,
        "todos": todos
    })

# to get a todo with specific title
async def get_one_todo(title):
    # finding a document with specified title;
    print(title)
    result = await collection.find_one({
        "title": title
    })
    result["_id"] = str(result["_id"])
    print(result)
    return({
        "message": "successfully fetched a specific todo",
        "todo": result
    })

# to update a todo with specific title
async def update_one_todo(todo):
    todo_dict = todo.dict()
    title = todo_dict['title']
    description = todo_dict['description']
    await collection.find_one_and_update(
        {
            "title": title
        }, {
            "$set": {
                "description": description
            }
        }
    )
    document = await collection.find_one({"title": title})
    document["_id"] = str(document["_id"])
    return ({
        "message": "successfully updated ",
        "todo": document
    })

# to remove a todo with specific title
async def remove_one_todo(title):
    result = await collection.find_one_and_delete(
        {
            "title": title
        }
    )
    print(result)
    result["_id"] = str(result["_id"])
    todos = []
    async for doc in collection.find():
        doc["_id"] = str(doc['_id'])
        todos.append(doc)

    return ({
        "message": "successfully removed ",
        "todo": result,
        "todos": todos
    })