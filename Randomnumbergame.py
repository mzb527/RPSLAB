import random

# Step 1: Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)
attempts_left = 5  # Allow only five attempts

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 10. You have 5 attempts.")

# Step 2: Use a while loop to control the game flow
while attempts_left > 0:
    try:
        # Step 3: Prompt the user for a guess
        guess = int(input("Enter your guess: "))

        # Step 4: Compare the guess to the secret number
        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Step 5: Decrement attempts and provide feedback
        attempts_left -= 1
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left.")
        else:
            print("Sorry, you've run out of attempts. The correct number was:", secret_number)

    except ValueError:
        # Handle non-integer input gracefully
        print("Invalid input. Please enter a valid number.")