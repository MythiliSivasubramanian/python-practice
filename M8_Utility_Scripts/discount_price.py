def final_price(price, discount):
    return price - (price * discount / 100)


print("=== Discount Price Calculator ===")

while True:
    try:
        price = float(input("Enter original price: "))
        discount = float(input("Enter discount percentage: "))

        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            continue

        result = final_price(price, discount)
        print(f"Final price after discount: {result:.2f}€")
    except ValueError:
        print("Invalid number. Try again.")

    again = input("Calculate again? (y/n): ").lower()
    if again != "y":
        break
