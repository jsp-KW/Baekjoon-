def solution(n, computers):
    # A->B 연결 ->B->C연결 일 경우 A->C도 연결이 가능함
    
    visited = [False]*(n)  
    
    def dfs (start) : 
        visited[start] = True
        
        for nxt in range (0, n) :
            if not visited[nxt] and computers[start][nxt] ==1:
                dfs(nxt)
                
    answer= 0
    for i in range (0,n) :
        if not visited[i] :
            dfs(i)
            answer+=1
        
    return answer