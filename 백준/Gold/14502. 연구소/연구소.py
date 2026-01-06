import sys
from collections import deque
from itertools import combinations

N,M = map(int, sys.stdin.readline().split())

# N X M 사이즈
# 0 : 빈칸, 1:벽 , 2: 바이러스
board = []
visited = [[False]*(M) for _ in range (N)]

for _ in range (N) :
    board.append (list(map(int,sys.stdin.readline().split())))


dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs (start, copy_board) :
    
    y,x = start
    visited[y][x] = True
    q = deque([start])

    while q :
        cur_y, cur_x = q.popleft()
        
        for i in range (4) :
            move_y,move_x = cur_y + dy[i] , cur_x + dx[i]

            if 0<=move_y <N  and 0<= move_x <M :
                
                if not visited[move_y][move_x] and copy_board[move_y][move_x] == 0 :
                    
                    copy_board[move_y][move_x] = 2
                    visited[move_y][move_x] = True
                    q.append((move_y,move_x))


# 3개를 세운다 벽
# 조합을 사용해서,
candidates = []

for i in range (N) :
    for j in range (M) :
        if board[i][j] == 0 :
            candidates.append((i,j))


answer = 0
for comb in combinations(candidates,3) :

    copy_board = [row[:] for row in board]
    
    for c in comb :
        y,x = c 
        copy_board[y][x] = 1

    for i in range (N) :
        for j in range (M) :
            if not visited[i][j] and copy_board[i][j] ==2 :
                bfs ((i,j), copy_board)

    cnt = 0

    for i in range (N) :
        for j in range (M) :
            if copy_board[i][j] == 0 :
                cnt +=1 

                
    answer = max(answer,cnt)

    visited = [[False]*(M) for _ in range (N)]


print (answer)
        