import sys
import math
N,M  = map(int, sys.stdin.readline().split())

min_six = float('inf')
min_one = float('inf')

for _ in range(M) :
    six_price, one_price = map(int, sys.stdin.readline().split())
    min_six = min(min_six , six_price)
    min_one = min(min_one, one_price)

   
case1 = (N // 6) * min_six + (N%6) * min_one

case2 = N * min_one

case3 = math.ceil(N/6) * min_six

answer = min(case1,case2,case3)
print(answer)