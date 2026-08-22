#guessing game

secret_word = "python"

while True:
    guess = input("What is the programmimg language we using ").lower()
    if guess == secret_word:
        print("You guessed the correct language !!!")
        break
    else:
        print("Incorrect guess try again")