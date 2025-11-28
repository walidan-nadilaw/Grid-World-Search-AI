from ucs import *
from general import inputGrid, printPath

if __name__ == "__main__":

    # file Membaca input grid dari file .txt
    row, col, grid, start, goal = inputGrid('dataset')

    # Print the inputed grid
    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()

    # UCS
    # Calling the function
    nExp_UCS, pathCost_UCS, path_UCS, time_UCS = UCS(row, col, grid, start, goal)

    # Printing the result
    print("UCS explore\t:", nExp_UCS)
    print("UCS cost\t:", pathCost_UCS[1])
    
    print("UCS path\t: ", end='')
    if(type(path_UCS) is str): print(path_UCS)
    else: printPath(path_UCS)
    
    print(f"UCS time\t: {time_UCS:.6f} seconds")