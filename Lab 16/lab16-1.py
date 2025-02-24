def divide(x,y):
    try:
     result = x / y
    except ZeroDivisionError:
       print("Cannot divide by zero!")
    else: 
       print("Result:", result)
    finally:
       print("Program finished")

divide(10, 0)
print()
divide(3, 2)
       