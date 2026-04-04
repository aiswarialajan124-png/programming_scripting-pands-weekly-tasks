import sys
import os

# Check that one comman line arguement is provided
if len(sys.argv) != 2:
    print("Error: No filename provided")
    sys.exit()

# Get filename
filename = sys.argv[1]

# makes sure that it is a text file
if not filename.endswith(".txt"):
    print("Error: File nust be a .txt file")
    sys.exit()

# Check to see if it is in system
if not os.path.isfile(filename):
    print("Error: File  does not exist")
    sys.exit()

# Open file in read mode
file = open(filename, "r")
# Read contents of file into a string
text = file.read()
file.close()

# Count how many times lowercase and uppercase show up
count = text.count("e") + text.count("E")

print(count)