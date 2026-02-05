import sys
from collections import deque

n = int (sys.stdin.readline())
m = int(sys.stdin.readline())

friends = [[] for _ in range (n+1)]

for _ in range (m) :
    a,b = map(int,sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

cnt = 0
# 1번과친구인 애들 다 찾아라
visited = [-1]*(n+1)
def bfs (start) :
    
    visited[start] = 0
    q = deque([start])

    while q :
        
        cur = q.popleft()
     

        for nxt in friends[cur] :
            if  visited[nxt]== -1 :
                visited[nxt]= visited[cur] +1
                q.append(nxt)



bfs (1)
for v in visited :
    if v <=2 and 1<=v:
        cnt+=1
print(cnt)
