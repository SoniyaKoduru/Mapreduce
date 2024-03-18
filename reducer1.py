import sys

# Initialize variables
pw = None
pc = 0
cw = None

# Read input from standard input (STDIN)
for line in sys.stdin:
    line = line.strip()
    cw = line.split('\t')[0]
    count = 1

    # If the current word is the same as the previous word, update the count
    if pw == cw:
        pc += int(count)
    else:
        # If the current word is different from the previous word,
        # print the previous word and its count
        if pw:
            print(f'{pw}\t{pc}')
        # Reset the count and update the previous word to the current word
        pc = count
        pw = cw

# Print the last word and its count
if pw == cw:
    print(f'{pw}\t{pc}')
