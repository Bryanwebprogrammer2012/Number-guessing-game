import random

number = random.randrange(1,100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("Your guess was too low.")
        guess = int(input("\nGuess a number between 1 and 100: "))
    else:
        print("Your guess was too high.")
        guess = int(input("\nGuess a number between 1 and 100: "))

print("You guessed correctly!")
       
