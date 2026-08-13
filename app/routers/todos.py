from fastapi import APIRouter , HTTPException , status
from typing import List

from app.schema import TodoCreate , TodoResponse , TodoUpdate #if u want to import everything keep *
from app import crud #or we can write as from app.crud import *
 
router = APIRouter(
    prefix = "/todos",
    tags = ["todos"]
)

@router.post("/",response_model = TodoResponse ,status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    return crud.create_todo(todo)

@router.get("/",response_model = List[TodoResponse])
def get_todos():
    return crud.get_all_todos()

@router.get("/{todo_id}",response_model=TodoResponse)
def get_todo(todo_id:int):
    todo = crud.get_todo_by_id(todo_id)

    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    return todo

@router.delete("/{todo_id}")
def delete_todo(todo_id:int):
    todo = crud.delete_todo(todo_id)

    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate):
    updated_todo = crud.update_todo(todo_id, todo)

    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated_todo