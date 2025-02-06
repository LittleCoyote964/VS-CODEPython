gr1, gr2, gr3 = input("Enter your grade (e.g., A B C) : ").split()

if gr1 == "A":
    gr1 = 4.0
elif gr1 == "B":
    gr1 = 3.0
elif gr1 == "C":
    gr1 = 2.0
elif gr1 == "D":
    gr1 = 1.0
else:
    gr1 = 0.0

if gr2 == "A":
    gr2 = 4.0
elif gr2 == "B":
    gr2 = 3.0
elif gr2 == "C":
    gr2 = 2.0
elif gr2 == "D":
    gr2 = 1.0
else:
    gr2 = 0.0
    
if gr3 == "A":
    gr3 = 4.0
elif gr3 == "B":
    gr3 = 3.0
elif gr3 == "C":
    gr3 = 2.0
elif gr3 == "D":
    gr3 = 1.0
else:
    gr3 = 0.0
    
GPA = (gr1 + gr2 + gr3) / 3

print("Your GPA is: " , round(GPA, 2))
