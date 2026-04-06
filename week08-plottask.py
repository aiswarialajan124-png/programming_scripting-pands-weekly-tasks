""" Weekly Task 8: week08-plottask.py

This program generates a histogram of 1000 random values drawn from a normal distribution and plots the function h(x) = x^3 on the same graph.The resulting plot is saved as an image file called "week08-plot.png" 

References: https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
MEAN = 5
STD_DEV = 2
SAMPLE_SIZE = 1000

# Generate random data
data = np.random.normal(loc=MEAN, scale=STD_DEV, size=SAMPLE_SIZE)

# Create x values for function
x = np.linspace(0, 10, 100)
y = x**3

# Create plot
plt.figure(figsize=(8, 6))

# Histogram (density=True)
plt.hist(data, bins=30, density=True, alpha=0.6, label="Normal Distribution")

# Function plot
plt.plot(x, y, linewidth=2, label="h(x) = x^3")

plt.title("Histogram and Function Plot")
plt.xlabel("x values")
plt.ylabel("Density / Function Value")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("week08-plot.png")

# Display the plot
plt.show()