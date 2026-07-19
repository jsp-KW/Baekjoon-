def solution(answers):
    answer = []
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5] # 1000 세트
    
    
    # 10000 문제
    
    
    # answers * 2000 세트
    
    s1 = 2000 * (student1)
    s2 = 1250 * (student2)
    s3 = 1000 * (student3)
    
    s1_res = [x-y for x,y in zip(answers,s1)]
    s2_res = [x-y for x,y in zip(answers,s2)]
    s3_res = [x-y for x,y in zip(answers,s3)]
    
    res1 = s1_res.count(0)
    res2 = s2_res.count(0)
    res3 = s3_res.count(0)
    
    max_ans = max(res1,res2,res3)
    
    temp = [res1,res2,res3]

    for i in range (3) :
        if max_ans == temp[i] :
            answer.append(i+1)
    
    return answer