import sys
from collections import deque

# 적록색약 : 빨간색 초록색 차이 거의 느끼지 x
# NXN  그리드 ,R,GB
# R하고 G 

n = int(sys.stdin.readline())

board = []

for _ in range (n) :
    temp =list(map (str, sys.stdin.readline().rstrip("\n")))
    board.append(temp)

visited = [[False]*(n) for _ in range (n)]
copy_board =board.copy()


answer1 = 0 # 적록 색맹x
answer2 = 0 # 적록 색맹o 일때 영역수 저장

dy = [1,-1,0,0]
dx = [0,0,-1,1]

def bfs (start) :
    
    y,x = start
    visited[y][x] = True
    q = deque([start])

    while q :
        cur_y, cur_x = q.popleft()
        for i in range (4) :
            move_y,move_x = cur_y + dy[i] , cur_x + dx[i]
            if 0<= move_y  < n and  0 <= move_x <n :
                if not visited[move_y][move_x] and board[move_y][move_x] == board[cur_y][cur_x] :
                    visited[move_y][move_x] = True
                    q.append((move_y, move_x))
    return True

def changed_bfs (start) :
    y,x = start
    visited[y][x] = True
    q = deque([start])

    while q :
        cur_y, cur_x = q.popleft()
        for i in range (4) :
            move_y,move_x = cur_y + dy[i] , cur_x + dx[i]

            if 0<= move_y  < n and  0 <= move_x <n  :
                if not visited[move_y][move_x]:
                    if copy_board[cur_y][cur_x] == 'R' : 
                        if copy_board[move_y][move_x] == 'G' or copy_board[move_y][move_x] == 'R' :
                            visited[move_y][move_x] = True
                            q.append((move_y, move_x))
                      

                    elif copy_board[cur_y][cur_x] == 'G':
                        if copy_board[move_y][move_x] == 'R' or copy_board[move_y][move_x] == 'G':
                            visited[move_y][move_x] = True
                            q.append((move_y, move_x))
                        

                    else:
                        if copy_board[move_y][move_x] == copy_board[cur_y][cur_x] :
                            visited[move_y][move_x] = True
                            q.append((move_y, move_x))
    return True
                        


for i in range (n) :
    for j in range (n) :
        if not visited[i][j]  :
            if bfs((i,j)): answer1 +=1

visited = [[False]*(n) for _ in range (n)]

for i in range (n) :
    for j in range (n) :
        if not visited[i][j]  :
            if changed_bfs((i,j)):
                answer2 +=1

            
print (answer1,answer2)

