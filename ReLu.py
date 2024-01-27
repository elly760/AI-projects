import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

# Generate values for x from -10 to 10
x_values = np.linspace(-10, 10, 100)
# Compute the ReLU values for each x
relu_values = relu(x_values)

# Plot the ReLU function
plt.figure(figsize=(8, 6))
plt.plot(x_values, relu_values, label='ReLU', color='r')
plt.title('Rectified Linear Unit (ReLU)')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid(True)
plt.legend()
plt.show()
