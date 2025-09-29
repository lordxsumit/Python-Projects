import random

computerChoice = random.randint(1,100)      # Generating a random number using import module.
guessCounter = 0

while True: 
    userChoice = int(input("Enter a number of your choice : "))
    guessCounter += 1
    if userChoice == computerChoice :
        print("You guessed the number ")
        break
    elif userChoice > computerChoice :
        print("Your guess is too high")
    else :
        print("Your guess is too low")
        
print(f"You guessed the number in {guessCounter} guesses.")
