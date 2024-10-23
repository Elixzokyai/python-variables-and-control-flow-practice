def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides"

    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


# Input: lengths of the sides
try:
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    # Determine the type of triangle
    result = triangle_type(side1, side2, side3)
    print(result)
except ValueError:
    print("Please enter valid numbers for the sides.")
