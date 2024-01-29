import random

name = input("Type your name: ").title()
print("Welcome,", name, "to this adventure!")

answer = input(
    "You have entered a dark alleyway, there is no turning back. The only options you got is a door to your "
    "left and a door to your right. which way would you like to go? left or right: ").lower()

if answer == "left":
    print("You have walked into a monster and have died.")
    exit()
elif answer == "right":
    answer = input("You come to a river of death. Would you like to 'swim' or 'run around: ").lower()
    if answer == "swim":
        print("You have succesfully swam through the river of death. ")
        answer = input(
            "You hear the treasure in front of you....... Are you willing to take it? YOu have a 50% chance of"
            "taking it and satying alive. (yes or no): ")
        if answer == "yes":
            random.choice('live', 'die')
            if answer == 'no':
                print(("You have left without the treasure."))

