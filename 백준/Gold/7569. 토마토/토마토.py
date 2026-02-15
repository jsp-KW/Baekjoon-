import sys
from collections import deque
# M,N,H
# N X M 짜리가 H개

M,N,H = map(int,sys.stdin.readline().split())

board = []

for i in range (H) :
    layer = []
    for _ in range (N):
        temp = list(map(int,sys.stdin.readline().split()))
        layer.append(temp)
    
    board.append(layer)


q = deque()

dh = [1,-1,0,0,0,0]
dn = [0,0,-1,1,0,0]
dm = [0,0,0,0,-1,1]

# 시작점 넣기
for h in range (H) :
    for n in range (N):
        for m in range (M) :
            if board[h][n][m] == 1 :
                q.append((h,n,m))


distance = [[[0]*(M) for _ in range (N)] for _ in range (H)]

while q :
    cur_h, cur_n, cur_m = q.popleft()

    for i in range (6) :
        mv_h, mv_n, mv_m = cur_h +dh[i], cur_n +dn[i], cur_m +dm[i]
        if 0<= mv_h <H and 0<= mv_n <N  and 0<= mv_m < M :
            if distance[mv_h][mv_n][mv_m] == 0 and board[mv_h][mv_n][mv_m] == 0:
                distance[mv_h][mv_n][mv_m] = distance[cur_h][cur_n][cur_m] +1
                board[mv_h][mv_n][mv_m] = 1
                q.append((mv_h, mv_n, mv_m))

ans = 0
for h in range (H) :
    for n in range (N) :
        for m in range (M) :
            if distance [h][n][m] == 0 and board[h][n][m] ==0 :
                print(-1)
                sys.exit()
            ans = max(ans, distance[h][n][m])


print (ans)