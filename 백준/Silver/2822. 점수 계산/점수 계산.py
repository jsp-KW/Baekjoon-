import sys

scores = []
for i in range (8) :
    score = int(sys.stdin.readline())
    scores.append((score,i+1))


scores.sort(key = lambda x: (-x[0]))
print(sum(num for num,_ in scores[:5]))
selected = [idx for _,idx in scores[:5]]
selected.sort()
print(*selected)