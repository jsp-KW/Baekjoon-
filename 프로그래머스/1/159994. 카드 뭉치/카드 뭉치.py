def solution(cards1, cards2, goal):

    check = True
    
    for target in goal :
        if target in cards1 :
            if cards1[0] == target :
                cards1.remove(target)
            else :
                check =False
                break
                
        else:
            if cards2[0] == target :
                cards2.remove(target)
            else:
                check= False
                break
                
    if not check :
        return "No"
    else:
        return "Yes"
                
                
                
