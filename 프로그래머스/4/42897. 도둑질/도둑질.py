def solution(money):
    answer = 0
    
    def make_dp (money) :
        n = len(money)
        dp =  [0]*(n)

        dp[0] = money[0]
        dp[1] = max(money[0], money[1]) # 0번집 털기 1번집 털기 ->큰 집부터 털기, 

        # 인접해있고, 동그랗게 연결되어있어서 맨 처음과 맨 마지막 같이 선택 x
        # I번째를 턴다 -> i-2 랑 연결
        # 안 털으면 스킵? i-1
        for i in range (2, n) :
            dp[i]= max (dp[i-1], dp[i-2] + money[i])
        return dp[n-1]
    case1 = make_dp (money[1:])
    case2 = make_dp (money[:-1])
    
    answer = max(case1,case2)
    return answer