import matplotlib.pyplot as plt
import numpy as np

def recaman_sequence(n):
    a0 = 0
    ls = [a0]
    for i in range(n):
        num1 = ls[i] - (i + 1)
        num2 = ls[i] + (i + 1)
        if num1 > 0 and num1 not in ls:
            ls.append(num1)
        else:
            ls.append(num2)
    return ls

n = int(input("Enter an integer number: "))
seq = recaman_sequence(n)

plt.figure()

for i in range(1, len(seq)):
    x1 = seq[i - 1]
    x2 = seq[i]

    center = (x1 + x2) / 2
    radius = abs(x2 - x1) / 2

    theta = np.linspace(0, np.pi, 200)
    x = center + radius * np.cos(theta)

    if i % 2 == 0:        # even n → below x-axis
        y = -radius * np.sin(theta)
    else:                 # odd n → above x-axis
        y = radius * np.sin(theta)

    plt.plot(x, y)

plt.axhline(0)
plt.xlabel("Value")
plt.ylabel("Arcs")
plt.title("Recamán Sequence with Alternating Semi-Circular Arcs")
plt.show()

