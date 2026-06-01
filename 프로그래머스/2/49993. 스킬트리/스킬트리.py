def solution(skill, skill_trees):
    answer = 0
    
    check_idx =0
    
    skill_all = set ()
    skill_set = set()

    for i in range (0,len(skill)) :
        skill_all.add(skill[0:i+1])
            

    for ch in skill :
        skill_set.add(ch)
    
 
    for s in skill_trees :
        temp =""
        for s_ch in s:
            if s_ch in skill_set :
                temp+= s_ch
            else:
                continue

        if temp in skill_all  or temp =="":
            answer+=1
        else :
            continue

        
    return answer