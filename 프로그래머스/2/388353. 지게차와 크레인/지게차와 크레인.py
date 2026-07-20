from collections import deque
def solution(storage, requests):
 
    n = len(storage)
    m = len(storage[0])
    answer = n*m
    
    
    graph = [[0] *(m+2) for _ in range (n+2)]
    
    # 상하좌우, 접근 가능 컨테이너 모두 꺼냄, 
    # 접근 가능컨테이너 -> 4면 중 적어도 1면이 창고 외부와 연결된 컨테이너
    
    # 외부 '0'으로 저장해놓자
    
    # 같은 문자열 두개인경우는 외부 접근 가능 컨테이너 x어도 걍 삭제
    # 그냥 문자열 -> 외부 접근 가능 컨테이너여야함
    
    
 
    
    # row 가 0이거나, n-1 일때 
    # col이 0이거나, n-1일때 외부 접근가능컨테이너 취급 해당좌표는
    
    for j in range (0, m+2) :
        graph[0][j] = '0'
        graph[n+1][j] = '0'
    
    for i in range(0, n+2) :
        graph[i][0] = '0'
        graph[i][m+1] = '0'
    
  
    for i in range(1, n+1) :
        for j in range(1, m+1):
            graph[i][j] = storage[i-1][j-1]
    
    def get_all (target) :
        cnt = 0
        for i in range (1,n+1) :
            for j in range (1,m+1) :
                if graph[i][j] == target :
                    graph[i][j] = '0'
                    cnt+=1
        return cnt
                    

    # row 0~ m+1 , col 0~n+1
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    def bfs(start, target_str) :
        visited=  [[False]*(m+2) for _ in range(n+2)]
    
        y,x = start
        visited[y][x] = True
        q= deque([start])
        
        remove_list = []
        while q :
            cur_y, cur_x = q.popleft()
            for i in range(4) :
                my,mx = cur_y + dy[i], cur_x +dx[i]
                
                if (0 >my or my > n+1 or mx <0 or mx >m+1) : #범위 벗어나면 x
                    continue
                
                # 외부 컨테이너들
                if visited[my][mx] :
                    continue
                
                if graph[my][mx] == '0' : #비어있는 곳이면 넣기
                    visited[my][mx] = True
                    q.append((my,mx))
                    
                elif graph[my][mx] == target_str: # 타겟 문자열하고 같으면 삭제
                    visited[my][mx] = True
                    remove_list.append((my,mx))
        
        for y,x in remove_list :
            graph[y][x] = '0'
        return len(remove_list) #삭제 대상이 들어있는 길이 반환
    
    for r in requests :
        if len(r) == 1:
            answer -= bfs((0,0),r[0])
        else: # 2자인경우
            answer -= get_all(r[0])
            
            
        
    return answer