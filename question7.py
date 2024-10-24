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
    Tri1 = float(input("Enter the length of side 1: "))
    Tri2 = float(input("Enter the length of side 2: "))
    Tri3 = float(input("Enter the length of side 3: "))

    # Determine the type of triangle
    result = triangle_type(Tri1, Tri2, Tri3)
    print(result)
except ValueError:
    print("Please enter valid numbers for the sides.")
