import sys
from itertools import combinations

N,S = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range (1,N+1) :

    for comb in combinations (numbers,i):
        sum =0
        for c in comb :     
            sum+=c
           
        if sum == S :
            cnt +=1
            

print (cnt)