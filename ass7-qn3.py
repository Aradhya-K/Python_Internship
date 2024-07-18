def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
def classify_triangle(a,b,c):
    if a==b and b==c:
        return "Equilateral"
    elif a==b or b==c or a==c:
        return "Isolates"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 ==a**2:
        return "Right-angled"
    else:
        return "Scalene"
def circumcenter_radius(a, b, c):
    if not is_valid_triangle(a, b, c):
        return -1
    if classify_triangle(a, b, c):
        hypotenuse = max(a, b, c)
        return hypotenuse/2
    else:
        return -1
a = 3
b = 4
c = 5
if is_valid_triangle(a, b, c):
    triangle_type = classify_triangle(a, b, c)
    print(f"the triangle is {triangle_type}.")
    radius = circumcenter_radius(a, b, c)
    print(f"the radius of the circumcenter is {radius}.")
else:
    print("the given sides do not form a valid triangle.")