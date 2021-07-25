#python
from os import system, name as system_name
from re import L
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

#Messages
NOTHING_TO_SHOW = "There is nothing to show"
AN_ERROR = "An error an occurred..."
NUMBER_INPUT_ERROR = "The input was not a valid integer"

def cls() -> None:
    system('cls' if system_name=='nt' else 'clear')

def read_once() -> None:
    all_data = database.getAll()
    count = 0
    message = ""
    for collection in all_data:
        count += 1
        if collection["status"] == True:
            message = ':white_check_mark:'
        else:
            message = ':x:'
        message = message + f'[secondary] {str(count)}.- {collection["title"]} [/secondary]\n' 
    console.print(message)

def create() -> None:
    #Get answers
    todo_title = console.input("[primary]Add the Title of the new Todo, [X] to exit: [/primary]")
    if todo_title.lower().strip() == 'x':
        return
    todo_description = console.input("[secondary]Add the description todo, [X] to exit: [/secondary]")
    if todo_description.lower().strip() == 'x':
        return
    
    #Add todo bd
    new_todo = todo()
    try:
        new_todo.title = todo_title
        new_todo.description = todo_description
        database.add(new_todo.create_model)
    except Exception as e:
        console.log(AN_ERROR,e)
            
def read() -> todo:
    #Get answers
    read_todo = todo()
    todo_read = 0
    try:
        todo_read = int(console.input("[primary]Choose a TODO, [0] to exit: [/primary]"))
        if todo_read == 0:
            return read_todo
    except ValueError as e:
        console.log("The input was not a valid integer")
        return read_todo
    if not read_todo.find_and_get(database.getAll(), todo_read - 1):
        console.log(NOTHING_TO_SHOW)
        return
    cls()
    message = read_todo.show_all()
    console.print(message)
    return read_todo

def update() -> None:
    #Get answers
    edit_todo = read()
    if edit_todo.id == 0:
        return
    option_edit = console.input("[primary]What do you need edit [T] Title or [D] Description, [X] to exit ? [/primary]")
    #Edit in database
    if option_edit.lower().strip() == 't':
        edit_todo.title = console.input("[secondary]Write the new Title:[/secondary] :arrow_right: \n")
    elif option_edit.lower().strip() == 'd':
        edit_todo.description = console.input("[secondary]Write the new Description:[/secondary] :arrow_right: \n")
    else:
        return
    try:
        database.updateById(edit_todo.id, edit_todo.create_model())
        cls()
        message = edit_todo.show_all()
        console.print(message)
    except Exception as e:
        console.log(AN_ERROR,e)
        return
    
def delete() -> None:
    #Get the Todo
    delete_todo = read()
    if delete_todo.id == 0:
        return
    try:
        database.deleteById(delete_todo.id)
    except Exception as e:
        console.log(AN_ERROR,e)
        return

def complete() -> None:
    #Get the Todo
    complete_todo = read()
    if complete_todo.id == 0:
        return
    option_complete = console.input("[primary]Do you complete this TODO [Y] Yes or [N] No ? [/primary]")
    #Edit in database
    if option_complete.lower().strip() == 'y':
        complete_todo.status = True
    elif option_complete.lower().strip() == 'n':
        complete_todo.status = False
    
    try:
        database.updateById(complete_todo.id, complete_todo.create_model())
        cls()
        message = complete_todo.show_all()
        console.print(message)
    except Exception as e:
        console.log(AN_ERROR,e)
        return

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
            cls()
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
        cls()
        
if __name__ == "__main__":
    run()
 
