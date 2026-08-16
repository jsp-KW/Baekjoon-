def solution(a):
    answer = 0
    # 인접한 풍선중 번호 작은거 터트릴 수 있는건 1번
    # 1번 다쓰면 번호 큰 애만 터트리기 가능
    
    
    n = len(a)
    if n<=2 :
        return n 
    
    left_min =  [0] * n
    right_min = [0] * n
    
    left_min[0] = a[0]
    for i in range (1, n) :
        left_min[i] = min (left_min[i-1], a[i])
    
    right_min[-1] = a[-1]
    for i in range (n-2, -1,-1) :
        right_min[i] = min(right_min[i+1], a[i])
        
    answer = 2
    # a[0], a[-1] 생존 무조건
    
    for i in range (1, n-1) : # 양쪽의 값이 모두 나보다 작은 경우만 아니면 가능하므로, 
        if not (a[i] > left_min[i-1] and a[i] > right_min[i+1]) :
            answer+=1
    return answer