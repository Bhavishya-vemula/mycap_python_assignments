import sqlite3


# Create a database connection
db = sqlite3.connect("expenses.db")

# Create a table to store expenses

db.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER, Date TEXT, category TEXT, amount INTEGER)")

# Create a function to add an expense to the database
def add_expense():
    id = input("Input ID: ")
    Date = input("Input date: ")
    category = input("Input category: ")
    amount = input("Input amount: ")
    db.execute("INSERT INTO expenses (id, date, category, amount) VALUES (?, ?, ?, ?)", (id, Date, category, amount))

# Create a function to get all expenses from the database
def get_expenses():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM expenses")
    return cursor.fetchall()

# Create a function to view all expenses
def view_expenses():
    expenses = get_expenses()
    for expense in expenses:
        print("ID:", expense[0], "Date:", expense[1], "Category:", expense[2], "Amount:", expense[3])

# Create a function to delete an expense from the database
def delete_expense():
    id = input("input id: ")
    print("Deleted ID no.: ", id )
    db.execute("DELETE FROM expenses WHERE id = ?", (id,))

    

# Create a main menu
def main_menu():
    print("Expense Recorder")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Delete an expense")
    print("4. Quit")

    # Get the user's choice
    choice = input("Enter your choice: ")

    # Choose the correct function
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Exited expense recorder")
        exit()
# Start the main menu
while True:
 main_menu()
