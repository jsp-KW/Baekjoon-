import sys
import heapq

N = int (sys.stdin.readline())

h = []

counts = []

for i in range (N):
    cnt = int (sys.stdin.readline())
    counts.append(cnt)

for cnt in counts :
    heapq.heappush(h,cnt)

total =  0
while len(h)>1 :
    
    a= heapq.heappop(h)
    b= heapq.heappop(h)

    total += (a+b)
    heapq.heappush(h, a+b)


print (total)

