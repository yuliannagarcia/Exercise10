# Hard-coded PIN
correct_pin = "1234"

# Number of attempts allowed
max_attempts = 3


# Recursive function to check PIN
def check_pin(attempts_left):
    # Base case: if no attempts left, print failure message
    if attempts_left == 0:
        print("Sorry, you have exceeded the maximum number of attempts.")
        return

    # Prompt user for PIN input
    supplied_pin = input("Enter your PIN: ")

    # Check if the supplied PIN matches the correct PIN
    if supplied_pin == correct_pin:
        print("Success! You have entered the correct PIN.")
    else:
        print("Incorrect PIN. You have", attempts_left - 1, "attempts remaining.")
        check_pin(attempts_left - 1)  # Call the function recursively with one less attempt


# Call the function to start PIN check with maximum attempts
check_pin(max_attempts)
