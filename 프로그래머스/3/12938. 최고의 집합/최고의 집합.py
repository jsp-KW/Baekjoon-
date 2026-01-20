def solution(n, s):
    answer = []
    if n>s : 
        return [-1]
    else :
        # 집합 안 원소 개수가 n 개, 합이 s 인 집합들 중에, 각 원소의 곱이 최대가 되는 집합
        #  곱이 최대려면, 안의 원소들의 차이가 많이 나지않아야함.
        can =  s // n
        temp = s % n
        answer = [can] *(n)
        for i in range (n-1, n-1-temp,-1) :
            answer[i] +=1
    return answer