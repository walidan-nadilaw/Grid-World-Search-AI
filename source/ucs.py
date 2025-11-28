from general import *
import time
import tracemalloc

def UCS(row, col, grid, start, goal):
    # Memulai perhitungan memori
    tracemalloc.start()
    
    # Menyimpan waktu dimana fungsi mulai berjalan
    startTime = time.perf_counter()
    
    # Menyimpan bobot kumulatif terbaik untuk setiap node
    enqueuedWeight = [[float('inf') for _ in range(col)] for _ in range(row)] # matrix row x col
    for i in range(row): 
        for j in range(col): 
            enqueuedWeight[i][j] = -1
    # -1 menyatakan node belum pernah dienqueue
    
    # List untuk menyimpan semua node yang sudah dieksplorasi
    explored = []  # format: [[row node, col node], bobot kumulatif, [row prev, col prev], urutan queue]

    # Priority queue (PQ) untuk menyimpan daftar node yang sudah dienqueue tapi belom divisit
    priorityQueue = MinHeap_NumbVal()
    
    # inisialisasi algoritma ucs
    enqueuedWeight[start[0]][start[1]] = 0      # menyatakan bahwa bobot kumulatif start adalah 0
    priorityQueue.insert([[start[0], start[1]], 0, [-1, -1]]) # memasukkan node start ke PQ
    explore = priorityQueue.popMin()            # mengvisit node terkecil pada PQ, disini berarti node start

    # Error handling ketika node start tidak ada
    # jika queue kosong atau sentinel, keluar
    if explore == [[-1, -1], -1, [-1, -1]]:
        print("No path found")
        return

    # Selama masih ada node yang bisa divisit dan node yang divisit bukan node goal, enqueue tetangga
    while(explore != [[-1,-1], -1, [-1,-1]] and explore[0] != goal):
        
        # iterasi terhadap semua tetangga dari node yang sedang diexplore (E)
        for neighbor in getNeighbor(explore[0][0], explore[0][1], row, col, grid):
            
            # Tetangga tidak perlu di enqueue ketika:
            # Tetangga berupa '#' atau dinding
            # Tetangga sudah dimasukkan sebelumnya
            if grid[neighbor[0]][neighbor[1]] == '#' or enqueuedWeight[neighbor[0]][neighbor[1]] != -1: 
                continue
            
            # Bobot tetangga adalah bobot kumulatif node E ditambah jarak node E ke tetangga
            neighbor_d = explore[1] + eightD(explore[0], neighbor)

            enqueuedWeight[neighbor[0]][neighbor[1]] = neighbor_d
            # Memasukkan tetangga ke PQ
            priorityQueue.insert([[neighbor[0], neighbor[1]], neighbor_d, [explore[0][0], explore[0][1]]])
        
        # Setelah node E selesai dieksplorasi maka masukkan ke list explored
        explored.append(explore)

        # Ambil node E berikutnya dengan mengambil node dengan bobot kumulatif terkecil dari PQ
        explore = priorityQueue.popMin()

        # Kasus: PQ kosong tapi belum eksplorasi node goal
        # Artinya path tidak ditemukan
        if explore == [[-1, -1], -1, [-1, -1]]:
            break
    
    # tadi belum masukin goal ke explored
    # jika goal dipop, tambahkan ke explored agar backtrack bekerja
    if explore != [[-1, -1], -1, [-1, -1]] and explore[0] == goal:
        explored.append(explore)

    # Menyusun path
    if not explored or explored[-1][0] != goal:
        path = "No path found"
    else:
        path = pathBacktrack(explored)

    # durasi fungsi = waktu saat ini - waktu mulai
    elapsedTime = time.perf_counter() - startTime
    current, peakMemory = tracemalloc.get_traced_memory()

    # return n node explored, path cost, path, duration
    return len(explored), explored.pop(), path, elapsedTime, peakMemory


# Debug Purpose
def printUCS(explored, goal):
    if not explored or explored[-1][0] != goal:
        print("No path found")
    else:
        printBacktrack(explored)