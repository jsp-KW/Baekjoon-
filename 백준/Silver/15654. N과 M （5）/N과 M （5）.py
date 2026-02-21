import sys
from itertools import permutations
# N, M  
# 길이가 M인 조건을 만족하는 수열
#

N,M = map(int,sys.stdin.readline().split())

nums = list(set(map(int,sys.stdin.readline().split())))

for per in permutations (sorted(nums),M) :
    print (*per)