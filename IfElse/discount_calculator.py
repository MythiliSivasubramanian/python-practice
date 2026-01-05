"""
Discount Calculator :
Calculating the discount and final amount based on the purchase amount:
- 20% discount for purchases >= 1000
- 10% discount for purchases >= 500
- No discount for purchases < 500
"""

# Prompting user to enter purchase amount
amount = float(input("Enter purchase amount: "))

# Applying discount based on amount and printing the result
if amount >= 1000:
    print("Discount = 20%")
    print("Final Amount =", amount * 0.8)
elif amount >= 500:
    print("Discount = 10%")
    print("Final Amount =", amount * 0.9)
else:
    print("No discount")
    print("Final Amount =", amount)
