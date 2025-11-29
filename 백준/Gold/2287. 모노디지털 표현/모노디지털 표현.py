import sys

K = int (sys.stdin.readline())
n = int (sys.stdin.readline())

target_nums = [int(sys.stdin.readline()) for _ in range (n)]

dp = [set() for _ in range (9)]

dp[1].add(K)

for i in range (2,9) :
    dp[i].add ( int(str(K)*i))


for i in range (2,9):
    for j in range (1,i) :
        for a in dp[j] :
            for b in dp[i-j] :
                dp[i].add(a+b)
                dp[i].add(a-b)
                dp[i].add(a*b)
                if b!=0 :
                    dp[i].add(a//b)


for target  in target_nums :
    answer = "NO"
    for i in range(1,9):
        if target in dp [i] :
            answer = i
            break
    print (answer)
