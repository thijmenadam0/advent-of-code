#
#
#
#

import sys
from collections import Counter

def read_file(filename):
    """ opens and reads file with name filename and returns a string of text """
    infile = open(filename, "r")
    text = infile.readlines()
    infile.close()
    return text

def main():
    file = read_file(sys.argv[1])
    line1 = []
    line2 = []
    for line in file:
        line = line.split()
        line1.append(line[0])
        line2.append(line[1])
    line1.sort()
    line2.sort()

    # Part One
    final = 0
    for i in range(len(line1)):
        final += abs(int(line1[i]) - int(line2[i]))
    print("Answer part 1: ", final)

    # Part Two
    counterl2 = Counter(line2)
    final2 = 0
    for i in range(len(line1)):
        if line1[i] in counterl2.keys():
            amount = counterl2[line1[i]]
            final2 += int(line1[i]) * amount

    print("Answer part 2: ", final2)

main()