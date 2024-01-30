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
        print(f"Incorrect PIN. {attempts_left - 1} attempts left.")
        # the number of attempts - 1 to descend from 3 to 0
        pin_check(attempts_left - 1)  # Call the function again with one less attempt


# initiating the PIN check process with the maximum allowed attempt
pin_check(max_attempts)

# Tanya's PIN Check code
# Attempts = 3
# correct_PIN = 0000

# while Attempts != 0:  # executes code block while attempts are not equal to 0
#  supplied_pin = getpass.getpass("Please enter your PIN: ")
# if supplied_pin != correct_PIN:
#    Attempts -= 1   # if attempts are less than or equal to 1
#   print(f"Incorrect PIN, You have {Attempts} Attempts left")
# else:
#    print("Kaching")
#   break
# if pin is correct, terminal prints kaching then break will end while loop