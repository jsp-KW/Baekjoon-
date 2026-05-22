def solution(A, B):
    answer = -1
    # 숫자가 크면 1점
    # 같으면 0점
    # A 팀의 순서를 공개됨
    # B팀이 얻는 승점을 구하자, A 팀의 최종 승점을 가장 높이는 방법
    
    
    # B-A를 하면서, 값이 양수이면서 그 차이가 최소로 남는 것?
    
    A.sort()
    B.sort()
    
    # 1 3 5 7 : A
    # 2 2 6 8 : B
    answer = 0
    
    i =0
    temp_idx=0
    while i < len(A) :
        target = A[i]
        while temp_idx < len(B) :
            if B[temp_idx] > target :
                answer+=1 
                temp_idx =temp_idx+1
                break
            temp_idx +=1
        i= i+1
    
    return answer
            