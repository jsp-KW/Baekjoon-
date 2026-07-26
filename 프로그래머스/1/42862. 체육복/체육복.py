def solution(n, lost, reserve):
    # lost: 도난, reserve:여벌
    
    
#     answer = 0
#     students =[1]*(n+1)
    
#     for l in lost:
#         students[l]-= 1
        
#     for r in reserve:
#         students[r]+=1
    
#     for i in range(1,n+1):
#         if students[i]==0:
#             if i-1>=1 and students[i-1]==2:
#                 students[i-1]-=1
#                 students[i]+=1
#             elif i+1<=n and students[i+1]==2:
#                 students[i+1]-=1
#                 students[i]+=1
    
#     for i in range(1,n+1):
#         if students[i]>=1:
#             answer+=1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # i번이라면, i-1번이나 i+1번에게만 체육복을 빌려줄 수 있음
    # 최대한 많이 빌려줘야함, 수업을 들을 수 있는 학생의 최대값을 return
    
    students = [0] *(n+1)
    answer = 0
    
    for l in lost :
        students[l] -=1
    
    for r in reserve :
        students[r] += 1
        
    for i in range (1, n+1) :
        
        if students[i] == 0 or students[i] == -1 :
            continue
        
        elif students[i] == 1 : # 여벌 있으면
            if i==1 :
                if students[i+1] == -1 :
                    students[i+1] = 0
            elif i == n :
                if students[i-1] == -1 :
                    students[i-1] = 0

            else:
                if students[i-1] == -1:
                    students[i-1] = 0
                    students[i] = 0
                elif students[i+1] == -1:
                    students[i+1] = 0
                    students[i] = 0
    
    for i in range (1, len(students)) :
        if (students[i] >=0) :
            answer+=1
            
    
    
    
    
    
    
    
    
            
            
        
        
        
    
    return answer