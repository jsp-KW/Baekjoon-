def solution(data, col, row_begin, row_end):
    answer = 0
    
    # col 번째 행을 기준으로 내림차순 정렬
    # 같은 경우 첫번째 컬럼 값이 큰 기준으로 내림차순 정렬
    data.sort(key = lambda x : (x[col-1], -x[0]))
    
    # S_i 를 구하자, i번째 행의 튜플에 대해, 각 컬럼의 값을 i로 나눈 나머지들의 합으로
    # i = row_begin , row_end 
    # 1,2,3,4,5
    i = row_begin -1
    s_i_begin = 0
    
    target =  data [i]
    for t  in target :
        s_i_begin +=  t%row_begin
    
    
    prev = s_i_begin 
    for j in range (row_begin+1, row_end+1): 
        
        idx = j-1
        target = data[idx]
        s_i_end = 0

        for t in target :
            s_i_end += t% j
        
        prev = prev ^ s_i_end
    
    return prev