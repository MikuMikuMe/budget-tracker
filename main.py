Creating a comprehensive budget tracker involves multiple components such as managing expenses, calculating budgets, and setting financial goals. Below is a simple version of a Python program that provides functionality for tracking expenses, defined budgets, and setting goals. This version stores data in memory; for a more robust implementation, consider integrating with a database or file system to persist data.

```python
import sys

class BudgetTracker:
    def __init__(self):
        """Initializes the budget tracker with empty data sets."""
        self.expenses = []
        self.budgets = {}
        self.goals = []

    def add_expense(self, amount, category):
        """Adds a new expense."""
        try:
            amount = float(amount)
            self.expenses.append({'amount': amount, 'category': category})
            print(f"Added expense: ${amount} in category '{category}'.")
        except ValueError:
            print("Invalid amount entered. Please enter a numerical value.")

    def set_budget(self, category, budget_amount):
        """Sets a budget for a specific category."""
        try:
            budget_amount = float(budget_amount)
            self.budgets[category] = budget_amount
            print(f"Set budget for '{category}': ${budget_amount}")
        except ValueError:
            print("Invalid budget amount. Please enter a numerical value.")

    def show_expenses(self):
        """Displays all recorded expenses and their total."""
        total_spent = 0
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"- ${expense['amount']} in {expense['category']}")
            total_spent += expense['amount']
        print(f"Total spent: ${total_spent:.2f}")

    def check_budget(self):
        """Checks and prints the expenses against set budgets."""
        print("\nBudget Overview:")
        category_expenses = {}
        for expense in self.expenses:
            category_expenses[expense['category']] = category_expenses.get(expense['category'], 0) + expense['amount']

        for category, budget in self.budgets.items():
            spent = category_expenses.get(category, 0)
            print(f"{category} - Spent: ${spent:.2f}, Budget: ${budget:.2f}")
            if spent > budget:
                print(f"  Over budget by: ${spent-budget:.2f}")
            else:
                print(f"  Under budget by: ${budget-spent:.2f}")

    def add_goal(self, description, target_amount):
        """Adds a financial goal."""
        try:
            target_amount = float(target_amount)
            self.goals.append({'description': description, 'target': target_amount})
            print(f"Added financial goal: {description} with target ${target_amount}")
        except ValueError:
            print("Invalid target amount. Please enter a numerical value.")

    def show_goals(self):
        """Displays all financial goals."""
        print("\nFinancial Goals:")
        if not self.goals:
            print("No goals set.")
        else:
            for goal in self.goals:
                print(f"- {goal['description']}: Target = ${goal['target']:.2f}")

def main():
    tracker = BudgetTracker()

    while True:
        print("\n--- Budget Tracker Menu ---")
        print("1. Add Expense")
        print("2. Set Budget")
        print("3. Show Expenses")
        print("4. Check Budgets")
        print("5. Add Financial Goal")
        print("6. Show Goals")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = input("Enter expense amount: ")
            category = input("Enter category: ")
            tracker.add_expense(amount, category)
        elif choice == '2':
            category = input("Enter category: ")
            budget_amount = input("Enter budget amount: ")
            tracker.set_budget(category, budget_amount)
        elif choice == '3':
            tracker.show_expenses()
        elif choice == '4':
            tracker.check_budget()
        elif choice == '5':
            description = input("Enter goal description: ")
            target_amount = input("Enter goal target amount: ")
            tracker.add_goal(description, target_amount)
        elif choice == '6':
            tracker.show_goals()
        elif choice == '7':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
```

### Key Features:
1. **Expense Tracking:** Users can add expenses with a specified amount and category.
2. **Budget Planning:** Users can set budgets for different categories and check their expenses against these budgets.
3. **Financial Goals:** Users can add and view financial goals with target amounts.

### Error Handling:
- The script handles numerical value errors by wrapping float conversions in try-except blocks.
- An invalid choice in the menu prompts the user to enter a correct choice.

### Note:
This is a simple command-line application for illustrative purposes. Enhancements could include input validation, data persistence (using a database or file storage), and a GUI for a more user-friendly interface.