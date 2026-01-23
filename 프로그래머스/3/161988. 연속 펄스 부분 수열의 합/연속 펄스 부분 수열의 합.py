def solution(sequence):
    answer = 0
    # 부분수열을 다 구한다 -> 시간복잡도때문에 x
    # 음수인 곳은 -1 , 양수 양옆에 있는 부분수열
    # 가운데 양수이고, 양옆에 음수가 잇는 경우도 최대가 될 수 있는데
    
    # 1. 부분수열을 어떻게 구해야할까?  부분합으로? 슬라이딩 윈도우로..?
    # 2. 구한 부분수열들에 펄스수열 형태가 2가지인데, 이를 어떻게 적용하나- > 이건 두가지 펄스니까, 각 해서 최대 고르면 될듯
    
    def kadane (start_sign) :
        best = -float('inf')
        cur = -float('inf')
        sign = start_sign
        
        for a in sequence :
            x = a* sign
            sign =  sign * -1
            
            cur = max (x,x+cur)
            best = max (best, cur)
            
        return best
    
    return max (kadane(1), kadane(-1))
    
    
            
    
    return answer