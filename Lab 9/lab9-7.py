num = int(input("Please enter a number:"))

for i in range(num, 1, -1):

    for j in range(num - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")

    print()