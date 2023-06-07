#HANGMAN GAME
#Step 1

import random

#Task1- Update the word list to use the 'word_list' from hangmanwords.py
from hangmanwordbank import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Task 2 Import the logo from hangmanchart.py and print it at the start of the game.
from hangmanchart import logo
print(logo)

#Task 3 Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Task4 - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Task 5 Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Task 6 Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Task 7 Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Task 8 Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Task 9 - Import the stages from hangman_art.py and make this error go away.
    from hangmanchart import stages
    print(stages[lives])

    # for checking the answer use the code written below line:
#print(f'Pssst, the solution is {chosen_word}.')
