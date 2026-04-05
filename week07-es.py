""" Weekly Task 7: week07-es.py

This program takes a filename as a command line argument, checks if the file exists and is a text file, then counts and prints the number of times the letter "e" (both lowercase and uppercase) appears in the file. If the file does not exist or is not a text file, it will print an appropriate error message.

References: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files"""

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