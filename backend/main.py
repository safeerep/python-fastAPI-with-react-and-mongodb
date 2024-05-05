from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import todo_routes
from config import database_config
app = FastAPI()

origins = [
    "https://localhost:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=  origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/health")
def root():
    return {
        "message": "ok fine"
    }

app.include_router(
    router=todo_routes.router,
    prefix="/api",
)