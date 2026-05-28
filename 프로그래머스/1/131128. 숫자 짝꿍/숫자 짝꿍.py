from collections import Counter
def solution(X, Y):
    answer = ''
    
    nums = []
    counter_y = Counter(Y)

    for x_ch in X :
        if counter_y [x_ch] >0 :
            nums.append(x_ch)
            counter_y[x_ch] -=1
            
    
    nums.sort(reverse=True)
    if not nums :
        return "-1"
    else :
        if nums[0] == '0' :
            answer = "0"
        else :
            for n in nums :
                answer+=n
    return answer