import sys
from collections import deque

M, N = map(int,sys.stdin.readline().split())
# 1 :  익은 토마토, 0 : 익지 않은 토마토 , -1: 토마토 X

tomato_box = [[0]*(M) for _ in range (N)]

for i in range (N) :
    temp = list (map(int, sys.stdin.readline().split()))
    tomato_box[i] = temp
dx = [0,0,-1,1]
dy = [-1,1,0,0]


start_nodes = deque()
day_count = [[-1]*(M) for _ in range (N)]

for i in range (N) :
    for j in range (M) :
        if tomato_box[i][j] ==1 :
            start_nodes.append ((i,j))
            day_count[i][j] = 0


while start_nodes :
    
    y,x = start_nodes.popleft()

    for i in range (4) :
        new_y, new_x = y+dy[i] , x+dx[i]
        if 0<= new_x <M  and 0<= new_y <N:
            if tomato_box[new_y][new_x] == 0  and day_count[new_y][new_x] ==-1 : # 익지 않았는 경우에만
                tomato_box[new_y][new_x] = 1 # 익음 처리
                day_count [new_y][new_x] = day_count[y][x] +1 # 익는거 하루 +1
                start_nodes.append ((new_y, new_x))

for i in range(N) :
    for j in range (M ):
        if tomato_box[i][j] == 0:
            print (-1)
            exit()
            
print (max(max(row) for row in day_count))