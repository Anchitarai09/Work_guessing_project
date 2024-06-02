import random
def choose_word():
    words=["python","coading","portfolio","courses" ,\
           "programming","code","data","visual","studio"]
    return random.choice(words)

def word_status(word,guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display +=letter
        else:
            display +="_"
    return display

def word_guessing_game():
    secret_word=choose_word()
    guessed_letters=[]
    attempts=7

    print("word Guessing Game")
    print("*********************")
    print("Secret Word:",word_status(secret_word,guessed_letters))
    
    while attempts > 0:
        guess = input("Guess A Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("you must enter a single letter")
            continue

        if guess in guessed_letters:
            print("you already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"No letter '{guess} occurs in the world.")
            print(f"you have {attempts} attempts remaining.")
        else:
            occurrences = secret_word.count(guess)
            print(f"Letter '{guess} occurs {occurrences} times.")
        
        current_status= word_status(secret_word,guessed_letters)
        print("secret word:",current_status)

        if "_" not in current_status:
            print("you won! you guessed the word")
            break
    if "_" in current_status:
        print(f"you ran out of attempts ! The word was: {secret_word}")
word_guessing_game()