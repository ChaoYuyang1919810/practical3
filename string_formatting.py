# Given variables
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# 1. Use f-string formatting to produce:
#    1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about ${cost:,.0f}!")

# 2. Using a for loop with range and f-string formatting, produce:
#    2 ^ 0 is    1
#    2 ^ 1 is    2
#    2 ^ 2 is    4
#    2 ^ 3 is    8
#    2 ^ 4 is   16
#    2 ^ 5 is   32
#    2 ^ 6 is   64
#    2 ^ 7 is  128
#    2 ^ 8 is  256
#    2 ^ 9 is  512
#    2 ^10 is 1024
#
# We choose field widths so that both the exponent and the power-of-two are right-aligned.
for exp in range(11):
    # For the exponent, use a width of 2.
    # For the result (2**exp), use a width of 5.
    print(f"2 ^{exp:>2} is {2**exp:>5}")
