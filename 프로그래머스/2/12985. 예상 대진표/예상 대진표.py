def solution(n,a,b):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    # 1 2 3 4 5 6 7 8
    
    # 12 ->1 / 34 ->2 / 56 ->3 /78 ->4
    # 24 ->1  67->2
    # 4 - 7
    
    while a != b:
        a =  (a+1)//2
        b = (b+1)//2
        answer+=1
    return answer