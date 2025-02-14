import math
#get the input for the amount of circles
M = int(input("Enter the number of circles: "))
#created list for the circles
circles = []

#will run through the list of circles to enter the x and y as well as the radius
for i in range(M):
    #create an input to gather data
    data = input(f"Enter the data for circle {i+1} (x y r):")
    #will convert the input data into float type variables
    x, y, r = map(float, data.split())     
    circles.append((x, y, r))

#finding the left and right side of the triangle (x - axis)
left = min(x - r for (x, y, r) in circles)
right = max(x + r for (x, y, r) in circles)

#finding the top and bottom (y - axis)
bottom = min(y - r for (x, y, r) in circles)
top = max(y + r for (x, y, r) in circles)

width_of_rec = right - left
height_of_rec = top - bottom
area = width_of_rec * height_of_rec

print("Area of triangle:", area)