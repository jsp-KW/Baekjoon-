def solution(sticker):
    answer = 0
    
    if len(sticker) ==1 :
        return sticker[0]

    def find_max(arr) :
        length = len(arr)
        dp =[0]*(length)

        if length ==0 :
            return 0
        
        if length ==1 :
            return arr[0]
        
        dp[0] = arr[0]
        dp[1] = max(arr[0],arr[1])
        
        
        for i in range(2, length):
            dp[i]= max(dp[i-1], dp[i-2] + arr[i]) #i번째를 안 고르는 경우 / i번째를 고르는 경우
            
        return dp[length-1]
    
    first_case = find_max(sticker[1:]) # 1부터 n-1원소까지
    second_case = find_max(sticker[:-1]) # 0~ n-2원소까지
        
    answer = max(first_case, second_case)

    return answer