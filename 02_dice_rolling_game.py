# This game is made by considering that the user is rolling two dice at a time.

import random

while True:
    choice = input("Enter your choice from (y,n)? : ").lower()
    if choice=='y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'{die1},{die2}')
    
    elif choice=='n':
        print("Thank's for playing")
        break

    else:
        print("Invalid Choice!")