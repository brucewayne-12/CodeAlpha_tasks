import random

words=["python","computer","programming","keyboard","internet"]
word = random.choice(words)
guessed_letters = []
max_attempts=6
attempts=0

while attempts < max_attempts :
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word +=letter
        else:
            display_word += "_" 
    print("\nWord: ",display_word)
    if "_" not in display_word:
        print("Congratulations!  you guessed the word! ")
        break
    guess = input("Enter a letter:").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess !")
    else:
        attempts += 1
        print("Wrong guess! ")
        print("Incorrect guesses: ",attempts)
        
if attempts == max_attempts:
    print("Game Over !")
    print("The word was:",word)
