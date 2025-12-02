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
    node = [-1, -1]
    for i in range(row):
        for j in range(col):
            if grid[i][j] == char:
                node = [i, j]
                return node

def getNeighbor(i, j, row, col, grid): #return list of list valid neighbor coordinates
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
    def __init__(self, cur_i, cur_j, par_i, par_j, cum_weight, heu_val, arrival_order):
        self.cur_coord = [cur_i, cur_j]
        self.par_coord = [par_i, par_j]
        self.cum_weight = cum_weight        # g(n)  backward cost: weight kumulatif
        self.heu_val = heu_val              # h(n)  forward cost: heuristic value
        self.arrival_order = arrival_order

class MinHeap:
    def __init__(self):
        self.array = []     

    def better(self, node1, node2):
        return

    """Insert a new element into the Min Heap."""
    def insert(self, node):

        self.array.append(node)
        i = len(self.array) - 1
        while i > 0:
            parent_index = (i - 1) // 2
            # Tambahkan logika untuk membandingkan node dengan biaya yang sama
            if (self.better(self.array[i], self.array[parent_index])):
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
            if left < len(self.array) and self.better(self.array[left], self.array[smallest]):
                smallest = left
            if right < len(self.array) and self.better(self.array[right], self.array[smallest]):
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

        if left < n and self.better(self.array[left], self.array[smallest]):
            smallest = left
        if right < n and self.better(self.aarray[right], self.array[smallest]):
            smallest = right
        if smallest != i:
            self.a[i], self.array[smallest] = self.array[smallest], self.array[i]
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
        """Remove and return the root (min) node. Return sentinel if empty."""
        if not self.array:
            return Node(-1, -1, -1, -1, -1, -1, -1)
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

def printBacktrack(nodes):
    # build map coord -> parent (tolerant terhadap beberapa format node)
    parent_map = {}
    if not nodes:
        print("No path found")
        return

    for n in nodes:
        # n may be: [[i,j], cost, [pi,pj]]  or  ([i,j], cost)  or other variants
        coord = None
        parent = None
        try:
            # try canonical: n[0] -> coord
            possible_coord = n[0]
            if isinstance(possible_coord, (list, tuple)) and len(possible_coord) == 2 and all(isinstance(x, int) for x in possible_coord):
                coord = tuple(possible_coord)
        except Exception:
            coord = None

        # try to get parent if available at index 2
        try:
            possible_parent = n[2]
            if isinstance(possible_parent, (list, tuple)) and len(possible_parent) == 2 and all(isinstance(x, int) for x in possible_parent):
                parent = tuple(possible_parent)
        except Exception:
            parent = None

        # fallback: if node itself is a pair like ([i,j], cost), coord may be n[0]
        if coord is None and isinstance(n, (list, tuple)) and len(n) >= 1:
            maybe = n[0]
            if isinstance(maybe, (list, tuple)) and len(maybe) == 2 and all(isinstance(x, int) for x in maybe):
                coord = tuple(maybe)

        if coord is not None:
            parent_map[coord] = parent if parent is not None else (-1, -1)

    # determine goal coordinate from last node in nodes (best-effort)
    last = nodes[-1]
    try:
        goal_coord = tuple(last[0])
    except Exception:
        # if can't determine, abort
        print("No path found")
        return

    # reconstruct path using parent_map
    path = []
    cur = goal_coord
    while cur != (-1, -1):
        path.insert(0, [cur[0], cur[1]])
        cur = parent_map.get(cur, (-1, -1))

    # print path start --> goal
    for i in range(len(path)):
        print(f"({path[i][0]},{path[i][1]})", end="")
        if i < len(path) - 1:
            print(" -> ", end="")

def pathBacktrack(nodes):
    # build map coord -> parent (tolerant terhadap beberapa format node)
    parent_map = {}
    if not nodes:
        print("No path found")
        return

    for n in nodes:
        # n may be: [[i,j], cost, [pi,pj]]  or  ([i,j], cost)  or other variants
        coord = None
        parent = None
        try:
            # try canonical: n[0] -> coord
            possible_coord = n[0]
            if isinstance(possible_coord, (list, tuple)) and len(possible_coord) == 2 and all(isinstance(x, int) for x in possible_coord):
                coord = tuple(possible_coord)
        except Exception:
            coord = None

        # try to get parent if available at index 2
        try:
            possible_parent = n[2]
            if isinstance(possible_parent, (list, tuple)) and len(possible_parent) == 2 and all(isinstance(x, int) for x in possible_parent):
                parent = tuple(possible_parent)
        except Exception:
            parent = None

        # fallback: if node itself is a pair like ([i,j], cost), coord may be n[0]
        if coord is None and isinstance(n, (list, tuple)) and len(n) >= 1:
            maybe = n[0]
            if isinstance(maybe, (list, tuple)) and len(maybe) == 2 and all(isinstance(x, int) for x in maybe):
                coord = tuple(maybe)

        if coord is not None:
            parent_map[coord] = parent if parent is not None else (-1, -1)

    # determine goal coordinate from last node in nodes (best-effort)
    last = nodes[-1]
    try:
        goal_coord = tuple(last[0])
    except Exception:
        # if can't determine, abort
        print("No path found")
        return

    # reconstruct path using parent_map
    path = []
    cur = goal_coord
    while cur != (-1, -1):
        path.insert(0, [cur[0], cur[1]])
        cur = parent_map.get(cur, (-1, -1))

    return path

def printPath(path):
    for i in range(len(path)):
        print(f"({path[i][0]},{path[i][1]})", end="")
        if i < len(path) - 1:
            print(" -> ", end="")
    print()