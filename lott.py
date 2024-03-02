import random

# Ask the user for numbers to exclude, separated by commas
exclude_input = input("Enter numbers to exclude, separated by commas (e.g., 1,2,3): ")

# Convert the input string to a list of integers
exclude_numbers = [int(num.strip()) for num in exclude_input.split(',') if num.strip().isdigit()]

# Create a list of numbers from 1 to 60, excluding the specified numbers
numbers = [num for num in range(1, 61) if num not in exclude_numbers]

# Function to get a random number and remove it from the list
def get_random_number():
    if numbers:  # Check if there are still numbers in the list
        choice = random.choice(numbers)  # Randomly select a number
        numbers.remove(choice)  # Remove the selected number from the list
        print(f"Random Number: {choice}")
    else:
        print("No more numbers left.")

# Example usage: get a random number (simulate hitting enter)
get_random_number()

# For real-world use, you would call get_random_number()
# each time the user hits enter, after the initial setup.
