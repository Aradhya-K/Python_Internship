def calculate_area(side_length):
    return side_length ** 2

side_length = float(input("Enter the side length of the square:"))

area = calculate_area(side_length)

print(f"The area of the square is:{area}")