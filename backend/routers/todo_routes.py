from fastapi import FastAPI, APIRouter
router = APIRouter()

@router.get('/get-todos')
async def get_todos():
    return {
        "todos": "..,..,.."
    }