import random

def play_round():
    target = random.randint(1, 10)
    attempts = 5
    print("\nNew Round! You have 5 attempts to guess the number.")
    
    for attempt in range(1, attempts + 1):
        user_choice = input(f"Attempt {attempt}: Guess the TARGET or type QUIT: ")
        
        if user_choice.upper() == "QUIT":
            print("You quit the game.")
            return False, 0  # User quits the game
        
        if not user_choice.isdigit():
            print("Invalid input! Please enter a number or type 'QUIT' to exit.")
            continue
        
        user_choice = int(user_choice)
        
        if user_choice == target:
            print("Success: Correct Guess!")
            return True, attempt  # User guessed correctly
        
        elif user_choice < target:
            print("Your number was too small, take a bigger guess...")
        else:
            print("Your number was too big, take a smaller guess...")
    
    print(f"You've used all your attempts. The correct number was {target}.")
    return False, 0  # User did not guess correctly within the attempts

def main():
    rounds_won = 0
    total_attempts = 0
    
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 10.")
    print("You have 5 attempts to guess the correct number.")
    print("Type 'QUIT' to exit the game at any time.")
    
    while True:
        play_again = input("\nDo you want to play a round? (yes/no): ").lower()
        
        if play_again == 'yes':
            won, attempts = play_round()
            if won:
                rounds_won += 1
            total_attempts += attempts
        elif play_again == 'no' or play_again == 'quit':
            break
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
    
    print("\n- - - - - - - - - - - - - - -")
    print("G A M E   O V E R")
    print(f"Rounds Won: {rounds_won}")
    print(f"Total Attempts Used: {total_attempts}")
    print("- - - - - - - - - - - - - - -")

if __name__ == "_main_":
    main()