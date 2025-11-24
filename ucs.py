from sys import *
from general import *

# insert untuk priority queque
def enqueue(q, d):
    m = 0
    for i in range(len(q)):
        if q[i] >= d:
            m = i
    q.insert(m, d)

def UCS(row, col, grid, start, goal):
    AccWeightMatrix = []
    for i in range(row):
        rowmat = []
        for j in range(col):
            rowmat.append(sys.maxsize)

    priorityQueue = []

    for neighbor in getNeighbor(start[0], start[1], row, col, grid):
        enqueue(priorityQueue, neighbor: 'a')

    explored = priorityQueue.pop(0)

    while (explored != goal):
        
    return 1