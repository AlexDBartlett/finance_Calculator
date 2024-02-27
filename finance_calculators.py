import math

def get_positive_float(prompt):
    """
    Prompt the user for a positive floating-point number until a valid input is provided.

    Args:
        prompt (str): The message to display to the user as a prompt.

    Returns:
        float: The positive floating-point number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def get_positive_int(prompt):
    """
    Prompt the user for a positive integer until a valid input is provided.

    Args:
        prompt (str): The message to display to the user as a prompt.

    Returns:
        int: The positive integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


def calculate_bond_repayment():
    """
    Calculate the monthly repayment amount for a bond.

    Prompts the user for the value of the house, interest rate, and
    the number of months for repayment. Then, calculates the monthly
    repayment amount using the provided values and prints the result.
    """
    P = get_positive_float("What is the value of the house? £")
    i = get_positive_float("What is the annual interest rate? (in percentage): ") / 100
    n = get_positive_int("How many months do you plan to repay? ")
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print(f"The monthly repayment amount for your bond is: £{repayment:.2f}")


def calculate_investment():
    """
    Calculate the final investment amount with either simple or compound interest.

    Prompts the user for the amount deposited, interest rate, the number of years
    for investment, and the type of interest (simple or compound). Then, calculates
    the final amount after the specified period using the provided values and prints
    the result.
    """
    P = get_positive_float("How much are you depositing? £")
    r = get_positive_float("What is the annual interest rate? (in percentage): ") / 100
    t = get_positive_int("How many years are you investing? ")
    interest = input("Do you want simple or compound interest? ").lower()
    if interest == 'simple':
        A = P * (1 + r * t)
        print(f"The final amount after {t} years with simple interest is £{A:.2f}")
    elif interest == 'compound':
        A = P * math.pow((1 + r), t)
        print(f"The final amount after {t} years with compound interest is £{A:.2f}")
    else:
        print("Invalid choice for interest calculation.")


while True:
    # Printing the menu options
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    print("exit - to exit the program")

    # Asking for user input
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # Handling user choice
    if choice == 'bond':
        calculate_bond_repayment()
    elif choice == 'investment':
        calculate_investment()
    elif choice == 'exit':
        print("Exiting the program. Goodbye!")
        break
    else:
        # If the user enters an invalid choice
        print("Please enter either investment or bond.")
