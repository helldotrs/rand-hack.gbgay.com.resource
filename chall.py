import random

try:
    while True:
        # Ask the user for numbers, separated by commas
        input_numbers = input("Enter numbers separated by commas (e.g., 4,5,6): ")

        # Convert the input string to a list of integers
        numbers_list = [int(num.strip()) for num in input_numbers.split(',') if num.strip().isdigit()]

        # Check if the list is not empty
        if numbers_list:
            # Randomly select a number from the list
            chosen_number = random.choice(numbers_list)
            print(f"Randomly selected number: {chosen_number}")
        else:
            print("No valid numbers entered. Please try again.")
        
        print("Enter new numbers or hit CTRL+C to exit.")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
