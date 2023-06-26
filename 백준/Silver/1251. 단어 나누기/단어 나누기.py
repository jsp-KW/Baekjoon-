import sys

s = sys.stdin.readline().rstrip('\n')

answer =[]
for i in range(1, len(s)-1):
    
    res =[]
    for j in range(i+1, len(s)):

        res = ((s[0:i:])[::-1]) + ((s[i:j:])[::-1]) + ((s[j::])[::-1])

        answer.append(res)

answer.sort()

print(answer[0])