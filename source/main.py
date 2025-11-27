from ucs import *
from general import inputGrid, printPath

if __name__ == "__main__":

    row, col, grid, start, goal = inputGrid('dataset_noPath')

    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()

    nExp_UCS, pathCost_UCS, path_UCS, time_UCS = UCS(row, col, grid, start, goal)
    print("UCS explore\t:", nExp_UCS)
    print("UCS cost\t:", pathCost_UCS[1])
    
    print("UCS path\t: ", end='')
    if(type(path_UCS) is str): print(path_UCS)
    else: printPath(path_UCS)
    
    print(f"UCS time\t: {time_UCS:.6f} seconds")