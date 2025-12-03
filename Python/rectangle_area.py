def calculate_area(length, width):
    """
    This function calculates the area of a rectangle.
    Area = length × width
    """
    area = length * width
    return area


# Main program starts here
print("Welcome to Rectangle Area Calculator!")
print("-" * 40)

# Ask user for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function to get the area
area = calculate_area(length, width)

# Show the result
print(f"\nThe area of the rectangle is: {area}")
print(f"Calculation: {length} × {width} = {area}")

# Check if area is too small
if area < 100:
    print("The area is too small.")
else:
    print("The area is good!")
