import sys
from collections import deque


M,N = map(int,sys.stdin.readline().split())

board = [[] for _ in range (N)] 

for i in range (N) :
    temp = list(map(int,sys.stdin.readline().split()))
    board[i].extend(temp)


start_cordinates = []
visited = [[-1]*(M) for _ in range (N)]

for i in range (N) :
    for j in range (M) :
        if board[i][j] == 1 :
            start_cordinates.append((i,j)) # 시작점 넣기
            visited[i][j] = 0


dy = [-1,1,0,0]
dx= [0,0,-1,1]
def bfs () :
    while q  :
        cur_y,cur_x = q.popleft()
        for i in range (4) :
            my,mx = cur_y + dy[i] , cur_x +dx[i]
            if 0<=my<N  and 0<= mx <M :
                if board[my][mx] == 0 and visited[my][mx] == -1:
                    visited[my][mx] = visited[cur_y][cur_x] +1
                    board[my][mx] = 1
                    q.append((my,mx))


q = deque(start_cordinates)

bfs()

day = 0
for i in range (N) :
    for j in range (M) :
        if board[i][j] == 0 :
            print(-1)
            sys.exit()
        if visited[i][j] > day :
            day = visited[i][j]
    

print (day if day != 0 else 0)
        
