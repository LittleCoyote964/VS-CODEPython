x1, y1, x2, y2, x3, y3 = input("Please input three points:").split()
x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)
x3, y3 = int(x3), int(y3)

Area = (1/2) * ((x1*(y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

print("The area is", Area)