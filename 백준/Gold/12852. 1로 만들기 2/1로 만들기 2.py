import sys
from collections import deque

# %3 = 0 : 3으로나눈다
# 2로 나눈다
# -1

# 연산 3개를 적절히 사용해서 1로 만들려한다, 연산을 사용하는 횟수의 최솟값을 구해라


N = int (sys.stdin.readline())

nums = [i for i in range (1,N+1)]
dist = [0]*(N+1)
visited = [False]*(N+1)
parent = [0]*(N+1)

q= deque([N])
visited[N] = True

while q :
    
    cur = q.popleft()

    if cur == 1 :
        print(dist[cur])
        break

    next_nums= []

    if cur % 2== 0 : 
        nxt =cur //2
        next_nums.append(nxt) 
    
    if cur % 3==0 :
        nxt = cur//3
        next_nums.append(nxt)
    
    if cur -1 >= 1 :
        nxt = cur -1 
        next_nums.append(nxt)

    for nxt_num in next_nums :
        if nxt_num >=1 and not visited[nxt_num] :
            visited[nxt_num]= True
            dist[nxt_num] = dist[cur] +1
            parent[nxt_num] = cur
            q.append(nxt_num)

path = []
cur = 1 

while True:
    if cur == N :
        path.append(cur)
        break
    path.append(cur)
    cur = parent[cur]


path.reverse()
print(*path)

