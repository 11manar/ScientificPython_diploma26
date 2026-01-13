from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Let's generate fake data that we can "fit" then 
def f(x, a, phi):
    return np.cos(x**2 + a*x + phi)

#random makes it look like experimental data
x = np.linspace(0, 4, 50)
y = f(x, 1.3, 0.9) + .1*np.random.normal(size=50)
data = np.column_stack((x, y))

np.savetxt("data.txt", data, delimiter=",", header="x,y", comments='')

loaded_data = np.loadtxt("data.txt", delimiter=",", skiprows=1)
x_loaded = loaded_data[:, 0]
y_loaded = loaded_data[:, 1]

# Now fit the model: the parameters omega and phi can be found in the
# `params` vector
params, params_cov = optimize.curve_fit(f, x, y)

print(params)

# plot the data and the fitted curve
plt.plot(x_loaded, y_loaded, 'bx', label="cos(x**2 + a*x + phi)")
plt.plot(x_loaded,f(x_loaded,1.3,0.9),'g-', label="function fitting")
plt.plot(x_loaded, f(x_loaded, *params), 'r-', label="params fitting")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)

plt.show()
