import matplotlib.pyplot as plt
import numpy as np

# Generate random star positions
num_stars = 1000
x = np.random.randn(num_stars)
y = np.random.randn(num_stars)
z = np.random.randn(num_stars)

# Plot the stars
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='black', marker='.', s=1)

# Set plot limits and labels
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot title
plt.title('Milky Way Visualization')

# Show the plot
plt.show()
