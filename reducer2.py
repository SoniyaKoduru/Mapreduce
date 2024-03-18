import sys

# Initialize variables
pw = None
pc = 0

# Read input from standard input (STDIN) line by line
for line in sys.stdin:
    # Remove leading and trailing whitespace from the line
    line = line.strip()

    # Split the line into word and count based on tab delimiter
    cw = line.split('\t')[0]
    count = 1  # Since each line represents one word, count is always 1

    # Check if the current word is the same as the previous word
    if pw == cw:
        # If the current word is the same, increment the count
        pc += int(count)
    else:
        # If the current word is different, print the previous word and its count
        if pw:
            print(f"{pw}\t{pc}")

        # Update previous_word to the current word and reset count
        pw = cw
        pc = count

# Print the last word and its count if it exists
if pw:
    print(f"{pw}\t{pc}")
