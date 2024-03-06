def main():
    print("Test")

    # Get user input
    get_user_expense()

    # Write expense to file.
    save_user_expense()

    # Read file and output expenses
    summarize_user_expense()


def get_user_expense():
    print("Expense input")
    expense_name = input("Enter Expense name: ")
    print(f"Your entered{expense_name}")


def save_user_expense():
    print("Expense saved")


def summarize_user_expense():
    print("Expense output")


if __name__ == "__main__":
    main()
