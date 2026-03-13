import sys
from collections import deque


T = int(sys.stdin.readline())

answers = []

for _ in range (T) :
    N = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    graph = [[] for _ in range (N+1)]

    for idx, num in enumerate(nums) :
        graph[idx+1].append(num)

    cnt = 0
    visited = [False]*(N+1)
    
    def bfs(start) :
        

        visited[start] = True 

        q = deque([start])

        while q :
            cur = q.popleft()
            for nxt in graph[cur] :
                if nxt == start and visited[nxt]:
                    return True
                
                if not visited[nxt] :
                    visited[nxt] =True
                    q.append(nxt)
        return False
    
    for i in range (1,N+1) :
        if not visited[i] :

            if bfs(i):
                cnt +=1
    
    answers.append(cnt)

for ans in answers:

    print(ans)