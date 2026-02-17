import sys
from itertools import combinations

N,M = map(int,sys.stdin.readline().split())

# 1부터 n까지 중복없이 M 개를 ㄱ른 수열
# 오름차순이어야함
numbers  = [i for i in range (1,N+1)]

result = []
for comb in combinations(numbers, M) :
    result.append(comb)

result.sort()

for res in result :
    print(*res)