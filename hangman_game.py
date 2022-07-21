import random
import time


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ['january','images','javascript','python','kids','plays','foll','doll','why','me','programmers','solidity','blockchain']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = ''

def play_loop():
    global play_game
    play_game = input('Do you want to play again? y = yes, n = no\n')
    while play_game not in ['Y','y','N','n']:
        error = 'Please enter a value'
        print(error)
        play_game = input('Do you want to play again? y = yes, n = no\n')
        if play_game == 'y':
            main()
            hangman()

        elif play_game == 'n':
            print('Thanks for playing we expect you back')
            exit()
def hangman():
    global count
    global display
    global word
    global already_guessed
    limit = 5
    guess = input('This is the Hangman Word: ' + display + ' Enter your guess \n')
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print("Invalid Input, Try again\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')
    elif guess in already_guessed:
        print("Try another later\n")
    else:
        count  += 1
        if count == 1:
            time.sleep(1)
            print("________ \n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "__|__ \n")
            print("Wrong guess " + str(limit - count) + 'guesses remaining \n')
        elif count == 2:
            time.sleep(1)
            print("________ \n"
                  "| |\n"
                  "| |\n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "__|__ \n")
            print("Wrong guess " + str(limit - count) + 'guesses remaining \n')
        elif count == 3:
            time.sleep(1)
            print("________ \n"
                  "| |\n"
                  "| |\n"
                  "| |\n"
                  "| \n"
                  "| \n"
                  "| \n"
                  "__|__ \n")
            print("Wrong guess " + str(limit - count) + 'guesses remaining \n')
        elif count == 4:
            time.sleep(1)
            print("________ \n"
                  "| |\n"
                  "| |\n"
                  "| |\n"
                  "| O\n"
                  "| \n"
                  "| \n"
                  "__|__ \n")
            print("Wrong guess " + str(limit - count) + 'guesses remaining \n')
        elif count == 5:
            time.sleep(1)
            print("________ \n"
                  "| |\n"
                  "| |\n"
                  "| |\n"
                  "| O\n"
                  "| /|\\n"
                  "| /\\n"
                  "__|__ \n")
            print("Wrong guess You are hanged!!! \n")
            print("The word was: ",already_guessed,word)
            play_loop()
        if word == "_"* length:
            print("Congratulations!! you got the word correctly!")
            play_loop()
        elif count != limit:
            hangman()
main()
hangman()