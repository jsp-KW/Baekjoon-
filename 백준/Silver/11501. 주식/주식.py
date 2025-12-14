import sys


# 산다/ 판다 / 안한다
# 최대이익


# 쌀때 사서 비쌀때 판다,


T  = int (sys.stdin.readline())
answers = []

for _ in range (T) :
    N = int (sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))

    max_price = 0
    max_idx = 0
    result = []
    for i in range (len(prices)-1,-1,-1) :
        
        if prices[i] > max_price :
            max_price = prices[i]
        else :
            result.append (max_price - prices[i])

    if len (result ) == 0 : answers.append(0)
    else : answers.append (sum(result))


for ans in answers:
    print (ans)
