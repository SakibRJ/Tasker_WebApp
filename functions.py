def get_todos(filepath="todos.txt"):
    """Read a text file and return the LIST of to-do items""" #""" is used for documentation; can be accessed by right click>goto>implementations
    with open(filepath, 'r') as local_file:
        local_todo = local_file.readlines()   #'readlines' reads and creates a lIST stored in as local_todo
        return local_todo

def write_todo(filepath, listname_argu):
    """Write the to-do items List in the .txt file"""
    with open(filepath, 'w') as local_file:
        local_file.writelines(listname_argu) #you can pass multiple parameters under the custom function as long as you can replace it later inside the code
                                             #Here 2 parameters are passed; 1. filepath 2. list name which stores the values

print("Hello! Welcome to Todos")

if __name__ == "__main__":
    #print(get_todos("todo.txt"))
    print("Hi this is a functions file; used when imported")