import sys
from collections import deque

R,C,K = map(int, sys.stdin.readline().split())


maps = [list(sys.stdin.readline().strip()) for _ in range (R)]

visited =[[False] *(C) for _ in range (R)]

# 한수 시작점은 r-1, 0
# 집은 0, c-1 에 있음
# 딱 K가 되야함 거리가

dx = [0,0,-1,1]
dy = [1,-1,0,0]

cnt = 0
def dfs (y,x,dist) :
    global cnt # 집에 정확히 방문할 경우를 저장할 변수 

    if (y,x) == (0,C-1) and dist == K :        
        cnt+=1 # 집 도착 +1
        return

    for i in range (4) :
        move_y , move_x = y + dy[i], x+ dx[i]

        if 0<= move_y <R and 0 <= move_x <C :
            if not visited[move_y][move_x]  and maps[move_y][move_x] != 'T' :
               
                visited[move_y][move_x] = True
                dfs (move_y, move_x, dist+1)
                visited[move_y][move_x] = False # back tracking



visited [R-1][0] = True
dfs (R-1,0,1)

print(cnt)
