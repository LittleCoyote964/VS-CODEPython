L1, L2, L3 = input("Please input lengths of three line segments:").split()
L1, L2, L3 = int(L1), int(L2), int(L3)
#Three sides can form a triangle if 
#L1 + L2 > L3, L1 + L3 > L2 etc...

if (L1 + L2 > L3) and (L1 + L3 > L2) and (L3 + L2 > L1):
    print("Yes")
else: 
    print("No")