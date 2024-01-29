import getpass

# the pin
correct_pin = "1234"

# number of attempts allowed
max_attempts = 3


# recursive function to check pin
# check the entered pin against the correct pin. It takes the number of attempts left as an argument.
# inside the function
# def is used to define a function
def pin_check(attempts_left):
    # Base case: if no attempts left, print failure message
    if attempts_left == 0:
        print("You have exceeded the maximum PIN attempts.")
        return

    # if above does not happen enters back to ask user for PIN input
    supplied_pin = input("Enter your PIN: ")

    # if the supplied PIN matches the correct PIN enters this if statement where print correct password or the else
    if supplied_pin == correct_pin:
        print("You have entered the correct PIN.")
    else:
        print("Incorrect PIN.", attempts_left - 1, "attempts left.")
        # the number of attempts - 1 to descend from 3 to 0
        pin_check(attempts_left - 1)  # Call the function again with one less attempt


# initiating the PIN check process with the maximum allowed attempt
pin_check(max_attempts)
