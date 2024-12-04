#
#
#
#

import sys

def read_file(filename):
    """ opens and reads file with name filename and returns a string of text """
    infile = open(filename, "r")
    text = infile.readlines()
    infile.close()
    return text

def main():
    file = read_file(sys.argv[1])

    # Part One
    final_val = 0
    for line in file:
        prev = None
        prev_diff = None
        valid = True
        line = line.split()
        for i in range(len(line)):
            current = int(line[i])
            if prev is not None:
                diff = prev - current
                if prev_diff is None:
                    prev_diff = diff
                if diff < 0 and prev_diff < 0 and diff >= -3:
                    prev_diff = diff
                elif diff > 0 and prev_diff > 0 and diff <= 3:
                    prev_diff = diff
                else:
                    valid = False
            prev = current
        if valid == True:
            final_val += 1
    print("Amount of safe reports:", final_val)

    # Part Two
    final = 0
    for line in file:
        prev = None
        prev_diff = None
        mistake = 0
        valid = True
        line = line.split()

        for i in range(len(line)):
            current = int(line[i])

            if prev is not None:
                diff = prev - current
                if prev_diff is None:
                    prev_diff = diff
                
                if diff == 0:
                    mistake += 1
                    pass

                if diff < 0 and prev_diff < 0 and diff >= -3 and mistake <= 1:
                   pass

                elif diff > 0 and prev_diff > 0 and diff <= 3 and mistake <= 1:
                    pass

                elif mistake == 0:
                    mistake += 1
                    prev_diff = None
                    pass
                else:
                    valid = False
                    prev_diff = diff

            prev = current
        if valid == True:
            final += 1
    
    print("Amount of safe reports with a problem dampener:", final)

main()