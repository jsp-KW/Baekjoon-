from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    
    # 제제 대상 배열에 넣고 길이 return
    
    result = [] # ban_id idx와 user 를 넣어서 튜플형태로 구분
    ban_idx =0
    for user in user_id :
        for i in range(0,len( banned_id )):
            target= banned_id[i]
            
            check= True
            if len(user) != len (target):
                continue 
            else :
                
                for j in range (0, len(target)) :
                    if target[j] != user[j] and target[j] !='*' :
                        check = False
                        break
                
            if check : 
                result.append( (i,user))
    # 리스트를 만들었고, 가짓수를 체크해야함
    answer_set= set()
    
    def dfs(idx, selected) :
        if idx == len(banned_id) :
            answer_set.add (tuple(sorted (selected)))
            return 
        
        for user_idx, user in result :
            
            if user in selected :
                continue 
            
            if user_idx != idx :
                continue 
                
            selected.add(user)
            dfs(idx+1, selected)
            selected.remove(user)
            
    dfs(0,set())
        
        
    return len(answer_set)