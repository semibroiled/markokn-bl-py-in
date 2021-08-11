#practice object oriented programming

class person():

    def __init__(self):
        self.introduce = 'hi! '
        self.height = 50

Amitav = person()
Amitav.name = 'Amitav'

print(Amitav.introduce+'my name is '+ Amitav.name)

class Length():

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.identity = str(value) +' '+unit

a = Length(2.54, 'cm')
print(a.unit, a.value)