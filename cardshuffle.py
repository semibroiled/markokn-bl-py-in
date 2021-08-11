import random

cards = [1, 2, 3, 4, 5,6 ,7 ,8, 9, 10, 'K', 'J', 'Q', 'A']

shuffle = []

#for i in range(len(cards)) :
   # rand_select = random.randint(0,len(cards)-1)
    #print(rand_select, cards[rand_select])
    #shuffle.append(cards[rand_select])
    #cards.pop(rand_select)
    #print(cards)


#shuffle = cards.sort

print(shuffle)


def randomizer(x):
    return random.randint(0,x)


print(cards.sort(key = randomizer(len(cards))))
