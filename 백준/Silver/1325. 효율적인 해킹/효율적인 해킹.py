import sys
from collections import defaultdict,deque


# 신뢰하는관계 
# 신뢰하지 않은 관계
# A가 B를 신뢰한다, B를 해킹하면 A도 해킹할 수 있음

# 신뢰관계가 주어졌을때 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력


# N,M 입력
# M개의 줄에 신뢰하는관계 AB -> A가 B를 신뢰한다

N,M = map(int, sys.stdin.readline().split())

computers =[[] for i in range(N+1)]
visited = [False] *(N+1)

for _ in range (M) :
    pc1,pc2 = map(int, sys.stdin.readline().split())
    computers[pc2].append(pc1)

def bfs(n):
    
    q = deque()
    q.append(n)
    visited[n] =True
    cnt =1
    while q :
        cur = q.popleft()
        for c in computers[cur]:
            if not visited[c]:
                visited[c] = True
                q.append(c)
                cnt+=1
    
    return cnt

max_cnt =0
results = [0]*(N+1)

for i in range(1,N+1) :
    results[i] = bfs(i)
    visited = [False] *(N+1)

max_cnt = max(results)

answer =[]

for i in range(1,N+1) :
    if results[i] == max_cnt :
        answer.append(i)
print(*answer)


