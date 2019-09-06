# Guessing Game Challenge

# I'm thinking of a number between 1 and 100"
# If your guess is more than 10 away from my number, I'll tell you you're COLD"
# If your guess is within 10 of my number, I'll tell you you're WARM"
# If your guess is farther than your most recent guess, I'll say you're getting COLDER"
# If your guess is closer than your most recent guess, I'll say you're getting WARMER"

import random

num = random.randint(1,100)

guesses = 0

while True:
    
    x = input("Make a guess: ")
    try:
        guess = int(x)
    except ValueError:
        print("Please enter a positive integer! ")
        continue
        
    guesses += 1
       
    if num == guess:
        print('Correct. It took {} guesses.'.format(guesses))
        break
    
    else:
        if guess < 1 or guess > 100:
            print('OUT OF BOUNDS!')
            continue
    
    if guesses == 1:
        if abs(num - guess) > 10:
            print("COLD!")
        else:
            print("WARM!")
        prev_guess = guess

    else:
        if abs(num - prev_guess) > abs(num - guess):
            print("WARMER!")
        elif abs(num - prev_guess) == abs(num - guess):
            print("Same distance from number.")
        else:
            print("COLDER!")
        prev_guess = guess