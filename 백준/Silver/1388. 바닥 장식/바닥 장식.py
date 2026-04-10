import sys
from collections import deque


N,M = map(int,sys.stdin.readline().split())

board = [[] for _ in range(N)]
 
for i in range (N) :
    temp = list(map(str, sys.stdin.readline().rstrip()))
    board[i].extend(temp)


visited = [[False]*(M) for _ in range (N)]
dx= [-1,1]
dy = [-1,1]
def bfs(start) :
    
    y,x = start
    q = deque([start])
    visited[y][x] = True

    while q :
        cur_y,cur_x = q.popleft()

        if board[cur_y][cur_x] == '|' :
            for i in range (2):
                nxt =  cur_y + dy[i]
                if 0<=nxt <N and not visited[nxt][cur_x] :
                    if board[nxt][cur_x] == '-' :
                        continue
                    else :
                        visited[nxt][cur_x] = True
                        q.append((nxt,cur_x))



        elif board[cur_y][cur_x] == '-' :
            for i in range (2):
                nxt =  cur_x + dx[i]
                if 0<=nxt <M and not visited[cur_y][nxt] :
                    if board[cur_y][nxt] == '|' :
                        continue
                    else :
                        visited[cur_y][nxt] = True
                        q.append((cur_y,nxt))
                    
cnt = 0
for i in range(N) :
    for j in range(M) :
        if not visited[i][j] :
            bfs((i,j))
            cnt +=1

print(cnt)