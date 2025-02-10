import math

k = int(input("Please input k:"))

if k < 0:
    print("Please input a positive number.")

if k > 1:
    for i in range(2, (k // 2) + 1):
        if (k % i) == 0:
            print(k, "is not a prime number")
            break
        
    else:
        print(k, "is a prime number.")

else: print(k, "is not a prime number.")