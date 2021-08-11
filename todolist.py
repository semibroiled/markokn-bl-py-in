class ToDo():

    def __init__(self):
        pass

class ToDoList():

    def __init__(self, listname):
        self.listname = listname
        self.todos = []
      #  self.add = todos.append(None) #how do i makes instance.add('arg') be appened to todos list in this init? 


tdl = ToDoList('groceries')
print(  tdl.listname, tdl.todos)
