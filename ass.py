def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying the discount if it's 20% or more.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
