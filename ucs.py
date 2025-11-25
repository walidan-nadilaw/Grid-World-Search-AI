from general import *

def UCS(row, col, grid, start, goal):
    
    # simpan best-known g-cost untuk tiap sel
    enqueuedWeight = [[float('inf') for _ in range(col)] for _ in range(row)]
    
    explored = []
    priorityQueue = MinHeap_NumbVal()
    
    enqueuedWeight[start[0]][start[1]] = 0
    priorityQueue.insert([[start[0], start[1]], 0, [-1, -1]])
    explore = priorityQueue.popMin()

    # jika queue kosong atau sentinel, keluar
    if explore == [[-1, -1], -1, [-1, -1]]:
        print("No path found")
        return

    while(explore != [[-1,-1], -1, [-1,-1]] and explore[0] != goal):
        for neighbor in getNeighbor(explore[0][0], explore[0][1], row, col, grid):
            if grid[neighbor[0]][neighbor[1]] == '#': 
                continue
            
            neighbor_d = explore[1] + eightD(explore[0], neighbor)
            # hanya enqueue jika cost lebih baik
            if neighbor_d < enqueuedWeight[neighbor[0]][neighbor[1]]:
                enqueuedWeight[neighbor[0]][neighbor[1]] = neighbor_d
                priorityQueue.insert([[neighbor[0], neighbor[1]], neighbor_d, [explore[0][0], explore[0][1]]])
        
        explored.append(explore)
        explore = priorityQueue.popMin()
        if explore == [[-1, -1], -1, [-1, -1]]:
            break
    
    # jika goal dipop, tambahkan ke explored agar backtrack bekerja
    if explore != [[-1, -1], -1, [-1, -1]] and explore[0] == goal:
        explored.append(explore)

    printUCS(explored, goal)

def printUCS(explored, goal):
    if not explored or explored[-1][0] != goal:
        print("No path found")
    else:
        printBacktrack(explored)