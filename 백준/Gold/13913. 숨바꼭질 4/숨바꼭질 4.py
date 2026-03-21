import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())

# 수빈 N ,동생 K
# X, 1초뒤 X-1, X+1 / 순간이동시 1초뒤 2X
# 가장 빠른 시간이 몇초후인지

distance =[-1]*(100001)

q = deque([N])
parent =[-1]*(100001)

distance[N] = 0
while q :
    cur = q.popleft()
    if cur == K :
        print(distance[K])
        break
    nxt1 = cur +1
    nxt2 = cur -1 
    nxt3 = cur*2

    
    if 0<= nxt1 < 100001 :
        if distance[nxt1] == -1 :
            distance[nxt1] = distance[cur] +1
            parent[nxt1] = cur
            q.append(nxt1)

    
    if 0<= nxt2 < 100001 :
        if distance[nxt2] == -1 :
            distance[nxt2] = distance[cur] +1
            parent[nxt2] = cur
            q.append(nxt2)

    
    if 0<= nxt3 < 100001 :
        if distance[nxt3] == -1 :
            distance[nxt3] = distance[cur] +1
            parent[nxt3] = cur
            q.append(nxt3)

# 1 2 3 4
# parent[1] =-1
# parent[2] =1
# parent[3] =2
# parent[4] =3 이므로,


temp = K
path =[]
while True :
    if temp == -1 :
        break
    path.append(temp)
    temp =parent[temp]
path.reverse()
print(*path)
    
