import random

# CONSTANTS
MAX_INCREASE = 0.175  # maximum daily increase of 17.5%
MAX_DECREASE = 0.05   # maximum daily decrease of 5%
MIN_PRICE = 1.0       # minimum allowed price is $1.00
MAX_PRICE = 100.0     # maximum allowed price is $100.00
INITIAL_PRICE = 10.0  # starting price is $10.00
FILENAME = "stock_output.txt"  # name of the file to write output to

price = INITIAL_PRICE
number_of_days = 0

# Open the file for writing
out_file = open(FILENAME, 'w')

# Print the starting price to the file
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate the daily price changes until the price goes out of bounds.
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1

    # 50% chance of increasing or decreasing:
    if random.randint(1, 2) == 1:
        # Price increases by 0 to MAX_INCREASE (up to 17.5%)
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases by 0 to MAX_DECREASE (up to 5%)
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file after simulation is complete
out_file.close()
