# scatter plot gw kepikirannya buat visualisasi
# grid size vs node explored
# grid size vs time

import matplotlib.pyplot as plt
import numpy as np

# grid size (row x col)
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])

# BFS node explored
Explore_BFS = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, Explore_BFS)

# UCS node explored
Explore_UCS = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91])
plt.scatter(x, Explore_UCS)

plt.xlabel("Grid Size (Row x Col)")
plt.ylabel("Number of Node Explored")
plt.show()