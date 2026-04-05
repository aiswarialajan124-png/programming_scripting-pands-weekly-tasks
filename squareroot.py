""" Weekly Task 6: squareroot.py
This program calculates the square root of a positive number using the Babylonian method (also known as Heron's method). The user is prompted to enter a positive number, and the program iteratively approximates the square root until it reaches a desired level of accuracy. The final result is printed rounded to one decimal place. If the user enters a negative number, the program will prompt them to enter a positive number. """

# function to calculate square root
def sqrt(number):
    guess = number / 2

    while True:
        newGuess = (guess + number / guess) / 2

        if abs(newGuess - guess) < 0.00001:
            return newGuess
        
        guess = newGuess


# the main program
num = float(input("Please enter a positive number: "))

# to check if number is positive
if num < 0:
    print("Please enter a positive number")

else:
    result = sqrt(num)
    print(f"The square root of {num} is approx. { round(result,1)}.")