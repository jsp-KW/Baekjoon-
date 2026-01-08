
import sys
from collections import deque

K = int(sys.stdin.readline().rstrip("\n"))
answers = []
for _ in range (K) :
    V,E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    color = [0]*(V+1)

    for _ in range (E) :    
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    ok = True
    for i in range (1,V+1) :
        if color[i] == 0 :
            color[i] = 1

            q = deque([i])

            while q :
                cur = q.popleft()

                for nxt in graph[cur] :
                    if color[nxt] == 0 : 
                        color[nxt] = -color[cur]
                        q.append(nxt)
                    elif color[nxt] == color [cur]  :
                        ok = False 
        

    if ok :
        answers.append("YES")
    else :
        answers.append("NO")
                   

for ans in answers:
    print(ans)