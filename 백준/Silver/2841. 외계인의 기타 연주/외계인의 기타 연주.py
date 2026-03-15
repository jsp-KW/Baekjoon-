import sys

N, P = map(int,sys.stdin.readline().split())

stacks = [[] for _ in range(7)]

cnt  = 0
for _ in range (N) :
    line, pret = map(int,sys.stdin.readline().split())

 
    while stacks[line] and stacks[line][-1] > pret: 
        stacks[line].pop()
        cnt+=1 
        # 현재 프렛보다 큰 애들이 몇개있는지 체크 
    
    if stacks[line] and stacks[line][-1] == pret :
        continue

    stacks[line].append(pret)
    cnt+=1


print(cnt)

