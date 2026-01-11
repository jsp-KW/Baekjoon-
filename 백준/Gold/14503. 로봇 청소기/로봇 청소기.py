import sys
from collections import deque
N,M =map(int,sys.stdin.readline().split())

board = [ [] for _ in range (N)] 

dx = [0,1,0,-1] # 북동남서
dy = [-1,0,1,0]


#북:0,동:1, 남:2, 서:3

start_y, start_x, status = map(int,sys.stdin.readline().split()) #로봇 좌표, 상태


for i in range (N) :
    temp = list(map(int,sys.stdin.readline().split()))
    board[i].extend(temp)

answer=  0
cur_y, cur_x, cur_status = start_y, start_x,status

while True :

    # 현재칸 청소하기
    if board[cur_y][cur_x] == 0 :
        board[cur_y][cur_x] = 2 # 청소처리
        answer+=1 
    
    moved = False

    for i in range (4) :
        cur_status = (cur_status-1) %4
        move_y, move_x = cur_y+ dy[cur_status], cur_x+dx[cur_status]

        if board[move_y][move_x] == 0 : # 청소해야하는 칸 발견시,
            cur_y,cur_x = move_y, move_x 
            moved = True
            break
    
    if not moved : # 청소할게 없다면, 바라보는 방향 유지한채 한칸 후진
        back_dir = (cur_status+2)%4 

        back_y,back_x = cur_y + dy[back_dir], cur_x+dx[back_dir]
        if board[back_y][back_x] == 1 :
            break
        else :
            cur_y, cur_x = back_y, back_x 

print (answer)