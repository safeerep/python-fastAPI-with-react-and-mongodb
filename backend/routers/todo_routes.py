from fastapi import APIRouter, HTTPException
router = APIRouter()
from model import todo_model

from controllers import database_controller

# router for to fetch all todos
@router.get('/get-todos')
async def get_todos():
    print("in router")
    try:
        return await database_controller.fetch_all_todos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

# router for to fetch one specific todo
@router.get('/get-todo/{title}')
async def get_todo(title):
    try:
        return await database_controller.get_one_todo(title)
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))


# router to create new todo   
@router.post('/create-todo')
async def create_todo(todo: todo_model.TodoModel):
    try:
        return await database_controller.create_todo(todo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# to update one specific todo   
@router.put('/update-todo')
async def update_todo(todo: todo_model.TodoModel):
    try:
        return await database_controller.update_one_todo(todo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# to remove one specific todo  
@router.delete('/remove-todo/{title}')
async def remove_todo(title):
    try:
        return await database_controller.remove_one_todo(title)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))