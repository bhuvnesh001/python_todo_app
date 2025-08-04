import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize file with headers if not exists
def initialize_file():
    try:
        with open(FILENAME, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Description', 'Amount', 'Category'])
    except FileExistsError:
        pass  # File already exists

# Add a new expense
def add_expense():
    try:
        description = input("Enter description: ")
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Travel): ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(FILENAME, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, description, amount, category])
        
        print("✅ Expense added successfully.\n")
    except ValueError:
        print("❌ Invalid amount. Please enter numbers only.\n")

# View all expenses
def view_expenses():
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            print("\n📋 Expense History:")
            print("-" * 60)
            for row in reader:
                print(f"{row[0]} | {row[1]} | ₹{row[2]} | {row[3]}")
            print("-" * 60 + "\n")
    except FileNotFoundError:
        print("❌ No expense file found.\n")

# Main menu
def main():
    initialize_file()

    while True:
        print("📊 Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting the app. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

