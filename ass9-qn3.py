def calculate_discounted_price(original_price,discount_percent):
    discount_amount = (original_price * discount_percent) / 100
    discounted_price = original_price - discount_amount
    return discounted_price

original_price = float(input("enter the original price: "))
discount_percent = int(input("enter the discount percent: "))
discounted_price = calculate_discounted_price(original_price, discount_percent)

print(f"discounted price: {discounted_price: .2f}")
