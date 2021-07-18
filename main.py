import os
def add_todo():
    #Retrive the comment
    new_todo = input("Add the new todo: ") 
    #Open the file
    with open("todo.txt", "a+", encoding="UTF-8") as f:
        #Move the cursor to the start of the file
        f.seek(0)
        #if file is not empty
        data = f.read(100)
        if len(data) > 0:
            f.write('\n')
        #Add the word in the file
        f.write(new_todo)
    #Close the file
    f.close()
    print("")
    input("Succesfully, press enter to continue.....")
def read():
    count = 0
    with open("todo.txt", "r", encoding="UTF-8") as f:
        for word in f:
            count = count + 1
            print(f'{count}.- {word}')
    f.close()

def read_todo():
    read()
    print("")
    input("Succesfully, press enter to continue.....")

def save_the_todo():
    list_words = []
    with open("todo.txt", "r", encoding="UTF-8") as f:
        for word in f:
            list_words.append(word)
    f.close()
    return list_words
def build_todo(list_words):
    with open("todo.txt", "w", encoding="UTF-8") as f:
        for word in list_words:
            f.write(word)
    f.close
    
def edit_todo():
    read()
    print("")
    number_edit = int(input("What line do you need to edit ?  ")) 
    list_words = save_the_todo()
    print(list_words[number_edit - 1])
    word_edit = input("Edit the description of TODO: ")
    list_words[number_edit - 1] = word_edit + '\n'
    build_todo(list_words)
    input("Succesfully, press enter to continue.....")
    
def delete_todo():
    read()
    print("")
    number_edit = int(input("What line do you need to delete ?  ")) 
    list_words = save_the_todo()
    list_words.pop(number_edit - 1)
    build_todo(list_words)
    input("Succesfully, press enter to continue.....")

def run():
    op = 0
    while op != 5:
        op = 0
        print(
            '''
                MENU TODO
            1.- Add Todo
            2.- Read Todo
            3.- Edit Todo
            4.- Delete Todo
            5.- Exit
            '''
        )
        try:
            op = int(input('Enter a number option .... '))
        except:
            print("Enter a number please")
        print("")
        if op == 1:
            add_todo() 
        if op == 2:
            read_todo()
        if op == 3:
            edit_todo()
        if op == 4:
            delete_todo()
        os.system('clear')
  
if __name__ == '__main__':
    run()