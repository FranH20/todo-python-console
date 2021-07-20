from typing import Collection
from rich.console import Console
from rich.layout import Panel
from rich.table import Table
from pysondb import db
from theme import custom_theme
from layout import layout
from todo import todo

database = db.getDb("database.json")
console = Console(theme=custom_theme)

#Table Todo
tableTodos = Table(title="Todo list")
tableTodos.add_column("N°", style="medium_purple")
tableTodos.add_column("Title", style="medium_spring_green")
tableTodos.add_column("Date", style="medium_purple")

def create():
    new_todo = todo()
    todo_title = console.input("[primary]Add the new todo: [/primary]")
    todo_description = console.input("[secondary]Add the description todo: [/secondary]")
    try:
        new_todo.title = todo_title
        new_todo.description = todo_description
        database.add({
            "title":new_todo.title,
            "description": new_todo.description,
            "time": new_todo.time,
            "date": new_todo.date
        })
    except Exception as e:
        console.log("An error an occurred... ",e)

def read():
    all_data = database.getAll()
    count = 0
    for collection in all_data:
        count = count + 1
        tableTodos.add_row(str(count),collection["title"],collection["date"])
    console.print(tableTodos)

def read_detail(number_row, all_data):
    data = all_data[number_row]
    console.print(data["title"])
    console.print(data["description"])
    console.print(data["time"])
    console.print(data["date"])

def find_collection(todo_update):
    collection = {}
    all_data = database.getAll()
    if todo_update >= 0:
        collection = all_data[todo_update]
    return collection

def update():
    #Get the Todo
    edit_todo = todo()
    todo_update = int(console.input("[primary]Choose the TODO to update: [/primary]"))
    todo_update = todo_update - 1
    collection = find_collection(todo_update)
    #Add the data to an object
    id_edit = collection["id"]
    edit_todo.title = collection["title"]
    edit_todo.description = collection["description"]
    console.print(f"[secondary]{edit_todo.title} [/secondary]")
    console.print(f"[secondary]{edit_todo.description} [/secondary]")
    option_edit = console.input("[primary]What do you need edit [T] Title or [D] Description, [X] to exit ? [/primary]")
    #Edit in database
    if option_edit.lower().strip() == 't':
        edit_todo.title = console.input("[secondary]Write the new Title:[/secondary] :arrow_right:")
    elif option_edit.lower().strip() == 'd':
        edit_todo.description = console.input("[secondary]Write the new Description:[/secondary] :arrow_right:")
    else:
        return
    try:
        database.updateById(id_edit, {
            "title": edit_todo.title,
            "description":edit_todo.description,
            "time":edit_todo.time,
            "date":edit_todo.date
        })
        read_detail(todo_update, all_data)
    except Exception as e:
        console.log("An error an occurred... ",e)
    
    
def delete():
    #Get the Todo
    todo_update = int(console.input("[primary]Choose the TODO to delete, [X] to exit [/primary]"))
    if todo_update.lower().strip() == "x":
        return

    todo_update = todo_update - 1
    collection = find_collection(todo_update)
    id_delete = collection["id"]
    try:
        database.deleteById(id_delete)
    except Exception as e:
        console.log("An error an occurred... ",e)

def run():
    read()
    delete()
    #op = int(console.input("[primary]Enter a number please : [/primary]"))
    #new_todo = console.input("[primary]Add the new todo: [/primary]")

if __name__ == "__main__":
    run()
 
