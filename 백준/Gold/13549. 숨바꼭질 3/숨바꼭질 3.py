import sys
from collections import deque


N, K = map(int,sys.stdin.readline().split())
distance =[-1]*(100001)

if N ==K :
    print(0)
    exit()

distance[N] = 0
q = deque([N])

while q :
    cur = q.popleft()

    nxt = cur *2 
    if 0<= nxt <= 100001 and distance[nxt] == -1 :
        distance[nxt] = distance[cur]
        q.append(nxt)

    for nxt in (cur-1, cur+1) :
        if 0<= nxt <100001 and distance[nxt] ==-1 :
            distance[nxt]= distance[cur] +1
            q.append(nxt)

print(distance[K])
    



