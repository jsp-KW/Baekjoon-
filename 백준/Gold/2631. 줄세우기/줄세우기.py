import sys

N = int(sys.stdin.readline())

childs = []
for _ in range (N) :
    temp =int( sys.stdin.readline())
    childs.append(temp)

dp =[1] * N

for i in range (N) :
    for j in range(i) :
        if childs[j] < childs[i] :
            dp [i] = max(dp[i], dp[j]+1)
            
print (len(childs) -max(dp))
