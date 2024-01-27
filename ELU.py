import numpy as np
import matplotlib.pyplot as plt

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

# Generate values for x from -10 to 10
x_values = np.linspace(-10, 10, 100)
# Compute the ELU values for each x
elu_values = elu(x_values)

# Plot the ELU function
plt.figure(figsize=(8, 6))
plt.plot(x_values, elu_values, label='ELU', color='r')
plt.title('Exponential Linear Unit (ELU)')
plt.xlabel('x')
plt.ylabel('ELU(x)')
plt.grid(True)
plt.legend()
plt.show()
