def prime(n: int) -> bool:
   
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    import math
    upper_limit = int(math.sqrt(n)) + 1
    for i in range(3, upper_limit, 2):
        if n % i == 0:
            return False
    return True

user_input = input("Enter an integer: ")
num = int(user_input) 

if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")