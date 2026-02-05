def solution(people, limit):
    answer = 0 
    
    left,right = 0,len(people) -1 
    
    #구멍 보트를 최대한 적개 사용하자
    people.sort ()
    # 50 50 70 80
    # 80 쓰고, 70쓰고, 50+50

    while left <= right :
        if people[left] + people[right] <= limit :
            left += 1
            right-=1
        else :
            right -=1 
        answer+=1
    
    return answer