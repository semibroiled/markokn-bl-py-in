import random

class RockPaperScissors():

    def __init__(self):
        self.wins = 0
        self.losses = 0
    def play(self):
        user = input('rock, paper or scissors?')
        rival = random.choice(['rock', 'paper', 'scissors'])

        if user == rival:
            pass
        elif(
            (user == 'rock' and rival =='scissors')
            or (user == 'scissors' and rival =='paper')
            or (user == 'paper' and rival =='rock')
        ):
            self.wins += 1
        else:
            self.losses += 1
    def run(self):
        while input('playß y/n') != 'n':
            self.play()
            print(f'wins: {self.wins}, losses: {self.losses}')
    
ami = RockPaperScissors()
ami.run()
