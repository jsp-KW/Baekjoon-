def solution(elements):
    answer = 0
    # 원형 수열
    
    

    candidates = set()
    
    n = len(elements) 
    
#     for length in range (2,n+1) :
#         for i in range (0, len(elements)) :
#             sum_val = 0
#             for j in range (0, length) :
#                 idx = (i+j)% len(elements)
#                 sum_val += elements[idx]
#             if sum_val not in candidates:
#                 candidates.add(sum_val)
#             else :
#                 continue
    
    arr = elements *2 
    prefix = [0] *(len(arr)+1)
    
    for i in range (0,len(arr)) :
        prefix[i+1] =prefix[i] + arr[i]
    #i-1까지의 합이 prefix[i]    
    candidates = set()
    n = len (elements)
    
    for length in range (1,n+1) :
        for start in range (n) :
            end = start +length 
            total = prefix[end] -prefix[start]
            candidates.add(total)
            
    return len(candidates)