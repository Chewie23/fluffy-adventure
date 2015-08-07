file_name = "results.txt"
out1file = open("Pass08042015.txt", "w")
out2file = open("Distinct08042015.txt", "w")

passing = [0, 4, 5]
distinct = [1, 3, 7]

with open(file_name) as f:
    for i, lines in enumerate(f):
        if i in passing:
            out1file.write(lines)

        if i in distinct:
            out2file.write(lines)

        print lines
out1file.close()
out2file.close()
 
