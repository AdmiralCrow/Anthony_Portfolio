import random

wordlist = ["Empathy", "Compassion", "Courage", "Kindness", "Gratitude", "Resilience", "Patience", "Honesty", "Perseverance", "Generosity", "Diversity", "Humility", "Open-mindedness", "Creativity", "Love", "Respect", "Responsibility", "Forgiveness", "Wisdom"]

pick_word = random.choice(wordlist)
wordpick_len = len(pick_word)

display = []
for x in range(wordpick_len):
    display.append('_')
game_over = False
attempts = 0
max_attempts = 6

def draw_hangman():
    if attempts == 0:
        print(" _________     ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif attempts == 1:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif attempts == 2:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
    elif attempts == 3:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|    ")
        print("|              ")
        print("|              ")
    elif attempts == 4:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|              ")
        print("|              ")
    elif attempts == 5:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|        /     ")
        print("|              ")
    else:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|        / \   ")
        print("|              ")
        print("Oh no, the hangman is dead!")
        print("Game over!")
        return

print("Let's play Hangman!")
while not game_over:
    print()
    draw_hangman()
    print(' '.join(display))
    print("Attempts remaining: " + str(max_attempts - attempts))

    guess = input("Guess a Letter: ").lower()

    if guess in display:
        print("You already guessed that letter. Try again!")
        continue

    found = False
    for position in range(wordpick_len):
        letter = pick_word[position].lower()
        if letter == guess:
            display[position] = pick_word[position]
            found = True

    if not found:
        attempts += 1
        if attempts >= max_attempts:
            game_over = True
            break

    if '_' not in display:
        game_over = True
        break

print()
print(' '.join(display))

if not '_' in display:
    print("Congratulations! You won!")
else:
    print("Sorry, you lost. The word was: " + pick_word)
