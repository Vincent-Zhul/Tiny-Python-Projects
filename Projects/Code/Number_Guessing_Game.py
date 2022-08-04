import random

# Create random number
n = random.randrange(1,100)
# Getting input
guess = int(input("Enter any number: "))

while n != guess: # whether correct
    # less than
    if guess < n:
        print("Too small!")
        guess = int(input("Enter again: "))
    # more than
    elif guess > n:
        print("Too big!")
        guess = int(input("Enter again: "))
    else:
        break
print("Awesome! That's Correct! You have done it!")