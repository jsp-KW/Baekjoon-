import sys
from collections import deque 

# F층 :총 층 수
# 스타트링크 : G층
# 강호 : S층
# 버튼 2개 : U : 위로 U층, D : 아래로 D층
# 강호 G층 도착하려면, 버튼을 적어도 몇 번 눌러야하는지 구해라
# G층에 갈 수 없다면 출력하기


F,S,G,U,D = map(int,sys.stdin.readline().split())

# 1 -> 10  u u u u d u

# 1<= 층수 <= F
# U , D
find = False
floor = [i for i in range (1,F+1)]
visited = [-1] *(F+1)
q = deque([S])
visited[S] = 0

move = [+U, -D]
while q :
    cur_floor = q.popleft()
    if cur_floor == G :
        find = True
        break

    for i in range (2) :
        move_floor = cur_floor + move[i]
        if 1<= move_floor <F+1 :
            if visited[move_floor] == -1 :
                visited[move_floor] = visited[cur_floor] +1 
                q.append(move_floor)

if find :
    print(visited[G])
else :
    print("use the stairs")