def solution(k, dungeons):
    
    visited= [False]*(len(dungeons))
    
    # k:현재 피로도
    # 최소>= 소모 
       
    answer = 0
    def dfs(cur_hp,step):
        nonlocal answer
        answer= max(step,answer)
        
        
        for i in range(0,len(dungeons)):
            min_hp,lose= dungeons[i]
            if not visited[i] and cur_hp>= min_hp :
                visited[i]= True
                dfs(cur_hp-lose, step+1)
                visited[i]= False

    dfs(k,0)
    return answer