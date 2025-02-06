int1, int2, int3 = input("Please enter three integers please:" ).split()
int1, int2, int3 = int(int1), int(int2), int(int3)

if int1 >= int2 and int1 >= int3:
    maxNum = int1
elif int2 >= int3 and int2 >= int1:
    maxNum = int2
else:
    maxNum = int3

if int1 <= int2 and int1 <= int3:
    minNum = int1
elif int2 <= int1 and int2 <= int3:
    minNum = int2
else:
    minNum = int3

print("The maximum number is:", maxNum,)
print("The minimum number is:", minNum)