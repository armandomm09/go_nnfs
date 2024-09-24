import matplotlib.pyplot as plt
import numpy as np

# Coordinates for the inputs and neurons
input_neurons_x = [1, 1, 1, 1]
input_neurons_y = [1, 2, 3, 4]
layer_neurons_x = [3, 3, 3]
layer_neurons_y = [1.5, 2.5, 3.5]

# Create a figure
fig, ax = plt.subplots(figsize=(6,6))

# Plot the inputs
for i in range(len(input_neurons_x)):
    ax.plot(input_neurons_x[i], input_neurons_y[i], 'bo', markersize=15)  # Blue input neurons

# Plot the neurons in the layer
for i in range(len(layer_neurons_x)):
    ax.plot(layer_neurons_x[i], layer_neurons_y[i], 'ro', markersize=15)  # Red neurons in the layer

# Draw lines (connections) between inputs and neurons
for i in range(len(input_neurons_x)):
    for j in range(len(layer_neurons_x)):
        ax.plot([input_neurons_x[i], layer_neurons_x[j]], [input_neurons_y[i], layer_neurons_y[j]], 'gray')

# Set plot limits and hide the axes
ax.set_xlim(0, 4)
ax.set_ylim(0, 5)
ax.axis('off')

# Add labels for inputs and neurons
for i, txt in enumerate(['1', '2', '3', '2.5']):
    ax.text(input_neurons_x[i] - 0.2, input_neurons_y[i] -0.2, f'Input {txt}', fontsize=12, verticalalignment='center')

for i, txt in enumerate(['Neuron 1', 'Neuron 2', 'Neuron 3']):
    ax.text(layer_neurons_x[i] + 0.2, layer_neurons_y[i], txt, fontsize=12, verticalalignment='center')

plt.show()
