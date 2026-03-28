import sys
import heapq

N,K = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

heapq.heapify(A)
for _ in range (K-1) :
    heapq.heappop(A)

print(A[0])