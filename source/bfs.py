from general import *
import time
import tracemalloc

class Node_BFS(Node):
    def __init__(self, cur_coord, par_coord, cum_weight, arrival_order):
        super().__init__(cur_coord, par_coord, cum_weight, -1, arrival_order)
        # heu_val diatur ke -1 (tidak digunakan)

class minHeap_BFS(MinHeap):
    def __init__(self):
        super().__init__()
    
    def compareEntry(self, node1, node2):
        if node1.arrival_order < node2.arrival_order:
            return True
        else: return False

def BFS(row, col, grid, start, goal):
    # Memulai perhitungan memori
    tracemalloc.start()
    
    # Menyimpan waktu dimana fungsi mulai berjalan
    startTime = time.perf_counter()
    
    # Menyimpan bobot kumulatif terbaik untuk setiap node
    visitedGrid = [[float('inf') for _ in range(col)] for _ in range(row)] # matrix row x col
    for i in range(row): 
        for j in range(col): 
            visitedGrid[i][j] = -1
    # -1 menyatakan node belum pernah dienqueue
    # -0 menyatakan node sudah pernah dienqueue
    # 1 menyatakan node sudah pernah divisit
    
    # List untuk menyimpan semua node yang sudah dieksplorasi
    explored = []  # elemen dalam format class Node_BFS
    explore_count = 0

    # Priority queue (PQ) untuk menyimpan daftar node yang sudah dienqueue tapi belom divisit
    priorityQueue = minHeap_BFS()
    arrival_order = 0

    # inisialisasi algoritma BFS
    toInsert = Node_BFS(start, [-1, -1], 0, arrival_order)
    priorityQueue.insert(toInsert)              # memasukkan node start ke PQ
    visitedGrid[start[0]][start[1]] = 0         # menandakan node start sudah pernah dienqueue
    arrival_order += 1

    explore = priorityQueue.popMin()            # mengvisit node terkecil pada PQ, disini berarti node start

    # Selama masih ada node yang bisa divisit dan node yang divisit bukan node goal, enqueue tetangga
    while(explore.cur_coord != goal):
        visitedGrid[explore.cur_coord[0]][explore.cur_coord[1]] = 1
        
        # iterasi terhadap semua tetangga dari node yang sedang diexplore (E)
        for neighbor in getNeighbor(explore.cur_coord, row, col, grid):
            
            # Tetangga tidak perlu di enqueue ketika:
            # Tetangga berupa '#' atau dinding
            # Tetangga sudah dimasukkan sebelumnya
            if grid[neighbor[0]][neighbor[1]] == '#' or visitedGrid[neighbor[0]][neighbor[1]] != -1: 
                continue
            
            # Bobot tetangga adalah bobot kumulatif node E ditambah jarak node E ke tetangga
            neighbor_cum_weight = explore.cum_weight + eightD(explore.cur_coord, neighbor)

            toInsert = Node_BFS(neighbor, explore.cur_coord, neighbor_cum_weight, arrival_order)
            arrival_order += 1

            # Memasukkan tetangga ke PQ
            priorityQueue.insert(toInsert)

            # Karakteristik dari BFS dimana tetangga yang sudah dienqueue tidak dienqueue kembali
            visitedGrid[neighbor[0]][neighbor[1]] = 0 # menandakan tetangga sudah pernah dienqueue
        
        
        # Setelah node E selesai dieksplorasi maka masukkan ke list explored
        explored.append(explore)
        explore_count += 1

        # Ambil node E berikutnya dengan mengambil node dengan bobot kumulatif terkecil dari PQ
        explore = priorityQueue.popMin()

        # Kasus: PQ kosong tapi belum eksplorasi node goal
        # Artinya path tidak ditemukan
        if explore.cur_coord == [-1, -1]:
            break
    
    # tadi belum masukin goal ke explored
    # jika goal dipop, tambahkan ke explored agar backtrack bekerja
    if explore.cur_coord == goal:
        explored.append(explore)
        explore_count += 1

    # Menyusun path
    if not explored or explored[-1].cur_coord != goal:
        path = "No path found"
    else:
        # path = "There's path found"
        path = pathBacktrack(explored)

    # durasi fungsi = waktu saat ini - waktu mulai
    elapsedTime = time.perf_counter() - startTime
    current, peakMemory = tracemalloc.get_traced_memory()

    # return n node explored, path cost, path, duration
    return explore_count, explored[-1].cum_weight, path, elapsedTime, peakMemory


# Debug Purpose
def printBFS(explored, goal):
    if not explored or explored[-1][0] != goal:
        print("No path found")
    else:
        printBacktrack(explored)