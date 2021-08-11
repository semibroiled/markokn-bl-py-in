import math
#None and is comparisions
a = [12,124,124]
b =  a 
x = [12,124,124]

print([a is b, a==b, a ==x, a is x])

n = None
if (n is None):
    print('n is None')
#Bool

a = True

if a:
    print ([a is a], [b is a], True+False)

#Numbers

print(10//3, 10%3, 10/3, 2**2)

a_number = 1_123_124
a = a_number
a_sqarenumber = a_number*a_number
print(a_sqarenumber, a*a, a is a_number, b is a_number)

a = 4.2

b = 0b101010

c = 6e23

d = float('nan')



e = float('inf')
print(type(a),type(b), c, d, e, type(e))



print(float(.1+.2), math.isclose(float(.1+.2), .3) )

a = 2 + 3j
b = 3 + 9j

print(a+b)

a+=1

print(a)

#Strings

a ='''a
a'''

b = 'a \n b \r\n c \t tab   d '
print(b)

pathr = r'C:\documents\foo\news.txt'
path =  'C:\documents\foo\news.txt'
print(path, pathr)

text = '''\n Tush! never tell me; I take it much unkindly
That thou, Iago, who hast. had my purse
As if the strings were thine, shouldst know of this.'''

b = text.join(['One', 'Two', 'Three'])
print(b)