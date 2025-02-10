T = int(input("Enter the number of test cases: "))

for t in range(T):

    K = float(input("Enter the cost of one cookie: "))
    N = int(input("Enter the number of cookies John wants to buy: "))
    M = float(input("Enter the amount of money John has: "))

    total_cost = 0

    for i in range(N):
        total_cost += K 
    
    if total_cost > M:
        shortfall = round(total_cost - M, 2)
    else:
        shortfall = 0

    if shortfall > 0:
        print(shortfall)
    else:
        print(0)
