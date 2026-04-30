from collections import deque
def solution(n):
    ans = 0
    
    while n!=0:
        if n% 2 == 0 :
            n = n //2 
        else: 
            ans +=1
            n = n-1


    return ans
        
    
    # K칸 점프  or   현재까지온 거리 x 2로 순간이동
    # 순간이동 : 건전지 사용x, k만큼 점프: 건전지 K 만큼 사용
    # N 만큼 떨어져 있는 장소로 가려한다, 사용량을 줄이기 위해 점프로는 최소로 간다
    # 사용량의 최소값을 구하자
    
    

    return ans