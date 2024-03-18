import sys

# Read entire line from STDIN (standard input)
for line in sys.stdin:
    # Get words from lines
    line = line.strip()
    words = line.split()
    # Assign count one to each word 
    for word in words:
        count = 1
        print(word, '\t'', count)
