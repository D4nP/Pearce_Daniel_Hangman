import random

print("                                                                               ")
print("               *** WELCOME TO MOVIE HANGMAN ***\n                              ")
print("                                                                               ")
print("                         -----------                                           ")
print("                            |       |                                          ")
print("                            |       0                                          ")
print("                            |       |                                          ")
print("                            |      /|\                                         ")
print("                            |      / \                                         ")
print("                            |                                                  ")
print("                            |                                                  ")
print("                                                                               ")

print("NOTE: This game is played entirely in lower case letters, please make sure the caps lock is off")

NUMBER_OF_CHOICES = 7

file_handler = open('word_list.txt', 'r') # r -> open fie in read mode
words = file_handler.readlines()

new_words = []
for word in words:
    cleaned_word = word.strip()
    new_words.append(cleaned_word)

words = new_words

unknown_word = random.choice(words)

unknown_word_length = len(unknown_word)
print("Guess this word of length:", unknown_word_length)

word_guessed = False
letters = "abcdefghijklmnopqrstuvwxyz"
letters_remaining = list(letters)

print("Word:", unknown_word)

# unknown_word_length -> the number of characters present in the unknown_word selected from the file
current_guesses = []
for i in range(unknown_word_length):
    current_guesses.append('_')

while NUMBER_OF_CHOICES > 0 and not word_guessed:
    print("\nWord:", ' '.join(current_guesses))
    print("Letters Remaining:", ' '.join(letters_remaining))
    print("Lives Remaining:", NUMBER_OF_CHOICES)
    guessed_letter = input("Please guess a letter: ")
    
    '''
    Validate logic:
    1. entered letter should be in the list of letters remaining
    2. entered letter should not be empty (enter character)
    3. entered letter should not be more than 1 characters

    If either one of the above conditions is true, we print the "Please enter a valid input!" to the user and 
    run continue statement
    continue -> skips the rest of statements in the loop a
    '''
    if (guessed_letter not in letters_remaining) or (guessed_letter == "") or (len(guessed_letter) > 1):
        print("\nPlease enter a valid input!")
        continue
    
    # 6. Update the letter remaining by crossing off the entered letter in the letters_remaining list.
    N = len(letters_remaining)
    for i in range(N):
        if guessed_letter == letters_remaining[i]:
            letters_remaining[i] = '-'
    
    guessed_right_letter = False
    N = len(unknown_word)
    # i -> loop variable
    # automatically incremented by 1 after every loop iteration
    # i = 0
    # i = 1
    # i = 2
    # ....
    # i < number of characters in our unknown word
    '''
    unknown word: h a t 
    N = 3
    user_input = 'a'
    for loop:
        unknown_word[i] -> h
        check if h == user_input
    '''
    for i in range(N):
        if unknown_word[i] == guessed_letter:
            guessed_right_letter = True
            current_guesses[i] = guessed_letter
    
    if not guessed_right_letter:
        NUMBER_OF_CHOICES -= 1
    else:
        if '_' not in current_guesses:
            word_guessed = True

print()
print('---------')
print('RESULT')
print('---------')
if word_guessed:
    print("CONGRATULATIONS YOU WIN!")
else:
    print("YOU LOSE")
    print("The word was:", unknown_word)


'''
word_guessed = False
NUMBER_OF_CHOICES = 7

- user has guessed the word correctly
- number of choices can reach 0

loop until either of above cases have become true:
    1. print the current word (Ex: _ _ _ e _ _)
    2. print letters remaining (Ex: a b c d .... z)
    3. print lives remaining
    4. take input from a user
    5. valid the user input (user input can be only lower case alphabets)
    6. Update the letter remaining by crossing off the entered letter in the list.
    7. Check if user entered character is in the unknown word (basically it's a correct input)

    8. If invalid input entered, decrese the NUMBER_OF_CHOICES by 1
    9. Otherwise check if the user has guessed all the letter in the word.

    Ex:
        h a t

        _ _ _
        _ a _
        h a _
        h a t

    -------------------------------------------------
    unknown word: h a t
    user input: a

    guess_right_letter = False
    loop through all the characters in unknown work
        we check if the current character is equal to the user iput
        if user input matches current letter:
            guess_right_letter = True
'''
