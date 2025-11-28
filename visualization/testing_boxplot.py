# Bocplot kepake banyak sih
# Bisa buat waktu, memori, path cost, node explored, (node explored/grid size)

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
d_1 = np.random.normal(100, 10, 200)
d_2 = np.random.normal(90, 20, 200)
d_3 = np.random.normal(80, 30, 200)
d = [d_1, d_2, d_3]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(d, patch_artist = True,
                notch ='True', vert = 0)

# colors = ['#0000FF', '#00FF00', 
#           '#FFFF00']

# for patch, color in zip(bp['boxes'], colors):
#     patch.set_facecolor(color)

for patch in bp['boxes']:
    patch.set_facecolor('#7cc0d8')

# for whisker in bp['whiskers']:
#     whisker.set(color ='##2596be',
#                 linewidth = 1.5,
#                 linestyle =":")

# changing color and linewidth of
# for cap in bp['caps']:
#     cap.set(color ='#8B008B',
#             linewidth = 2)

for median in bp['medians']:
    median.set(color ='#134b5f',
               linewidth = 1.5)

# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#0b2d39',
              alpha = 0.5)

ax.set_xticklabels(['BFS', 'UCS', 'A*'])
 
plt.title("Sebaran Biaya Path")

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.show()