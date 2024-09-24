import matplotlib.pyplot as plt

# Datos
inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2

# Crear la figura
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar los nodos de entrada
for i, value in enumerate(inputs):
    ax.scatter(0, i, s=2000, c='skyblue', edgecolor='black')
    ax.text(0, i, f'Input {value}', ha='center', va='center', fontsize=10)

# Dibujar el nodo de la neurona
ax.scatter(1.2, 1, s=2000, c='salmon', edgecolor='black')
ax.text(1.2, 1, f'B = {bias}', ha='center', va='center', fontsize=10)

# Dibujar las conexiones
for i in range(len(inputs)):
    ax.plot([0, 1], [i, 1], color='black', linestyle='dashed', linewidth=1)
    ax.text(0.5, (i + 1) / 2, f'W = {weights[i]}', ha='center', fontsize=10)

# Ajustar límites y eliminar ejes
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, len(inputs))
ax.axis('off')

# Título
plt.title('Neural Network Representation with 3 Inputs', fontsize=14)
plt.show()

