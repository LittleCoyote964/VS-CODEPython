#def divide(x,y):
x = 10
y = 0
try:
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero!")
else: 
    print("Result:", result)
finally:
    print("Program finished")

#divide(10, 0)
#print()
#divide(3, 2)
       