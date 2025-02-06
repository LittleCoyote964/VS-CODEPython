import random
a = random.randint(1,3)
b = random.randint(1,3)
c = random.randint(1,3)
d = random.randint(1,3)

is_Rectangle = False

if a == b and c == d:
    is_Rectangle = True

elif b == c and a == d:
    is_Rectangle = True

elif a == c and b == d:
    is_Rectangle = True


print("Input:", a, b, c, d) 
if is_Rectangle == False:
    print("Output: No")
else: 
    print("Output: Yes")