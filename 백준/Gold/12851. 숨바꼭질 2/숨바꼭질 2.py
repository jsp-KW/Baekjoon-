import sys

from collections import deque

N,K = map(int,sys.stdin.readline().split())

#걷거나, 순간이동
#걷 : 1초후 x-1, x+1 순간이동: 1초후 2+x

distance = [-1]*(100001)

distance[N] = 0

apporachments =[0]*(100001)
apporachments[N] = 1
q = deque([N])

while q :
    cur = q.popleft()
    if cur == K  :
        break

    teleport = 2*cur
    for walk in (cur-1, cur+1,teleport) :
        nxt = walk
        if 0<= nxt <=100000:
            if distance[nxt] == -1 :# 먼저 도착시
                distance[nxt] = distance[cur] + 1
                apporachments[nxt] = apporachments[cur] 
                q.append(nxt)
            elif distance[nxt] == distance[cur] +1 :
                apporachments[nxt] +=apporachments[cur]

print(distance[K])
print(apporachments[K])