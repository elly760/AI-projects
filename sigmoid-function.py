# Importing the sigmoid function
import numpy as np
import matplotlib.pyplot as plt

# Defining the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# number_x = 0
# print(sigmoid(number_x))

# For array input
x_array_numbers = np.array([-1, 0, 1])
print(sigmoid(x_array_numbers))  # Output will be an array of sigmoid values for each element

# ploting the graph for sigmoid function
# Generate values for x from -10 to 10
x_values = np.linspace(-10, 10, 100)
# Compute the sigmoid values for each x_values
sigmoid_values = sigmoid(x_values)

# Plot the sigmoid function
plt.figure(figsize=(8, 6))
plt.plot(x_values, sigmoid_values, label='Sigmoid', color='r')
plt.title('SIGMOID FUNCTION')
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.grid(True)
plt.show()