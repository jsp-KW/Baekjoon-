def solution(n, computers):
    # i번 컴퓨터 j번 컴퓨터 연결되어있음 -> computers[i][j] =1
    def dfs (node) :
        visited[node] = True
        for j in range (n) :
            if computers[node][j] ==1 and not visited[j] :
                visited[j] = True
                dfs(j)

        
    answer = 0
    visited = [False] * n
    for i in range (0,n):
        if not visited[i]  :
            answer+=1
            dfs(i)
        
    
     

    return answer