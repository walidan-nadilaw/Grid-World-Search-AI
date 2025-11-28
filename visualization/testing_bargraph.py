# Visualisasi utk rata2:
# path cost / grid size
# path cost / node explored

import matplotlib.pyplot as plt

algo = ['BFS', 'UCS', 'A*']
avg = [0.5, 0.3, 0.2]   

plt.bar(algo, avg)
plt.title('Avg something')
plt.xlabel('Algorithm')
plt.ylabel('Avg something')
plt.show()