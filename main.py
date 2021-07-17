import os
import time
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

def read_todo():
    count = 0
    with open("todo.txt", "r", encoding="UTF-8") as f:
        for word in f:
            count = count + 1
            print(f'{count}.- {word}')
    f.close()
    print("")
    input("Succesfully, press enter to continue.....")

def run():
    op = 0
    while op != 3:
        op = 0
        print(
            '''
                MENU TODO
            1.- Add Todo
            2.- Read Todo
            3.- Exit
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
        os.system('clear')
  
if __name__ == '__main__':
    run()