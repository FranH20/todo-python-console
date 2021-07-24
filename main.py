#python
from os import system
#rich
from rich.console import Console
from rich.layout import Panel
from rich.text import Text
from rich.align import Align

#pysondb
from pysondb import db

#packages
from theme import custom_theme
from todo import todo


database = db.getDb("database.json")
console = Console(theme=custom_theme)

def create():
    todo_title = console.input("[primary]Add the Title of the new Todo, [X] to exit: [/primary]")
    if todo_title.lower().strip() == 'x':
        return
    todo_description = console.input("[secondary]Add the description todo, [X] to exit: [/secondary]")
    if todo_description.lower().strip() == 'x':
        return
    new_todo = todo()
    try:
        new_todo.title = todo_title
        new_todo.description = todo_description
        database.add({
            "title":new_todo.title,
            "description": new_todo.description,
            "time": new_todo.time,
            "date": new_todo.date,
            "status": new_todo.status
        })
    except Exception as e:
        console.log("An error an occurred... ",e)
        
def read_detail(collection):
    system("clear")
    console.print(f'Title: [primary]{collection["title"]}[/primary]')
    console.print(f'Description: [primary]{collection["description"]}[/primary]')
    if collection["status"] == True:
        console.print('Status: [primary]Todo finished[/primary]  :white_check_mark:')
    else:
        console.print('Status: [primary]Todo unfinished[/primary] :x:')
    console.print(f'Date: [primary]{collection["date"]}[/primary]')
    console.print(f'Time: [primary]{collection["time"]}[/primary]')

def read_once():
    all_data = database.getAll()
    count = 0
    for collection in all_data:
        count = count + 1
        message = f'{str(count)}.- '
        if collection["status"] == True:
            message = f':white_check_mark: [secondary] {str(count)}.- {collection["title"]} [/secondary]'
        else:
            message = f':x: [secondary] {str(count)}.- {collection["title"]} [/secondary]' 
        console.print(message)
    
        
def read():
    todo_read = 0
    try:
        todo_read = int(console.input("[primary]Choose the TODO to view the detail, [0] to exit: [/primary]"))
    except ValueError as e:
        console.log("The input was not a valid integer")
    if todo_read == 0:
        return
    todo_read = todo_read - 1
    collection = find_collection(todo_read)
    read_detail(collection)

def find_collection(todo_search):
    collection = {}
    all_data = database.getAll()
    if todo_search >= 0:
        collection = all_data[todo_search]
    return collection

def update():
    #Get the Todo
    todo_update = 0
    try:
        todo_update = int(console.input("[primary]Choose the TODO to update, [0] to exit [/primary]"))
    except ValueError as e:
        console.log("The input was not a valid integer")
    if todo_update == 0:
        return
    edit_todo = todo()
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
        edit_todo.title = console.input("[secondary]Write the new Title:[/secondary] :arrow_right: \n")
    elif option_edit.lower().strip() == 'd':
        edit_todo.description = console.input("[secondary]Write the new Description:[/secondary] :arrow_right: \n")
    else:
        return
    try:
        database.updateById(id_edit, {
            "title": edit_todo.title,
            "description":edit_todo.description,
            "time":edit_todo.time,
            "date":edit_todo.date,
            "status": edit_todo.status
        })
        collection = find_collection(todo_update)
        read_detail(collection)
    except Exception as e:
        console.log("An error an occurred... ",e)
    
    
def delete():
    #Get the Todo
    todo_delete = 0
    try:
        todo_delete = int(console.input("[primary]Choose the TODO to delete, [0] to exit: [/primary]"))
    except ValueError as e:
        console.log("The input was not a valid integer")
    if todo_delete == 0:
        return

    todo_delete = todo_delete - 1
    collection = find_collection(todo_delete)
    id_delete = collection["id"]
    try:
        database.deleteById(id_delete)
    except Exception as e:
        console.log("An error an occurred... ",e)
def complete():
    #Get the Todo
    todo_complete = 0
    try:
        todo_complete = int(console.input("[primary]Choose the TODO to complete, [0] to exit [/primary]"))
    except ValueError as e:
        console.log("The input was not a valid integer")
    if todo_complete == 0:
        return
    complete_todo = todo()
    todo_complete = todo_complete - 1
    collection = find_collection(todo_complete)
    #Add the data to an object
    id_edit = collection["id"]
    complete_todo.title = collection["title"]
    complete_todo.description = collection["description"]
    option_complete = console.input("[primary]Do you complete this TODO [Y] Yes or [N] No ? [/primary]")
    #Edit in database
    if option_complete.lower().strip() == 'y':
        complete_todo.status = True
    elif option_complete.lower().strip() == 'n':
        complete_todo.status = False
    
    try:
        database.updateById(id_edit, {
            "title": complete_todo.title,
            "description":complete_todo.description,
            "time":complete_todo.time,
            "date":complete_todo.date,
            "status": complete_todo.status
        })
        collection = find_collection(todo_complete)
        read_detail(collection)
    except Exception as e:
        console.log("An error an occurred... ",e)
def get_text():
    all_data = database.getAll()
    text = Text()
    text.append("1.- Add Todo \n")
    if all_data:
        text.append("2.- Read Todo \n")
        text.append("3.- Edit Todo \n")
        text.append("4.- Delete Todo \n")
        text.append("5.- Complete Todo \n")
    text.append("6.- Exit")
    return text, all_data
def run():
    op = 0
    while op != 6:
        text,all_data = get_text()
        console.print(Panel.fit(
                Align.center(
                    text,
                    vertical="middle",
                ),
                padding=(1, 2),
                title="Menu TODO"
            )
        )
        try:
            op = int(console.input('[secondary]Enter a number option .... [/secondary]'))
            system('clear')
            read_once()
        except ValueError as e:
            console.log("The input was not a valid integer")
            break
        
        if op == 1:
            create() 
            console.input("[primary]Succesfully, press enter to continue.....[/primary]")
        elif all_data:             
            if op == 2:
                read()
                console.input("[primary]Succesfully, press enter to continue.....[/primary]")
            elif op == 3:
                update()
                console.input("[primary]Succesfully, press enter to continue.....[/primary]")
            elif op == 4:
                delete()
                console.input("[primary]Succesfully, press enter to continue.....[/primary]")
            elif op == 5:
                complete()
                console.input("[primary]Succesfully, press enter to continue.....[/primary]")
        
        system('clear')
        

if __name__ == "__main__":
    run()
 
