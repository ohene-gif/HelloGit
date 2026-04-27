import sys
import string

shift = int(sys.argv[1])

letters = ""

# read input
for line in sys.stdin:
    line = line.strip().upper()

    for char in line:
        if char in string.ascii_uppercase:
            letters += chr(((ord(char) - 65 + shift) % 26) + 65)

# build 5-letter blocks
blocks = [letters[i:i+5] for i in range(0, len(letters), 5)]

# print 10 blocks per line
for i in range(0, len(blocks), 10):
    print(" ".join(blocks[i:i+10]))
