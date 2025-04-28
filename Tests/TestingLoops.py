try:
    a = 10
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed")


n = int(input("Enter size for addition table: "))
for i in range(1, n + 1):
    for j in range(n + 1):
        print(f"{i * j:3}", end= " ")
    print()