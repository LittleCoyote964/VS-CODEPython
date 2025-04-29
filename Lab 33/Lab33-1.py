with open("input1.txt", "r") as infile, open("output1_SID.txt", 'w') as outfile:
    for line in infile:
        word = line.strip()
        print(word)
#reversing now using slicing    
        rev = word[:: -1]
        outfile.write(rev + '\n')