import sys
from collections import deque

# R X C
# . : 빈곳, * : 물, X : 돌
# 'D' : 굴, 고슴도치 위치 'S'

R, C = map(int,sys.stdin.readline().split())

board = []

# 물도 확장, 고슴도치도 이동인데,  고슴도치-> 물 x, 물->비버 x

for _ in range (R) :
    temp =list( map(str, sys.stdin.readline().rstrip()))
    board.append(temp)



# 굴까지, 비버가 이동하는데 걸리는 최소시간을 출력하자
# 만약 이동x라면, 'KAKTUS' 를 출력

dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited= [[False]*(C) for _ in range (R)]

water_q = deque ()
animal_q = deque()


for y in range (R) :
    for x in range (C) :
        if board[y][x] =='*': 
            water_q.append((y,x))
        elif board[y][x] == 'S' :
            animal_q.append((y,x))
            visited[y][x] = True

time = 0


def bfs () :
        for _ in range (len(animal_q)) : # 시간당 처리라, while 이 아닌 for문으로 처리
            cur_y, cur_x = animal_q.popleft()
            for i in range (4) :
                move_y,move_x = cur_y+ dy[i] , cur_x + dx[i]
                if 0<= move_y <R and  0<= move_x <C and not visited[move_y][move_x]: 
                    if board[move_y][move_x] == 'D' :
                        return True
                    if board[move_y][move_x] == '.' :
                            visited[move_y][move_x] = True 
                            animal_q.append((move_y,move_x))    
        return False

def water_bfs () :
    for _ in range (len(water_q) ) :
        cur_y, cur_x = water_q.popleft()
        
        for i in range (4) :
            water_y, water_x = cur_y + dy[i] , cur_x + dx[i]

            if  0<= water_y < R and 0<= water_x <C :
                    
                if board[water_y][water_x] in ('.', 'S') :
                    board[water_y][water_x] = '*'
                    water_q.append((water_y,water_x))
        
while animal_q  :
    water_bfs ()
    if bfs() :# true :굴 도착이므로,
        time +=1
        print (time)
        sys.exit(0)
    time +=1 

print ("KAKTUS")
    
