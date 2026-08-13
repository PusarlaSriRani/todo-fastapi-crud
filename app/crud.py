from app.schema import TodoCreate, TodoUpdate

todos = []

def create_todo(todo: TodoCreate):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "description": todo.description,
        "completed": False
    }

    todos.append(new_todo)
    return new_todo

def get_all_todos():
    return todos

def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None

def update_todo(todo_id: int, todo_update: TodoUpdate):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = todo_update.title
            todo["description"] = todo_update.description
            return todo
    return None

def patch_todo(todo_id: int, todo_update: TodoUpdate):
    for todo in todos:
        if todo["id"] == todo_id:
            update_data = todo_update.dict(exclude_unset=True)
            todo.update(update_data)
            return todo
    return None
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return todo

    return None