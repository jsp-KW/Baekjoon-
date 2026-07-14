def solution(dartResult):
    answer = 0
    
    scores = [0]*(3)
    num=""
    idx=0
    
    for ch in dartResult :
        
        if ch.isdigit() :
            num += ch
        
        elif ch == 'S' :
            scores[idx] = int(num)
            num= ""
            idx+=1
        elif ch == 'D' :
            scores[idx] = int(num) **(2)
            num= ""
            idx+=1
        elif ch == 'T' :
            scores[idx] = int(num)**(3)
            num= ""
            idx+=1
            
        elif num == "":
            if ch == '*' :
                if idx-2 >= 0:
                    scores[idx-2] = scores[idx-2] *2
                    scores[idx-1] = scores[idx-1]* 2
                else:
                    scores[idx-1] = scores[idx-1]*2
            else:
                scores[idx-1] = -scores[idx-1]
         
    return sum(scores)