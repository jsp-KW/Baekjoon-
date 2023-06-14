def solution(keymap, targets):
    answer = []
    
    dict = {}
    for i in range(0, len(keymap)):
        for j in range(0, len(keymap[i])):
            c = keymap[i][j]
            
            if c in dict :
                dict[c] =  min (dict[c], j+1)
            else :
                dict[c] = j+1
                
                
    for tar in targets:
        res =0
        for t in tar :
            if t in dict:
                res += dict[t]
        
            else :
                res =-1
                break
                
        answer.append(res)
    
    return answer
