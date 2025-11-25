from sys import *
from general import *

def UCS(row, col, grid, start, goal):
    
    enqueuedBefore = []
    for i in range(row):
        for j in range(col):
            enqueuedBefore[i][j] = 0
    
    explored = []
    # AccWeightMatrix = []
    # for i in range(row):
    #     rowmat = []
    #     for j in range(col):
    #         rowmat.append(sys.maxsize)
    
    priorityQueue = MinHeap_NumbVal()
    
    priorityQueue.insert([[start[0], start[1]], 0, [-1, -1]])
    explore = priorityQueue.delete(priorityQueue.getMin())
    enqueuedBefore[explore[0][0]][explore[0][1]] = 1

    while(explore != [[-1,-1], -1, [-1,-1]] and explore[0] != goal):
        for neighbor in getNeighbor(explore[0][0], explore[0][1], row, col, grid):
            if (grid[neighbor[0]][neighbor[1]] == '#' or enqueuedBefore[neighbor[0]][neighbor[1]] == 1): continue
            
            neighbor_d = explore[1] + eightD(explore[0], neighbor[0])
            # if (neighbor_d >= enqueuedWeight[neighbor[0], neighbor[1]]): continue
    
            priorityQueue.insert([[neighbor[0], neighbor[1]], neighbor_d, [explore[0][0], explore[0][1]]])
            enqueuedBefore[neighbor[0]][neighbor[1]] = 1
        
        explored.append(explore)
        explore = priorityQueue.delete(priorityQueue.getMin())
        enqueuedBefore[explore[0][0]][explore[0][1]] = 1

    

        