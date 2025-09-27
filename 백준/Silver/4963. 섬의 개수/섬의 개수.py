import sys
from collections import deque
answers= []

def bfs (start) :

    y,x = start[0],start[1]
    visited[y][x] = True
    
    q = deque([(y,x)])

    while q  :

       
        cur_y, cur_x = q.popleft()

        for i in range (8) :
            move_y, move_x = cur_y + dy[i] , cur_x +dx[i]
            if 0 <= move_y<h and 0<= move_x < w :
                if not visited[move_y][move_x] and maps[move_y][move_x] == 1 :
                    
                    visited[move_y][move_x]= True
                    q.append((move_y,move_x))
      


while True :

    w,h = map(int,sys.stdin.readline().split())
    count = 0
    if w <=0  or h <= 0  :
        break

    maps =[[] for _ in range (h)]
    for i in range (h) :
        lines = list(map(int,sys.stdin.readline().split()))
        maps[i]+= lines
    
    if w ==1  and h ==1 :
        if maps[0][0] ==  0 :
            answers.append(0)
        else :
            answers.append(1)

    else:
            
        visited =[[False]*(w) for _ in range (h)]
        dy = [-1,1,0,0,-1,-1,1,1]
        dx = [0,0,-1,1,-1,1,-1,1]
        inner_result = 0
        for i in range (h) :
            for j in range (w) :
                if not visited[i][j] and maps[i][j] ==1 :
                    bfs((i,j))
                    inner_result += 1

        answers.append(inner_result)


    
for ans in answers :
    print (ans)