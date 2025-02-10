def area_triangle(x1, y1, x2, y2, x3, y3):
    area = (1/2) * abs((x1*(y2 - y3)) + (x2*(y3 - y1)) + (x3*(y1 - y2)))
    print("The area is", area)

x1, y1, x2, y2, x3, y3 = input("Please enter three points:").split()
x1, y1, x2, y2, x3, y3 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3)


area_triangle(x1, y1, x2, y2, x3, y3)
