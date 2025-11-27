from ucs import *
from general import inputGrid, printPath

if __name__ == "__main__":

    row, col, grid, start, goal = inputGrid()

    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()

    nExp_UCS, pathCost_UCS, path_UCS, time_ucs = UCS(row, col, grid, start, goal)
    print("UCS explore\t:", nExp_UCS)
    print("UCS cost\t:", pathCost_UCS[1])
    print("UCS path\t: ", end='')
    printPath(path_UCS)
    print(f"UCS time\t: {time_ucs:.6f} seconds")