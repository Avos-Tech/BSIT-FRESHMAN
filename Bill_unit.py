def calculate_electric_bill(units):
    rate_per_unit = 5.50  # Rate per unit in peso
    fixed_charge = 20.00  # Fixed charge in peso

    # Calculate total amount
    amount = units * rate_per_unit + fixed_charge

    return amount

# Prompt user for input
name = str(input("Enter the name of bill: "))
units_consumed = float(input("Enter the number of units consumed: "))

# Calculate the bill
bill_amount = calculate_electric_bill(units_consumed)

# Display the bill amount
print(name)
print(f"The electric bill amount is: ₱{bill_amount:.2f}")
