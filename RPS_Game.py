import random

options = ["rock", "paper", "scissors"]
lives = 3
win = 1
lose = -1

print("Welcome to the Rock, Paper, Scissors Game!")
print("You have 3 lives. Try to win against the computer.")
print("Rules: Enter 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit the game.")
print("Let's start the game!")
print("If you lose, system 32 will be deleted.")


while True:
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    if user_choice == computer_choice:
        pass
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        win += 1
    else:
        lose += 1

    if lose > win:
        lives -= 1
        print(f"You have {lives} lives remaining.")
        if lives == 0:
            print("Game over! You have lost all your lives. Deleting system 32...")
            break

    if win > lose:
        print(f"You have {lives} lives remaining.")
        if win == 5:
            print("Congratulations! You have won the game!")
            break
