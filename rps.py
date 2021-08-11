import random

wins  = 0
loss = 0
def rps():
    user = input('rock, paper or scissors?')
    rival = random.choice(['rock', 'paper', 'scissors'])

    if user == rival:
        pass
    elif(
        (user == 'rock' and rival =='scissors')
        or (user == 'scissors' and rival =='paper')
        or (user == 'paper' and rival =='rock')
    ):
        global wins
        wins +=1
    else:
        global loss
        loss += 1
while  input('play? y/n') != 'n':
    rps()
    print(f'wins : {wins}, losses : {loss}')

