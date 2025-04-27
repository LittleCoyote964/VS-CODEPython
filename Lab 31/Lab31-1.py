import matplotlib.pyplot as plt
import numpy as np

xp = np.array([0, 2, 4, 6, 8, 10])
yp = np.array([0, (2**2), (4**2), (6**2), (8**2), (10**2)])
plt.title('This is for lab 31-1')
plt.xlabel('These are my x values')
plt.ylabel('These are my y values')
plt.plot(xp, yp, marker="o", color="Orange")
plt.show()