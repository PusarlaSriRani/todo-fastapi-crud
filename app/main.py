from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import todos

app = FastAPI (
    title = 'Todo API',
    description = 'A simple API for managing todos',
    version = '0.1.0'
)
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=['*'])
app.include_router(todos.router)

@app.get("/")
def root():
    return{
        "message":"welcome to Todo API"
    }