import sys
import enchant

#Initialize the English dictionary
english_dict = enchant.Dict("en_US")

# Read entire line from STDIN (standard input)
for line in sys.stdin:
    # Get words from lines
    line = line.strip()
    words = line.lower().split(" ")
    # Assign count one to each word
    for word in words:
        if word != "":
            if not english_dict.check(word):
        	count = 1
        	print(word, '\t'', count)