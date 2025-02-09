import math

def distance_from_line(x, y, x1, y1, x2, y2):
    return abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

def calculate_larger_area(x, y, r, x1, y1, x2, y2):
    distance = distance_from_line(x, y, x1, y1, x2, y2)
    if distance >= r:
        return math.pi * r ** 2  
    theta = 2 * math.acos(distance / r)
    segment_area = (r ** 2 / 2) * (theta - math.sin(theta))
    larger_area = math.pi * r ** 2 / 2 + segment_area
    return larger_area

x, y = map(float, input("Enter the circle's origin (x y): ").split())
r = float(input("Enter the radius of the circle: "))
x1, y1, x2, y2 = map(float, input("Enter two points on the line (x1 y1 x2 y2): ").split())
result = calculate_larger_area(x, y, r, x1, y1, x2, y2)

area = round(result, 4) 

print("Area:", area)