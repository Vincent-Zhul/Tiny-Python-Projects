import random

# Set Max and Min value
min_val = 1
max_val = 6

# Whether continue
roll_again = "yes"

# Circulate
while roll_again == "yes" or roll_again == "y":
    print("Start rolling dice")
    print("Dice value is: ")

    # Round 1
    print(random.randint(min_val, max_val))

    # Round 2
    print(random.randint(min_val, max_val))

    # Whether continue
    roll_again = input("Continue to roll dice? (if yes, enter yes or y): ")