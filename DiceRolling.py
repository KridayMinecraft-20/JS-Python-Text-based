import random

print("Welcome to the Dice Roller!")

while True:
    roll = input("Press Enter to roll the dice, or type 'quit' to stop: ")
    if roll == "quit":
        print("Well then, Goodbye!")
        break
    
    number = random.randint(1, 6)
    print("You rolled the number", number)
