def solution(n, lost, reserve):
    # lost: 도난, reserve:여벌
    
    
    answer = 0
    students =[1]*(n+1)
    
    for l in lost:
        students[l]-= 1
        
    for r in reserve:
        students[r]+=1
    
    for i in range(1,n+1):
        if students[i]==0:
            if i-1>=1 and students[i-1]==2:
                students[i-1]-=1
                students[i]+=1
            elif i+1<=n and students[i+1]==2:
                students[i+1]-=1
                students[i]+=1
    
    for i in range(1,n+1):
        if students[i]>=1:
            answer+=1
            
    
            
            
        
        
        
    
    return answer