#vocabulary trainer
#Word list in dictionaries
word1 = { 
    'word': 'Gravity',
    'meaning': 'property of masses'
    }
word2 = { 
    'word': 'Anti',
    'meaning': 'opposite'
    }
word3 = { 
    'word': 'Ante',
    'meaning': 'before'
    }
#dictionaries in a list
words = [word1, word2, word3]

#helpsvariable
x = True
#iterate through list of words
for entry in words:
    print(entry['word'])
    x = input()
    if x: 
        print(entry['meaning'])
        correct = input('Did you answer it correctly?\n')
        entry.setdefault('correct', ''+correct)

#check changes to words
print(words)

#show correct percentage
x = 0
for entry in words:
    if 'yes' in entry['correct']:
        x +=1
print(f'You got {x} answers right from {len(words)} questions. That\'s {(x/len(words))*100}% correct!')


#not bad for a makeshift answer
#tnoughts to improve
#show you got %wrong or correct depending on how many questions you got right or wrong
#define variable yes with all possible yes annotations
#click to show meaning 
#how to input choices instead of string? 