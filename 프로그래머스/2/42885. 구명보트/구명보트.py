def solution(people, limit):
#     answer = 0
#     left, right = 0, len(people)-1
    
#     people.sort()
    
#     # 모든 사람들을 구출하기 위해 필요한 구명보트 개수의 최소값
    
#     # 50 50 70 80
    
#     while left <= right :
#         cur_weight= 0
#         cur_weight= people[left] + people[right]
        
#         if cur_weight <= limit :
#             left = left +1
#             right= right -1
        
#         else :
#             right = right -1
        
#         answer +=1
        
        
#     return answer
    
    
    
    
    
    answer =0
    
    people.sort()
    left = 0
    right = len(people)-1
    
    while left <=right :
        temp = people[left] + people[right]
        
        if temp <=limit :
            left+=1
            right -=1
        else:
            right -=1
        answer+=1
        
    
    
    return answer
    
    
    
    
    
    
    
    
    
    
