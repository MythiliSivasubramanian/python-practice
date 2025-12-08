amount = float(input("Enter purchase amount: "))

if amount >= 1000:
    print("Discount = 20%")
    print("Final Amount =", amount * 0.8)
elif amount >= 500:
    print("Discount = 10%")
    print("Final Amount =", amount * 0.9)
else:
    print("No discount")
    print("Final Amount =", amount)
