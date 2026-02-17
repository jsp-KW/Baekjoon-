import sys
from itertools import permutations

N , M = map(int,sys.stdin.readline().split())
# n개의 자연수 중에서, m개를 고른 수열
# 중복되는 수열 여러번 출력x, 각 수열은 공백을 구분으로출력, 사전순으로 증가

nums = list(map(int,sys.stdin.readline().split()))
#길이가 M인 수열
# 출력을 M번 해야한다는거같음, 오름차순 해서

res  = set()
for comb in permutations(nums,M):
    res.add(comb)


for r in sorted(res) :
    print(*r)
    