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


def main():
    """
    Main function to run the calculator
    """

    print("="*50)
    print("Welcome to the collaborative calculator")
    print("="*50)
    numbers = get_numbers()
    if len(numbers) == 0:
        print("No numbers entered. Existing")
        return 
    print(f"\n You have entered: {numbers}")
    print("\n What operation would you like to perform")
    print("1. Addition")
    print("2. Multiplication")
    choice = input("Enter your choice 1 or 2: ").strip()

    if choice == "1":
        # TODO: This feature will be implemented by Mohammed
        print("Feature comming soon.")

    elif choice == "2":
        # TODO: This feature will be implemented by Caroline
        print("Feature comming soon.")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()