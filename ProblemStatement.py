import random

print('\t\tLets play a guessing game!')

def range_input():
    str = input("Enter a range of numbers in the given format: num1-num2\n Eg. 100-200\n")
    c = str.find('-')

    if c==-1:
        print('Enter range in the correct format')
    else:
        firstNum = int(str[:c])
        lastNum = int(str[c+1:])
    
    return firstNum, lastNum

firstNum, lastNum = range_input()
while lastNum < firstNum:
    print('Second number in range should be greater than the first!') 
    firstNum, lastNum = range_input()


luckyNum = random.randint(firstNum, lastNum)

# print('Lucky number is: ', luckyNum) 

numGuess = 4
guess = 1

print('You get four guesses to guess the lucky number that lies in the entered range. Lets get started!')
guessed = False

def guessNumber(guess):
    if guess == 1:
        return 'first'
    elif guess == 2:
        return 'second'
    elif guess == 3:
        return 'third'
    elif guess == 4:
        return 'fourth and last'


while guess <= numGuess:
    n = guessNumber(guess)
    out = f'Enter your {n} guess: '
    print(out)
    try:
        guessedNum = int(input())
    except:
        print('Only integer guesses are allowed!')
        continue
    
    if guessedNum == luckyNum:
        print('Yeah! You identified the number.')
        guessed = True
        break
    elif guessedNum > lastNum or guessedNum < firstNum:
        print('Entered number does not lie in the range')
    elif guessedNum > luckyNum:
        print('Please try again! The number you guessed is too high')
    elif guessedNum < luckyNum:
        print('Please try again! The number you guessed is too small')
    guess += 1

if not guessed:
    print('Oops! All your chances are finished. Better luck next time!')

print('Thank you for playing!')

