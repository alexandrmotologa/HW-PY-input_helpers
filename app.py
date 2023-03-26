def inputInt(message):
    # Loop indefinitely until a valid integer is entered
    while True:
        try:
            # Attempt to convert the user input to an integer
            num = int(input(message))
            # If successful, return the integer
            return num
        except ValueError:
            # If the input cannot be converted to an integer, print an error message and loop again
            print("Please enter an integer.")

def inputFloat(message):
    # Loop indefinitely until a valid float is entered
    while True:
        try:
            # Attempt to convert the user input to a float
            num = float(input(message))
            # If successful, return the float
            return num
        except ValueError:
            # If the input cannot be converted to a float, print an error message and loop again
            print("Please enter a float.")

def inputBoolean(message):
    # Loop indefinitely until a valid boolean response is entered
    while True:
        # Convert the user input to lowercase for easier comparison
        response = input(message).lower()
        if response in ("yes", "y", "true", "t", "1"):
            # If the response is one of the true values, return True
            return True
        elif response in ("no", "n", "false", "f", "0"):
            # If the response is one of the false values, return False
            return False
        else:
            # If the response is not valid, print an error message and loop again
            print("Please enter a valid boolean response.")

# Read two integer and calculate their product
n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")
print(n + m)

# Read two floats and calculate their product
x = inputFloat("Enter the first float: ")
y = inputFloat("Enter the second float: ")
print(x * y)

# Prompt the user for a boolean response
response = inputBoolean("Do you have a pet at home? (yes/no) ")
print(response)