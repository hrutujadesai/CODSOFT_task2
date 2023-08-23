import random

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice.\nChoose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or  \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'

def play_again():
    return input("Do you want to play again?\n(Yes/No): ").lower() == 'yes'

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You choose {user_choice}, and the computer choose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)

        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: \nYour score {user_score} \nComputer score {computer_score}")

        if not play_again():
            break

    print("Thanks for playing!")
    print("Exit ")

if __name__ == '__main__':
    main()