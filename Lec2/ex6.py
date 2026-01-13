import numpy as np
import matplotlib.pyplot as plt

# Parametric equations for a torus
R, r = 3.0, 1.0
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# 1) Surface plot (default styling)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection="3d")
ax1.plot_surface(x, y, z)
ax1.set_title("Torus – Surface Plot")
plt.show()

# 2) Wireframe plot
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection="3d")
ax2.plot_wireframe(x, y, z, linewidth=0.5)
ax2.set_title("Torus – Wireframe Plot")
plt.show()

# 3) Scatter plot
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection="3d")
ax3.scatter(x.flatten(), y.flatten(), z.flatten(), s=1)
ax3.set_title("Torus – Scatter Plot")
plt.show()

