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
        console.log("An error an occurred...",e)

def read():
    all_data = database.getAll()
    count = 0
    for collection in all_data:
        count = count + 1
        tableTodos.add_row(str(count),collection["title"],collection["date"])
    console.print(tableTodos)

def update():
    pass
    
def delete():
    pass

def run():
    read()
    pass
    #op = int(console.input("[primary]Enter a number please : [/primary]"))
    #new_todo = console.input("[primary]Add the new todo: [/primary]")

if __name__ == "__main__":
    run()
 
