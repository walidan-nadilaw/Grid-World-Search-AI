def getNeighbor(i, j, row, col, grid):
    neighbor = []
    if (i > 0):
        if(grid[i-1, j] != '#'):    neighbor.append([i-1, j])   # utara
    if (i > 0 and j < col):     
        if(grid[i-1, j+1] != '#'):  neighbor.append([i-1, j+1]) # timur laut            
    if (j < col):               
        if(grid[i, j+1] != '#'):    neighbor.append([i, j+1])   # timur
    if (i < row and j < col):
        if(grid[i+1, j+1] != '#'):  neighbor.append([i+1, j+1]) # tenggara
    if (i < row):
        if(grid[i+1, j] != '#'):    neighbor.append([i+1, j])   # selatan
    if (i < row and j > 0):
        if(grid[i+1, j-1] != '#'):  neighbor.append([i+1, j-1]) # barat daya
    if (j > 0):                 
        if(grid[i, j-1] != '#'):    neighbor.append([i, j-1])   # barat
    if (i > 0 and j > 0):
        if(grid[i-1, j-1] != '#'):  neighbor.append([i-1, j-1]) # barat laut
    return neighbor

def eightD(node1, node2):
    if(node1[0] == node2[0]): return 1
    if(node1[1] == node2[1]): return 1
    return (2) ** 0.5

class MinHeap_NumbVal:
    def __init__(self):
        self.a = []     # berisi tuple [[node_i, node_j], value, [parent_i, parent_j]]

    """Insert a new element into the Min Heap."""
    def insert(self, node):
        self.a.append(node)
        i = len(self.a) - 1
        while i > 0 and self.a[(i - 1) // 2][1] > self.a[i][1]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    """Delete a specific element from the Min Heap."""
    def delete(self, value):
        i = -1
        for j in range(len(self.a)):
            if self.a[j][1] == value:
                i = j
                break
        if i == -1:
            return [[-1, -1], -1, [-1, -1]]
        popped = self.a[i]
        self.a[i] = self.a[-1]
        self.a.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.a) and self.a[left][1] < self.a[smallest][1]:
                smallest = left
            if right < len(self.a) and self.a[right][1] < self.a[smallest][1]:
                smallest = right
            if smallest != i:
                self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
                i = smallest
            else:
                break
        return popped

    """Heapify function to maintain the heap property.""" 
    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left][1] < self.a[smallest][1]:
            smallest = left
        if right < n and self.a[right][1] < self.a[smallest][1]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.minHeapify(smallest, n)

    """Search for an element in the Min Heap."""
    def search(self, element):
        for j in self.a:
            if j == element:
                return True
        return False

    def getMin(self):
        return self.a[0] if self.a else None

    def printHeap(self):
        print("Min Heap:", self.a)

def printBacktrack(nodes):
    idx = len(nodes) - 1
    straight = []
    
    straight.insert(0, nodes[idx])

    

# Example Usage
# if __name__ == "__main__":
#     h = MinHeap()
#     values = [10, 7, 11, 5, 4, 13]
#     for value in values:
#         h.insert(value)
#     h.printHeap()
    
#     h.delete(7)
#     print("Heap after deleting 7:", h.a)
    
#     print("Searching for 10 in heap:", "Found" if h.search(10) else "Not Found")
#     print("Minimum element in heap:", h.getMin())