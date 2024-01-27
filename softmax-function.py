import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    e_x = np.exp(x - np.max(x))  # Subtracting the maximum value for numerical stability
    return e_x / e_x.sum(axis=0)

# Generate values for x from -10 to 10
x_values = np.linspace(-10, 10, 100)
# Compute the softmax values for each x
softmax_values = softmax(x_values)

# Plot the softmax function
plt.figure(figsize=(8, 6))
plt.plot(x_values, softmax_values, label='Softmax', color='b')
plt.title('Softmax Function')
plt.xlabel('x')
plt.ylabel('Softmax(x)')
plt.grid(True)
plt.legend()
plt.show()
