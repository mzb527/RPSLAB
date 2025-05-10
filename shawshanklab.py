# Step 1: Define the movie information and cast variables
movie_info = ("The Shawshank Redemption", "Frank Darabont")  # Title and Director (immutable)
cast = ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]  # List of actors (mutable)
new_actor = "William Sadler"

# Step 2: Function to validate inputs
def validate_option(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

# Step 3: Access and print movie information
try:
    print("Movie Title:", movie_info[0])
    print("Director:", movie_info[1])
    print("Original Cast:", ", ".join(cast))
except IndexError:
    print("Error: Unable to retrieve movie information. Check your data structure.")

# Step 4: Simulate adding a new actor with input validation
add_actor = validate_option("Do you want to add a new actor to the cast? (yes/no): ", ["yes", "no"])

if add_actor == "yes":
    try:
        actor_name = input("Enter the name of the new actor: ").strip()
        if actor_name:  # Check if input is not empty
            cast.append(actor_name)
            print(f"Actor '{actor_name}' has been added to the cast.")
        else:
            print("Error: Actor name cannot be empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Step 5: Print the updated cast list
try:
    print("Updated Cast:", ", ".join(cast))
except Exception as e:
    print(f"An error occurred while displaying the updated cast: {e}")