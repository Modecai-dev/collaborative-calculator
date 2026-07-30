"""
A simple command line calculator that performs addition and multiplication
"""


def get_numbers():
    """
    Get numbers from user input
    """
    numbers = []
    print("Enter numbers (type 'done' when finished): ")

    while True:
        user_input = input("Enter a number: ").strip()
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number")
    return numbers
