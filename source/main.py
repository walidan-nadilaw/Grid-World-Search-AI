from astar import *
from ucs import *
from general import inputGrid, printPath

if __name__ == "__main__":

    # Membaca input grid dari file .txt
    # Parameter fungsi inputGrid adalah nama dataset (tanpa .txt)
    row, col, grid, start, goal = inputGrid('input100x100')

    # Mencetak grid yang dibaca
    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()
    print()


#======= UCS =======
    nExp_UCS, pathCost_UCS, path_UCS, time_UCS, memory_UCS = UCS(row, col, grid, start, goal)

    # Mencetak hasil
    print("UCS explore\t:", nExp_UCS)
    print("UCS cost\t:", pathCost_UCS[1])

    print("UCS path\t: ", end='')
    if(type(path_UCS) is str): print(path_UCS)  # ketika tidak ada path dari start menuju goal
    else: printPath(path_UCS)                   # ketika ada path dari start menuju goal
    
    print(f"UCS time\t: {time_UCS:.6f} seconds")
    print("UCS memory\t:", memory_UCS / 1024, "KB")

    path_UCS.pop(0)
    path_UCS.pop()
    for node in path_UCS:
        grid[node[0]][node[1]] = 'P'
    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()
    print()


#======= A STAR =======
    nExp_Astar, pathCost_Astar, path_Astar, time_Astar, memory_Astar = Astar(row, col, grid, start, goal)

    # Mencetak hasil
    print("Astar explore\t:", nExp_Astar)
    print("Astar cost\t:", pathCost_Astar[1])

    print("Astar path\t: ", end='')
    if(type(path_Astar) is str): print(path_Astar)  # ketika tidak ada path dari start menuju goal
    else: printPath(path_Astar)                   # ketika ada path dari start menuju goal
    
    print(f"Astar time\t: {time_Astar:.6f} seconds")
    print("Astar memory\t:", memory_Astar / 1024, "KB")

    path_Astar.pop(0)
    path_Astar.pop()
    for node in path_Astar:
        grid[node[0]][node[1]] = 'P'
    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()
    print()
    