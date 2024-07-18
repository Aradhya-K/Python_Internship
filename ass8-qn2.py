product_quantities = [13, 5, 6, 10, 11]

prices = [1.2, 6.5, 1.0, 4.8, 5.0]

total_price_per_product = [product_quantities[i] * prices[i] for i in range(len(product_quantities))]

total_price = sum(total_price_per_product)

print(total_price)