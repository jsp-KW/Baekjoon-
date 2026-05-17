def solution(data, ext, val_ext, sort_by):
    answer = []
    
    # code : 0 , date 1, maximum :2, remain:3
    compare_idx=  0
    sort_idx =0
    if ext == 'code' :
        compare_idx =0
    elif ext =='date':
        compare_idx =1
    elif ext == 'maximum':
        compare_idx =2
    else :
        compare_idx= 3
        
    if sort_by== 'code' :
        sort_idx =0
    elif sort_by =='date':
        sort_idx =1
    elif sort_by == 'maximum':
        sort_idx =2
    else :
        sort_idx= 3
        
    for d in data :
        if int(val_ext) > d[compare_idx] :
            answer.append(d)
        else: continue 
 
    answer.sort (key = lambda x : (x[sort_idx]))
        
        
    return answer