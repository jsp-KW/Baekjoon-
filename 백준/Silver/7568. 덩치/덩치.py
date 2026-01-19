import sys
# 키 몸무게
# (x,y)
# x,y p,q  : x>p,y >q 라면, A의 덩치가 b보다 더 크다
# 즉, 둘다 커야한다는거임..

# N명의 집단에서, 각 사람의 덩치 등수 : 자신보다 더 큰 덩치를 가진 사람의 수
# K명이라면, K+1 가 된다

people = []

answers= []
N = int(sys.stdin.readline())
for _ in range (N) :
    weigth, height = map(int,sys.stdin.readline().split())
    people.append((weigth,height))



for person in people :

    answer = 0
    for i in range (0,len(people)) :
        
        if people[i] == person :
            continue
        
        else: 
            cur_weight, cur_height = person
            temp_weight, temp_height= people[i]

            if cur_weight <temp_weight and cur_height < temp_height :
                answer+=1 
            
    answers.append(answer+1)


print(*answers)
        
