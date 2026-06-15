def solution(n):

    # nxn 
    # 동남서북
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    num =1 
    
    answer = [[0]*(n) for _ in range (n)]
    
    y=0
    x=0
    cur_idx =0
    for num in range (1,n*n+1):
        
        answer[y][x] = num
        my =y +dy[cur_idx]
        mx =x +dx[cur_idx]
        
        if (0> my)or (my >=n )or  (0 > mx) or (mx >=n) or answer[my][mx] !=0:
            cur_idx= (cur_idx +1) % 4
            my = y +dy[cur_idx]
            mx = x +dx[cur_idx]
        
        y,x = my,mx
            
    return answer