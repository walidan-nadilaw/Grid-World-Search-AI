def inputGrid(datasetName):
    with open('dataset/'+datasetName+'.txt') as file:
        line = file.readline().strip().split()
        row, col = list(map(int, line))
        
        grid = []
        for _ in range(row): 
            line = file.readline().strip().split()
            grid.append(list(line))
        
        start = searchChar("S", row, col, grid)
        goal = searchChar("G", row, col, grid)

        return row, col, grid, start, goal

def searchChar(char, row, col, grid):
    Node = [-1, -1]
    for i in range(row):
        for j in range(col):
            if grid[i][j] == char:
                Node = [i, j]
                return Node

def getNeighbor(coor, row, col, grid): #return list of list valid neighbor coordinates
    i, j = coor
    neighbor = []
    if i > 0:
        if grid[i-1][j] != '#':    neighbor.append([i-1, j])   # utara
    if i > 0 and j < col-1:
        if grid[i-1][j+1] != '#':  neighbor.append([i-1, j+1]) # timur laut            
    if j < col-1:               
        if grid[i][j+1] != '#':    neighbor.append([i, j+1])   # timur
    if i < row-1 and j < col-1:
        if grid[i+1][j+1] != '#':  neighbor.append([i+1, j+1]) # tenggara
    if i < row-1:
        if grid[i+1][j] != '#':    neighbor.append([i+1, j])   # selatan
    if i < row-1 and j > 0:
        if grid[i+1][j-1] != '#':  neighbor.append([i+1, j-1]) # barat daya
    if j > 0:                 
        if grid[i][j-1] != '#':    neighbor.append([i, j-1])   # barat
    if i > 0 and j > 0:
        if grid[i-1][j-1] != '#':  neighbor.append([i-1, j-1]) # barat laut
    return neighbor

def euclidean8d(node1, node2): #return float jarak heuristik antara start dan goal
    dx = abs(node1[0] - node2[0])
    dy = abs(node1[1] - node2[1])
    
    if(dy > dx):
        return (dy-dx) + dx * (2)**0.5
    else:
        return (dx-dy) + dy * (2)**0.5

def eightD(node1, node2): #return float jarak antara tetangga
    if(node1[0] == node2[0]): return 1
    if(node1[1] == node2[1]): return 1
    return (2) ** 0.5

class Node:
    def __init__(self, coord, parent, cum_weight, heu_val, arrival_order) -> None:
        self.cur_coord: list[int]= coord
        self.parent_coord: list[int] = parent
        self.cum_weight: float = cum_weight        # g(n)  backward cost: weight kumulatif
        self.heu_val: float = heu_val              # h(n)  forward cost: heuristic value
        self.arrival_order: int = arrival_order

class MinHeap:
    def __init__(self):
        self.array = []     

    def compareEntry(self, node1, node2):
        return

    """Insert a new element into the Min Heap."""
    def insert(self, Node):

        self.array.append(Node)
        i = len(self.array) - 1
        while i > 0:
            parent_index = (i - 1) // 2
            # Tambahkan logika untuk membandingkan Node dengan biaya yang sama
            if (self.compareEntry(self.array[i], self.array[parent_index])):
                self.array[i], self.array[parent_index] = self.array[parent_index], self.array[i]
                i = parent_index
            else:
                break

    """Delete a specific element from the Min Heap."""
    def delete(self, value):
        i = -1
        for j in range(len(self.array)):
            if self.array[j].cur_coord == value:
                i = j
                break
        if i == -1:
            return Node(-1, -1, -1, -1, -1, -1, -1)
        popped = self.array[i]
        self.array[i] = self.array[-1]
        self.array.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.array) and self.compareEntry(self.array[left], self.array[smallest]):
                smallest = left
            if right < len(self.array) and self.compareEntry(self.array[right], self.array[smallest]):
                smallest = right
            if smallest != i:
                self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
                i = smallest
            else:
                break
        return popped

    """Heapify function to maintain the heap property.""" 
    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.compareEntry(self.array[left], self.array[smallest]):
            smallest = left
        if right < n and self.compareEntry(self.array[right], self.array[smallest]):
            smallest = right
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.minHeapify(smallest, n)

    """Search for an element in the Min Heap."""
    def search(self, element):
        for j in self.array:
            if j == element:
                return True
        return False

    def getMin(self):
        return self.array[0] if self.array else None
    
    def popMin(self):
        """Remove and return the root (min) Node. Return sentinel if empty."""
        if not self.array:
            return Node([-1, -1], [-1, -1], -1, -1, -1)
        root = self.array[0]
        if len(self.array) == 1:
            self.array.pop()
            return root
        # pindahkan last ke root lalu heapify
        self.array[0] = self.array.pop()
        self.minHeapify(0, len(self.array))
        return root

    def printHeap(self):
        print("Min Heap:", self.array)

def pathBacktrack(exploredList: list[Node]) -> list[Node]:

    NodeCount :int = len(exploredList)
    path :list[Node] = []
    currentNode :list[int]= exploredList[-1].cur_coord

    for i in range(NodeCount-1, -1, -1):
        if exploredList[i].cur_coord == currentNode:
            path.append(exploredList[i].cur_coord)
            currentNode = exploredList[i].parent_coord
            if currentNode == [-1, -1]:
                break

    return path[::-1]  # reverse path
    # Slicing Time: 3.000000106112566e-06
    # Reversing Time: 7.999999979801942e-06