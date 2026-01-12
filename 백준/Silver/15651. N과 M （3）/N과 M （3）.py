import sys
from itertools import product

N,M = map (int, sys.stdin.readline().split())

numbers= [i for i in range (1,N+1)]

# 1~N 까지 자연수중에서 M개를 고른 수열 

for p in product (range (1,N+1), repeat = M) :
    print (*p)