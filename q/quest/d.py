# Implement a function that takes three sides of a triangle as input and determines if it's an equilateral, isosceles, or scalene triangle


def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# Example usage
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

triangle_type = classify_triangle(side1, side2, side3)
print("The triangle is:", triangle_type)