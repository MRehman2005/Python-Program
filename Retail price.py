def calculate_retail_price(cogs, operating_costs, profit_margin):
    # Calculate retail price
    retail_price = cogs + operating_costs + profit_margin
    return retail_price

# Input values from the user
cogs = float(input("Enter the Cost of Goods Sold (COGS): $"))
operating_costs = float(input("Enter the Operating Costs per unit: $"))
profit_margin = float(input("Enter the Desired Profit Margin: $"))

# Calculate the retail price
retail_price = calculate_retail_price(cogs, operating_costs, profit_margin)

# Output the retail price
print(f"The retail price of the product is: ${retail_price:.2f}")
