import sys
from collections import deque

#0 은 갈수 없는 땅, 1은 갈수있는 땅, 2는 목표지점
# 기존의 bfs 랑 살짝 다르게, 목표지점에서 거리배열 기준으로 방문 처리 및 거리를 측정해야함;;
# 다시 풀어보기
n,m =map(int, sys.stdin.readline().split())

maps = [[] for _ in range (m)]

for i in range (n) :
    temp = list(map(int,sys.stdin.readline().split()))
    maps[i].extend(temp)


dy = [-1,1,0,0]
dx = [0,0,-1,1]

answer = -1

for i in range (n):
    for j in range (m) :
        if maps[i][j] == 2:
            start_y, start_x = i,j

dist = [[-1]* m  for _ in range (n)]
q = deque()
q.append((start_y,start_x))
dist[start_y][start_x] = 0

while q :
    y,x = q.popleft()
    for i in range (4) :
        move_y ,move_x = y+dy[i], x+dx[i]

        if 0<=move_y <n and 0<= move_x<m:

            if maps[move_y][move_x] == 1 and dist[move_y][move_x]== -1: 
                dist[move_y][move_x] = dist[y][x] +1
                q.append((move_y,move_x))
 

for i in range (n) :
    for j in range (m) :
        if maps[i][j] == 0 :
            print (0, end= " ")
        else:
            print (dist[i][j], end = " ")
    print ()