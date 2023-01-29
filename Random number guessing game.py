import random
import sys

while True:
    try:
        level = int(input("Level: "))
        assert(level > 0), 'Number must be bigger than 0'
        break
    except (ValueError, AssertionError):
        continue
    else:
        break


x = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < x:
            print("Too small!")
        elif guess > x:
            print("Too large!")
        else:
            sys.exit("Just right!")
    except ValueError:
        continue
