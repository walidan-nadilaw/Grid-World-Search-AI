def getNeighbor(i, j, row, col, grid):
    neighbor = []
    if (i > 0):
        if(grid[i-1, j] != '#'):    neighbor.append([i-1, j])   # utara
    if (i > 0 and j < col):     
        if(grid[i-1, j+1] != '#'):  neighbor.append([i-1, j+1]) # timur laut            
    if (j < col):               
        if(grid[i, j+1] != '#'):    neighbor.append([i, j+1])   # timur
    if (i < row and j < col):
        if(grid[i+1, j+1] != '#'):  neighbor.append([i+1, j+1]) # tenggara
    if (i < row):
        if(grid[i+1, j] != '#'):    neighbor.append([i+1, j])   # selatan
    if (i < row and j > 0):
        if(grid[i+1, j-1] != '#'):  neighbor.append([i+1, j-1]) # barat daya
    if (j > 0):                 
        if(grid[i, j-1] != '#'):    neighbor.append([i, j-1])   # barat
    if (i > 0 and j > 0):
        if(grid[i-1, j-1] != '#'):  neighbor.append([i-1, j-1]) # barat laut
    return neighbor

def createAdjMat(row, col, grid):
    AdjMat = []