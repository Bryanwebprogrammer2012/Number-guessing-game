import random 

attempts = 0

number = random.randrange(1,100)
guess = input("Guess a number between 1 and 100: ")
if guess.isalpha():
    print("You are not allowed to input letters")




while guess != number:
    if guess>"100" or guess<"0":
        print("Invalid input.Try again. ")
        guess = int(input("\nGuess a number between 1 and 100: "))
    
    if guess < number:
        print("Your guess was too low.")
        attempts = attempts + 1
        guess = int(input("\nGuess a number between 1 and 100: "))
   
    else:
        print("your guess is too high")
        attempts = attempts + 1
        guess = int(input("\nGuess a number between 1 and 100: "))
    
    

print("You guessed correctly!")
print("You guessed the answer in", attempts, "attempts.")  