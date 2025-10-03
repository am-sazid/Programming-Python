# Function to compute area of rectangle
def rectangle_area(length, width):
    return length * width

# Example usage
l = float(input("Enter length: "))
w = float(input("Enter width: "))

area = rectangle_area(l, w)
print("Area of rectangle:", area)
