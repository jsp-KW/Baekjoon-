from collections import deque

def solution(board):
    answer = 0
    # 직선도로  100원, 코너 500원
    
    # 최소 비용 계산
    
    # 방향이 이전 방향이랑 다르면 코너 +1 :500원
    # 같다면 그냥 도로 : 100원
    
    # 0은 비어있음, 1은 벽
    
    n = len(board)
    INF= int(1e9)
    
    # y,x,방향 3차원 distance 배열
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    distance = [[[INF] * (4) for _ in range(n)] for _ in range(n)]

    # y, x, 이전방향, 현재비용
    def bfs(start) :
        q= deque()
        
        for i in range (4) :
            first_y, first_x = 0 + dy[i],0 +dx[i]
            if 0<=first_y <n and 0<=first_x <n :
                if board[first_y][first_x] ==0:
                    distance[first_y][first_x][i] = 100
                    q.append((first_y, first_x ,i))
            
        while q :
            cur_y, cur_x , prev_direction = q.popleft()
            for i in range (4) :
                my,mx = dy[i] + cur_y, dx[i] + cur_x
                if 0<= my< n and 0 <= mx< n:
                    if board[my][mx] == 0 :
                        cur_cost  = distance[cur_y][cur_x][prev_direction]
                    
                        # 방향이 이전하고 다르면 코너
                        if prev_direction != i : 
                            next_cost = cur_cost + 600

                        else: # 방향이 이전하고 같으면 직진도로
                            next_cost = cur_cost + 100

                        # 이전 값 보다 싸다면? 갱신
                        if distance[my][mx][i] > next_cost :
                            distance[my][mx][i] = next_cost
                            q.append((my,mx,i))
                     
        return min(distance[n-1][n-1])
                        
    answer = bfs((0,0,-1))
    return answer