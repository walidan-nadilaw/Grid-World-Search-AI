from general import *
import time

def UCS(row, col, grid, start, goal):
    # Menyimpan waktu dimana fungsi mulai berjalan
    start_time = time.perf_counter()
    
    # Menyimpan bobot akumulatif(? lupa kata yang tepat) terbaik untuk setiap node
    enqueuedWeight = [[float('inf') for _ in range(col)] for _ in range(row)] # matrix row x col
    for i in range(row): 
        for j in range(col): 
            enqueuedWeight[i][j] = -1
    # -1 menyatakan node belum dienqueue
    
    # List untuk menyimpan semua node yang sudah dieksplorasi
    explored = []  # format: [[row node, col node], bobot akumulatif, [row prev, col prev], urutan queue]

    # Priority queue (PQ) untuk menyimpan daftar node yang sudah dienqueue tapi belom divisit
    priorityQueue = MinHeap_NumbVal()
    
    # inisialisasi algoritma ucs
    enqueuedWeight[start[0]][start[1]] = 0      # menyatakan bahwa bobot akumulasi ke start adalah 0
    priorityQueue.insert([[start[0], start[1]], 0, [-1, -1]]) # memasukkan node start ke PQ
    explore = priorityQueue.popMin()            # mengvisit node terkecil pada PQ, disini berarti node start

    # Error handling ketika node start tidak ada
    # jika queue kosong atau sentinel, keluar
    if explore == [[-1, -1], -1, [-1, -1]]:
        print("No path found")
        return

    # Selama masih ada node yang bisa divisit dan node yang divisit bukan node goal, enqueue tetangga
    while(explore != [[-1,-1], -1, [-1,-1]] and explore[0] != goal):
        
        # iterasi terhadap semua tetangga dari node yang sedang diexplore
        for neighbor in getNeighbor(explore[0][0], explore[0][1], row, col, grid):
            
            # jika tetangga berupa '#' atau dinding, maka tidak bisa diexplore
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

    if not explored or explored[-1][0] != goal:
        path = "No path found"
    else:
        path = pathBacktrack(explored)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    # return n node explored, path cost, path, duration
    return len(explored), explored.pop(), path, elapsed_time


# Debug Purpose
def printUCS(explored, goal):
    if not explored or explored[-1][0] != goal:
        print("No path found")
    else:
        printBacktrack(explored)