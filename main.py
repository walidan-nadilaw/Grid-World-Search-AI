row = 5
col = 5
grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', 'G'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.']
]
start = [0, 0]
goal = [2, 4]

def getNeighbor(i, j):
    neighbor = []
    if (i > 0):                 neighbor.append([i-1, j])   # utara
    if (i > 0 and j < col):     neighbor.append([i-1, j+1]) # timur laut            
    if (j < col):               neighbor.append([i, j+1])   # timur
    if (i < row and j < col):   neighbor.append([i+1, j+1]) # tenggara
    if (i < row):               neighbor.append([i+1, j])   # selatan
    if (i < row and j > 0):     neighbor.append([i+1, j-1]) # barat daya
    if (j > 0):                 neighbor.append([i, j-1])   # barat
    if (i > 0 and j > 0):       neighbor.append([i-1, j-1]) # barat laut
    return neighbor

# priority queque
def enqueue(q, d):
    m = 0
    for i in range(len(q)):
        if q[i] > q[m]:
            m = i
    q.insert(m, d)

# def UCS(row, col, grid, start, goal)


# for i in range(row):
#     for j in range(col):
#         print(grid[i][j], end=' ')
#     print('\n')