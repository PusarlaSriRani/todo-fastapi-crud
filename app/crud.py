from app.schema import TodoCreate , TodoResponse , TodoUpdate
 
todos = []

todo_id_counter =1

def create_todo(todo:TodoCreate):
    global todo_id_counter
    new_todo = {
        "id":todo_id_counter,
        "title" :todo.title,
        "description" : todo.description,
        "completed": False
    } 
    
    todos.append(new_todo)

    todo_id_counter +=1
    return new_todo

def get_all_todos():
    return todos

def get_todo_by_id(todo_id :int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None

def delete_todo(todo_id:int):
    todo = get_todo_by_id(todo_id)

    if not todo:
        return None
    
    todos.remove(todo)

    return todo

def update_todo(todo_id: int, todo_data:TodoUpdate):
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None
    updated_data = todo_data.model_dump(exclude_unset=True)

    for key,value in updated_data.items():
        todo[key] = value 
    
    return todo