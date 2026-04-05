""" Weekly Task 4: collatz.py

This program takes a positive integer as input, and applies the Collatz conjecture to it. The program will keep applying the rules until the current value becomes 1."""

# Ask user to enter a positive integer
num = int(input("Enter a positive integer: "))

# Keep going until number becomes 1
while num != 1:
    print(num, end=" ")

    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

# Print final 1
print(1)