import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    """
    Compute the hyperbolic tangent function for the input x.

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    t -- tanh(x)
    """
    return np.tanh(x)

# Generate values for x from -10 to 10
x_values = np.linspace(-10, 10, 100)
# Compute the tanh values for each x
tanh_values = tanh(x_values)

# Plot the tanh function
plt.figure(figsize=(8, 6))
plt.plot(x_values, tanh_values, label='Tanh', color='b')
plt.title('Tanh Function')
plt.xlabel('x')
plt.ylabel('Tanh(x)')
plt.grid(True)
plt.legend()
plt.show()
