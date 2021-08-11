#todolist

#empty dict todo
todo = {

}

num = 0
while True:

    entry = input('Input a task:\n')

    num+=1
    todo.setdefault(num, entry)

 
    
    print(f' Your tasks are {todo.items()}')

#I can increase a list with this, but i cant check them off
