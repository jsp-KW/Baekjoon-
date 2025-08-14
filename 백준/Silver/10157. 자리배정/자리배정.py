import sys

col, row = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

if K > col * row  :
    print (0)
else :

    concert = [[0]*col for _ in range (row)]

# 첫번째 자리 좌표 맨 왼쪽 아래 (1,1)-> 인덱스 기준 : 
# 두번재 자리, y값 -1, 
# 위로간다 -1, y값이 어디까지->x고정, 0<= y <= row-1까지가고

# 다음으로 넘어갈때 x값이 0<= x<= col-1 

# 아래로가는것 -> x고정, y값 감소,  row-1<=y <=0
# 왼쪽으로 -> y고정, x값 감소 col-1 <= x <=0 +1
#  7 x 6 기준 -> x:5 y:0

# 위 오른쪽 아래, 왼쪽
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    x,y = 0,0 #0,0은 답으로 1,1 좌표


    direction = 0 # 0 위 1, 오른쪽 2 아래, 3왼쪽

    for num in range (1,row*col +1) :
        concert[y][x] =num

        nx,ny = x +dx[direction], y+dy[direction]

        if num == K :
            print (x+1, y+1)
            break
    
        if not (0<=nx <col and 0<= ny <row) or concert[ny][nx] != 0:
            direction = (direction+1)%4
            nx,ny =x+dx[direction], y+dy[direction]

        x,y = nx,ny

