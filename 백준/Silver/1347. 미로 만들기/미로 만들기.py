import sys
# 홍준이는 미로 안의 한 칸에 남쪽을 보며 서있다
# 미로는 직사각형 격자모양
# 벽 or 이동 가능
# 모든 행,열에는 적어도 하나의 이동할 수 있는 칸이 있음

#f: 앞 l ,r 왼쪽 오른쪽 전환 -> 회전만 한거

dy = [1,0,-1,0]
dx = [0,-1,0,1] #남,서,북,동

len_loc = int(sys.stdin.readline())
locations = list(map(str, sys.stdin.readline().rstrip()))

y,x,d = 0,0,0

path = [(y,x)]

for loc in locations :
    if loc =='R' :
        d = (d+1)%4
    elif loc == 'L' :
        d= (d+3)%4
    elif loc == 'F' :
        y+= dy[d]
        x+= dx[d]
        path.append ((y,x))


min_y = min(p[0] for p in path)
min_x = min(p[1] for p in path)
max_y = max (p[0] for p in path)
max_x = max(p[1] for p in path )

height= max_y - min_y +1
width =  max_x - min_x +1

board = [['#'] *(width) for _ in range (height)]
for py, px in path :
    board[py-min_y][px-min_x] = '.'

for row in board :
    print (''.join(row))
    