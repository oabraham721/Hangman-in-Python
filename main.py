#hangman
import random

chosenW = random.choice(
    ["absence", "abuse", "account", "accident", "beneath", "bend", "benefit", "biology", "bitter", "candidate",
     "campaign", "camera", "capacity", "capture", "deaf", "daughter", "deal", "decorate", "dialogue", "economy",
     "finance", "educate", "efficient", "supportive", "elderly", "flight", "folk", "flame", "frustration", "garbage",
     "gather", "gentle", "global", "hilarious", "intelligence", "jazz", "knife", "longevity", "monument", "nonsense",
     "nobody", "turmeric", "utilize", "sashimi", "reconfigure", "wheat", "yellowish", "zone"])

list = []
usedW = []
n = len(chosenW)

if n >= 8:
    chances = 4
else:
    chances = 3

print('\nWelcome to Hangman, please do the best of your abilities to guess the unknown word\n')
print('You have {} chances to mess up\n'.format(str(chances)))
underScore = '_'

for i in range(0, n):
    list.append(underScore)

print(*list)
userChar = (input('\nGuess any character you\'d like: ', ))

x = 0
y = 0

while True:

    for i in range(n):
        if userChar == chosenW[i]:
            list[i] = userChar
            x = 1
            y += 1

    if x == 1:
        for i in range(1):

                usedW.append(userChar)

        print('\n', *list,end ="")
        print('\t\tUsed: ',end ="")
        print(*usedW)
        userChar = (input('\nCorrect choice, please make another choice: '))
        x = 0
    elif x == 0:
        print('\n', *list, end="")
        print('\t\tUsed: ', end="")
        print(*usedW)
        userChar = (input('\nIncorrect choice you now have {} chance(s) left  please try again: '.format(str(chances-1))))
        chances -= 1

    if chances == 0:
        print('\nYou have ran out of chances and have lost, sorry.\nThe correct word would\'ve been "' + chosenW + '".')
        break
    elif y == (n - 1):
        print('\nCongrats user, you\'ve won the game!!')
        print(chosenW)
        break














