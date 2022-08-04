import random

# Life times
lives = 3

# Mysterious words, random selection
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
secret_word = random.choice(words)
# print(secret_word)

clue = list(words)
heart_symbol = u'\u2764'  #represent your lives

guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1


while lives > 0:
    print(clue)
    print('The life times remain: ' + heart_symbol * lives)
    guess = input('Guess letters or whole words: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Error. You have lost one of your lives.\n')
        lives = lives - 1


if guessed_word_correctly:
    print('Winning! The secret word is ' + secret_word)
else:
    print('Losing! The secret word is ' + secret_word)