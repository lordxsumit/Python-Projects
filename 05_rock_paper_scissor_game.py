import random

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ['r', 'p', 's']

while True :
    user_choice = input("Enter your choice from -> Rock / Paper / Scissors as (r/p/s) and 'q' to Exit the game : ").lower()
    computer_choice = random.choice(choices)

    if user_choice == 'q' :
        print("Thank you for playing the game 🙏")
        break

    elif user_choice != 'r' and user_choice != 'p' and user_choice != 's' :
            print("Invalid choice!")
    
    else:
        print(f"You Choose {emojis[user_choice]}")
        print(f"Computer Choose {emojis[computer_choice]}")

        if user_choice == computer_choice :
            print("Draw\n")
        elif user_choice == 'r' and computer_choice == 'p' :
            print("You Lost\n")
        elif user_choice == 'r' and computer_choice == 's' :
            print("You won\n")
        elif user_choice == 'p' and computer_choice == 'r' :
            print("You Won\n")
        elif user_choice == 'p' and computer_choice == 's' :
            print("You Lost\n")
        elif user_choice == 's' and computer_choice == 'p' :
            print("You Won\n")
        elif user_choice == 's' and computer_choice == 'r' :
            print("You Lost\n")