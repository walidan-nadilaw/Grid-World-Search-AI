from ucs import *
from general import inputGrid

if __name__ == "__main__":

    row, col, grid, start, goal = inputGrid()

    nExp_UCS, pathCost_UCS, path_UCS = UCS(row, col, grid, start, goal)
    print(nExp_UCS)
    print(pathCost_UCS)
    print(path_UCS)

    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()