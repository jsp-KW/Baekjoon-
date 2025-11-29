import sys


players, jimin, hansu = map(int, sys.stdin.readline().split())

# 지민과 임한수는 서로 대결하기 전 항상 이긴다고 가정함.

round = 0
while jimin!= hansu :
    
    jimin = (jimin+1) //2
    hansu = (hansu+1) //2
    round +=1

print (round)