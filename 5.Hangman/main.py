import random

word_file = open("C:\\Users\\conno\\Coding projects\\Python\\Hangman\\words.txt", "r")
words = []
correct_guesses = []
incorrect_guesses = []

def get_words(file):
    for word in file:
        words.append(word.removesuffix("\n"))

get_words(word_file)
word_file.close()

def get_random_word(list):
    return list[random.randint(0, len(list)-1)]

def man_hang(x):
    if x == 6:
        print(
            " _____" +
            "\n|    |" +     
            "\n|    " +
            "\n|    " +
            "\n|    " +
            "\n|_____" 
        )
    elif x == 5:
        print(
            " _____" +
            "\n|    |" +     
            "\n|    O" +
            "\n|    " +
            "\n|    " +
            "\n|_____" 
        )
    elif x == 4:
        print(
            " _____" +
            "\n|    |" +     
            "\n|    O" +
            "\n|    |" +
            "\n|    " +
            "\n|_____" 
        )
    elif x == 3:
        print(
            " _____" +
            "\n|    |" +     
            "\n|    O" +
            "\n|   /|" +
            "\n|    " +
            "\n|_____" 
        )
    elif x == 2:
        print(
            " _____" +
            "\n|    |" +     
            "\n|    O" +
            "\n|   /|\\" +
            "\n|    " +
            "\n|_____" 
        )
    elif x == 1:
        print(
            " _____" +
            "\n|    |" +     
            "\n|    O" +
            "\n|   /|\\" +
            "\n|   /" +
            "\n|_____" 
        )
    elif x == 0:
        print(
            " _____" +
            "\n|    |" +     
            "\n|    0" +
            "\n|   /|\\" +
            "\n|   / \\" +
            "\n|_____" 
        )
        print("Game Over, you lose!")

def hide_show_word(guess):
    answer = ""
    for letter in guess:
        if correct_guesses.__contains__(letter):
            answer = answer + letter
        else:
            answer = answer + "*"
    return print("Word to guess: " + answer)

def get_score(guess):
    no = 0
    letter_recurring = []
    for letter in guess:
        if not letter_recurring.__contains__(letter):
            letter_recurring.append(letter)
            no += 1
    return no

def run_game():
    active = True
    word_to_guess = get_random_word(words)
    lives = 6
    score = 0

    print("!!!HANGMAN GAME!!!")

    while active == True:
        if score == get_score(word_to_guess):
            print(
            "\n <3 !!! <3" +
            "\n    \\O/" +
            "\n     |" +
            "\n    / \\"
        )
            print("YOU WON!!! The answer was: " + word_to_guess)
            active = False
            break
        else:
            man_hang(lives)
        
        if lives == 0:
            active = False
            break
        else:
            hide_show_word(word_to_guess)
            cha = input("Enter a charactor: ").capitalize()[0]
        
        if correct_guesses.__contains__(cha) or incorrect_guesses.__contains__(cha):
            print(f"\nThe charactor: {cha}! Has already been guessed!")
        elif word_to_guess.__contains__(cha):
            correct_guesses.append(cha)
            score += 1
            print(f"\nCharactor: {cha}! Is in the word!")
        else:
            incorrect_guesses.append(cha)
            lives -= 1
            print(f"\nCharactor: {cha}! Is not in the word!")

run_game()