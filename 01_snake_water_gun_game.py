# First of all we will take inputs from user in the form of 's', 'w', 'g' referred to as snake, water and gun and then use them to compare with the user's input and play the game ?

import random

print("1 for snake\n2 for water\n3 for gun")
userinput = int(input("Enter your choice :"))

computerChoice = random.randint(1,3)
# choiceList = {1: 's', 2: 'w', 3: 'g'}

while True:
    if computerChoice==1 and userinput==2 :
        print("You Lost the game!")
    elif computerChoice==2 and userinput==3 :
        print("You Lost the game!")
    elif computerChoice==2 and userinput==1 :
        print("You Won the game!")
    elif computerChoice==3 and userinput==2 :
        pass