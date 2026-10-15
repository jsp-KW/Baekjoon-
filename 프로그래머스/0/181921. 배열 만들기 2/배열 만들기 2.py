from itertools import product
def solution(l, r):
    answer = set()
    
    str_r = str(r)
    
    num = ["0","5"]
    str_len = len(str_r)
    for i in range (1, str_len+1) :
        for per in product (num, repeat=i):
            res = int("".join(per))
            if res >=l and res <= r :
                answer.add(res)
                
    
    
    li_ans = list(answer)
    li_ans.sort()
    
    if not li_ans :
        return [-1]
    else:
        return li_ans