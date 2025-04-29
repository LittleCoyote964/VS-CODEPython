with open("input2.txt", "r") as infile, open("output2_SID.txt", "w") as outfile:
    for line in infile:
        word = line.strip()
        print(word)