import random


def get_user_choice():

    user_choice = str(input("Enter ur choice! rock, paper, or scissors!!!")).lower()
    while user_choice not in ['rock', 'paper', 'scissors']:

        print("Bruh...HOW IN THE WORLD can u enter something wrong. 3 options- rock, paper, or scissors ")
        user_choice = (input("Enter ur choice! rock, paper, or scissors!!!"))

    return user_choice



def get_computer_choice():
    return random.choice (['rock', 'paper', 'scissors'])



def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return ("It's a TIE!! Boring... Let's play again ;)")
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return ("You Win!! Dat's how we do it :-)")        
    
    else:
        return ("Computer Wins! U can do better try again! :-(")
        
 

def play_game():

    print("Welcome to the mightiest game of all... Rock, Paper, Scissors!!!(BTW my name is MR. BOT)")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"YOU = {user_choice}.")
    print(f"MR. BOT = {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    play_game()