def solution(answers):
    answer = []
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5] 
    
    cnt1, cnt2,cnt3 = 0,0,0
    for i,correct in enumerate (answers) : # 최대 길이
        if answers[i] == student1[i % len(student1)]:
            cnt1 +=1
        if answers[i] == student2[i % len(student2)]:
            cnt2 +=1
        
        if answers[i] == student3[i % len(student3)]:
            cnt3 +=1
    temp = [cnt1,cnt2,cnt3]
    
    max_val = max(temp)
    
    for i in range (0, 3) :
        if temp[i] == max_val :
            answer.append(i+1)
        
    
    return answer