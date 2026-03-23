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