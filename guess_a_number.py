from random import randint
import os

# Define color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'

LEADERBOARD_FILE = 'Leaderboard.txt'


def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as file:
            scores = [line.strip().split(':') for line in file.readlines()]
            return [(name, int(score)) for name, score in scores]
    return []


# Function to save the leaderboard
def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, 'w') as file:
        for name, score in leaderboard:
            file.write(f"{name}:{score}\n")


# Function to display the leaderboard
def display_leaderboard(leaderboard):
    print(f"\n{MAGENTA}----- Leaderboard -----{RESET}")
    for i, (name, score) in enumerate(sorted(leaderboard, key=lambda x: x[1], reverse=True)):
        print(f"{i + 1}. {name} - {score} points")
    print(f"{MAGENTA}-----------------------{RESET}\n")


welcome_art = f"""{BLUE}
██████╗ ██╗   ██╗███████╗███████╗███████╗     █████╗     ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ██╔══██╗    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗    ███████║    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██╔══██║    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║  ██║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
print(welcome_art)
# Welcome message
print(f'{CYAN}Welcome To The Guess A Number Game')
user = input(f"{YELLOW}Enter your name: {RESET}")

leaderboard = load_leaderboard()

print(f"\n{MAGENTA}--------------------------------{RESET}\n")
print(f"{GREEN}1. Easy Mode (1-10) - 1 point.{RESET}")
print(f"{GREEN}2. Medium Mode (1-100) - 2 points.{RESET}")
print(f"{GREEN}3. Hard Mode (1-1000) - 5 points.{RESET}")
print(f"{GREEN}4. Expert Mode (1-50 with 5 lives) - 20 points.{RESET}")
print(f"{GREEN}5. Custom Mode - Set your own parameters!{RESET}")
print(f"\n{MAGENTA}--------------------------------{RESET}\n")

# Initialize variables
points = 0
lives = 5
mode = int(input(f"{YELLOW}Select mode (1-5): {RESET}"))
is_true = True

# Input validation
if mode not in range(1, 6):
    print(f"{RED}Invalid mode. Please try again.{RESET}")
    mode = int(input(f"{YELLOW}Select mode (1-5): {RESET}"))

# Game loop
while True:
    print(f"\n{MAGENTA}--------------------------------{RESET}\n")
    if mode == 1:
        computer_number = randint(1, 10)
        number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        while computer_number != number:
            if number > computer_number:
                print(f"{RED}Too high! Try again.{RESET}")
            else:
                print(f"{RED}Too low! Try again.{RESET}")
            number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        else:
            print(f"\n{GREEN}Congratulations! You won the game.{RESET}")
            points += 1

    elif mode == 2:
        computer_number = randint(1, 100)
        number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        while computer_number != number:
            if number > computer_number:
                print(f"{RED}Too high! Try again.{RESET}")
            else:
                print(f"{RED}Too low! Try again.{RESET}")
            number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        else:
            print(f"\n{GREEN}Congratulations! You won the game.{RESET}")
            points += 2

    elif mode == 3:
        computer_number = randint(1, 1000)
        number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        while computer_number != number:
            if number > computer_number:
                print(f"{RED}Too high! Try again.{RESET}")
            else:
                print(f"{RED}Too low! Try again.{RESET}")
            number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        else:
            print(f"\n{GREEN}Congratulations! You won the game.{RESET}")
            points += 5

    elif mode == 4:
        computer_number = randint(1, 50)
        number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        while computer_number != number:
            if number > computer_number:
                print(f"{RED}Too high! Try again.{RESET}")
                lives -= 1
            else:
                print(f"{RED}Too low! Try again.{RESET}")
                lives -= 1
            if lives > 0:
                print(f"{YELLOW}Lives remaining: {lives}{RESET}")
                number = int(input(f"{YELLOW}Enter your number: {RESET}"))
            else:
                print(f"{RED}You lost the game. The correct number was {computer_number}.{RESET}")
                break
        else:
            print(f"\n{GREEN}Congratulations! You won the game.{RESET}")
            points += 20
    elif mode == 5:
        custom_range_min = int(input(f"{CYAN}Enter the minimum number for the range: {RESET}"))
        custom_range_max = int(input(f"{CYAN}Enter the maximum number for the range: {RESET}"))
        custom_lives = int(input(f"{CYAN}Enter the number of lives: {RESET}"))
        computer_number = randint(custom_range_min, custom_range_max)
        lives = custom_lives
        print(f"\n{GREEN}Custom Mode: Guess a number between {custom_range_min} and {custom_range_max}!{RESET}")
        number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        while computer_number != number:
            if number > computer_number:
                print(f"{RED}Too high! Try again.{RESET}")
            else:
                print(f"{RED}Too low! Try again.{RESET}")
            number = int(input(f"{YELLOW}Enter your number: {RESET}"))
        else:
            print(f"\n{GREEN}Congratulations! You won the game.{RESET}")
    print(f"\n{MAGENTA}--------------------------------{RESET}\n")
    print(f"{YELLOW}Current Points: {points}{RESET}")

    # End game or restart
    play_again = input(f"{CYAN}Do you want to play again? (y/n): {RESET}").lower()
    if play_again == 'y':
        lives = 5
        is_true = True
        print(f"\n{MAGENTA}--------------------------------{RESET}\n")
        print(f"{GREEN}1. Easy Mode (1-10) - 1 point.{RESET}")
        print(f"{GREEN}2. Medium Mode (1-100) - 2 points.{RESET}")
        print(f"{GREEN}3. Hard Mode (1-1000) - 5 points.{RESET}")
        print(f"{GREEN}4. Expert Mode (1-50 with 5 lives) - 20 points.{RESET}")
        print(f"{GREEN}5. Custom Mode - Set your own parameters!{RESET}")
        print(f"\n{MAGENTA}--------------------------------{RESET}\n")
        mode = int(input(f"{YELLOW}Select mode (1-5): {RESET}"))
    else:
        print(f"\n{MAGENTA}--------------------------------{RESET}\n")
        print(f"{MAGENTA}Thank you for playing, {user}! You finished with {points} points.{RESET}")

        # Update leaderboard if the score is high enough
        leaderboard.append((user, points))
        save_leaderboard(leaderboard)

        # Display the leaderboard
        display_leaderboard(leaderboard)
        break
