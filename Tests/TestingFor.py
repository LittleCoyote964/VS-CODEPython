#using this program just to test the for loop, need to practice on it

#to understand the basic part of the for loop
for counter in range(1, 21, 5):
    print(counter)

print("----------this is another test--------")

#will test to see if I can single out a integer
for counter2 in range(1, 21):
    if counter2 == 3:
        continue
    else:
        print(counter2)
#seems like it works and it singled out the number 3.

print("\nthis will be another test---------\n")
#What if I want to print every iteration in the same line?
#by default it is print the iteration to a a new line.

for counter3 in range(1, 31):
   # print(counter3, end=" ") This will have a space in between the integers. 
    print(counter3, end="")
#the "end=" will change it to the iterations being right next to each other in the same line

print("\n\nThis will be a new test__________\n")

# what if i want to repeat a function several time. "Nested Loop"
for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")
# our result will not show the numbers 1 - 9 three times

print("\n\n-This will be a new test-\n")
#now we want to create a new line after iterating it once. 
for x in range(3):
    for y in range(1, 10):
        print(y, end=" ") #this accounts for one run loop, after this it will exit the for loop and do it all over again
    print()# we add a print statement to add a new line to the loop. 

print("\n\nDifferent test _____________\n")