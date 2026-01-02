import sys
from collections import deque


# NXN
# 상하좌우 끝 벽이 있음
# 맨좌측, 뱀의 길이 1, 처음에 오른쪽
# 벽 OR 자기자신의 몸과 부딪히면 게임 끝
# 이동한 칸 사과 O , 사과 없어지고 꼬리는 움직이지 X
# 이동한 칸 사과 X, 몸길이 줄여서 꼬리가 위치한 칸을 비워준다.

#  게임이 몇초에 끝나는지 계산하라

directions = [(0,1), (1,0), (0,-1), (-1,0)] # 우 하 좌 상
N = int(sys.stdin.readline()) # 보드 크기
K = int (sys.stdin.readline()) # 사과 개수

board = [[0]*(N) for _ in range (N)]

for _ in range (K) :
    row, col = map (int,sys.stdin.readline().split())
    board[row-1][col-1] = 1


snake_length = 1


L = int(sys.stdin.readline()) # 뱀의 방향 변환 횟수

turns = []

for _ in range (L) :
    X,C = map (str,sys.stdin.readline().split())
    after_time = int (X)
    turns.append ((after_time,C))

idx = 0
time = 0
snake = deque ([(0,0)]) # 머리, 꼬리
snake_set  = {(0,0)} # 충돌 체크

dir_idx = 0 # 처음 오른쪽 
while True :
    time = time +1

    head_r, head_c =  snake[0]
    dr,dc = directions[dir_idx]
    nr,nc = head_r +dr , head_c +dc

    if not (0<=nr <N and  0 <= nc <N) :
        print (time)
        break

    if (nr, nc) in snake_set :
        print(time)
        break


    # 충돌 체크후, 실제로 이동하기 위해서
    # 좌표 삽입
    snake.appendleft ((nr,nc))
    snake_set.add ((nr,nc))



    if board[nr][nc] == 1  :
        board [nr][nc] = 0
    else :
        tail = snake.pop()
        snake_set.remove(tail)



    # 다음 방향 계산    
    if idx <L and time == turns[idx][0]  :
        if turns[idx][1] == 'D' :
            dir_idx = (dir_idx +1) % 4
        else :
            dir_idx =  (dir_idx +3) % 4
        idx = idx +1


    

    

