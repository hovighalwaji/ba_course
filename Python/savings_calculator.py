print("Monthly Savings Calculator".center(50, "="))
print()

# Step 1: Ask user for monthly income and expenses
income = float(input("Enter your monthly income (in your currency): "))
expenses = float(input("Enter your total monthly expenses: "))

# Step 2: Calculate monthly savings
savings = income - expenses

# Show the results
print("\n" + "-" * 40)
print(f"Monthly Income   : {income:,.2f}")
print(f"Monthly Expenses : {expenses:,.2f}")
print(f"Monthly Savings  : {savings:,.2f}")
print("-" * 40)

# Step 3: Check if savings are enough (more than 20% of income)
required_savings = 0.2 * income  # 20% of income

# Using comparison and logical operators as required
if savings > required_savings and savings > 0:
    print("You are saving enough!")
elif savings >= 0 and savings <= required_savings:
    print("You need to save more.")
elif savings < 0:
    print("You are spending more than you earn!")
else:
    print("You need to save more.")
