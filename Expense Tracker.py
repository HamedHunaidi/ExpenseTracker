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
    expense_amount = float(input("Enter Expense amount: "))

    print(f"Your entered {expense_name}, {expense_amount}")

    expense_categories = ["Food", "Home", "Work", "Fun", "Misc"]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            
        print(selected_index)
        break


def save_user_expense():
    print("Expense saved")


def summarize_user_expense():
    print("Expense output")


if __name__ == "__main__":
    main()
