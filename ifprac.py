#if practice

#length = float(input())
#size = 'small' if length<6 else 'big'

#forloop practice 

#tuple unpaking 

#time = (13,34,00)

#hour, minte, second = time
#print(hour)

#from os import walk 

#a = walk('amitavchrismostafa')

#for directory, dirs, files in a :
#    print(directory, files)

import random 

a = [ random.randint(0,10) for i in range(100)]

b = [num for num in a if num>9]

colors= {
    'red': '#ff0000',
    'green': '#008000',
    'blue': '#0000ff',
}
for color, value in colors.items():
    print(color, value[1:])
    
