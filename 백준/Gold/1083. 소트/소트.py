import sys


N = int (sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

S = int (sys.stdin.readline())


for i in range (N) :

    if S == 0 : break

    end = min (N-1, i+S)

    max_idx =  i
    for j in range (i+1, end+1) :
        if arr[j] > arr[max_idx] :
            max_idx = j

    
    for j in range (max_idx,i,-1) :
        arr[j], arr[j-1] = arr[j-1], arr[j]

    S = S-(max_idx -i)


print(*arr)
