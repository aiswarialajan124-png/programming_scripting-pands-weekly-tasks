""" Weekly Task 8: week08-plottask.py

This program generates a histogram of 1000 random values drawn from a normal distribution with a mean of 5 and a standard deviation of 2. It also plots the function h(x) = x^3 on the same graph. The histogram is normalized to show density, and the function is plotted as a line. The resulting plot is saved as "week08-plot.png" and displayed on the screen."""

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 values from normal distribution (mean=5, std=2)
data = np.random.normal(loc=5, scale=2, size=1000)

# Create x values for h(x) = x^3
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
plt.ylabel("Density /  Function Value")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("week08-plot.png")

plt.show()