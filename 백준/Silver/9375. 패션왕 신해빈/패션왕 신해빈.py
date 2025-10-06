import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip())

answers=  []


for i in range (T):
    n = int (sys.stdin.readline())
    clothes = defaultdict(int)

    for  _ in range (n):
    
        name, type = sys.stdin.readline().split()
        clothes[type] +=1

    res =1

    for c in clothes.values() :
        res= res * (c+1)
    answers.append(res-1)
    

print (*answers, sep = '\n')
    