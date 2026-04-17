import sys


N,K = map(int,sys.stdin.readline().split())

temp = list(map(int,sys.stdin.readline().split()))

# 연속적인 K일의 온도의 합이 최대가 되는 값을 출력
# k =2 , idx= 0 ~8포함
# k= 5 , idx =0~ 5포함

current_sum = sum(temp[:K])
max_sum = current_sum

for i in range (K, N) :
    current_sum = current_sum - temp[i-K] + temp[i]

    if max_sum  < current_sum :
        max_sum = current_sum


print(max_sum)

