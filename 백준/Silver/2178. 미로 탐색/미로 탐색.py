from collections import deque
a,b = map(int, input().split())


go_x= [-1, 1, 0, 0]
go_y= [0, 0, -1, 1]
# bfs 를 이용하여.. queue 을 이용

maze =  []

for i in range(a):
    row = list(map(int, input()))  # 한 줄에 입력된 값들을 리스트로 변환하여 저장
    maze.append(row)


def bfs (x,y):
    queue = deque()
    queue.append((x,y))

    while queue: 
        x,y = queue.popleft()
        
        for i in range (4) :
            check_x =  x + go_x[i]
            check_y =  y + go_y[i]

            if check_x <0 or check_x >=a  or check_y >=b or check_y <0:
                continue

            if maze[check_x][check_y] ==0 :
                continue
 
            if maze[check_x][check_y] == 1 : 
                maze[check_x][check_y] = maze[x][y] +1
                queue.append((check_x,check_y))

            

        
    return maze[a-1][b-1]

print(bfs(0,0))

    
    




