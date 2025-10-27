import random

upper_bound = 7
lower_bound = 1
max_attempts = 3
secret_number = random.randint(upper_bound, lower_bound)

def get_guess():

    while True:

        guess = int(input("Guess a no. between 1 and 7:"))
        if lower_bound <= guess <= upper_bound:
            return guess
        else:
            print("Go back to nursery cuz u dont know how to count. NO.'s between 1-7: ")

def check_guess(secret_number, guess):
    if guess == secret_number:
        print("The odds were 1 in 7. Bravo you are correct")
    elif guess < secret_number:
        print("Too low..But u r close")
    else:
        print("Too high but u r close")


def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess

        result = check_guess(secret_number, guess)

        if result == "Correct":
            print(f"Congratz...you guessed the number {secret_number} in {attempts} guesses")
            won = True
            break
        else:
            print(f"{result} Try Again :-(")

    
    if not won:
        print("Sorry butchya' ran outta' attempts. The secret no. is {secret_number}")



    if __name__ == "__main__":
        print("Let's play the guessing game!")
        play_game()



        
     


