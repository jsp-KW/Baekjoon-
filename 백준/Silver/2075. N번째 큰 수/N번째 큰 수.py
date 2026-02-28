import sys
import heapq

N= int(sys.stdin.readline())
q = []

board = [[] for _ in range (N)]

for i in range (N) :
    nums = list(map(int,sys.stdin.readline().split()))
    for number in nums :
        heapq.heappush (q,number)
        if len(q) == N +1:
            heapq.heappop(q)
    
    
print(q[0])

#  i,j 의 숫자는  i-1,j 보다 항상 크다
# n 번째 큰수를 어떻게 찾지? -> 최소힙으로 항상 N개만 가지고 있게 보장하자
# N+1개가 된다면, 힙에서 가장 작은걸 지워버림,
