

import sys

stack = []
n = int(sys.stdin.readline().rstrip())

for i in range(n) :
    num = int (sys.stdin.readline().rstrip())
    stack.append(num)

max = 0  
answer = set() # set 을 이용하여 중복에 대한 처리 이슈 제거
for i in range (n-1,-1, -1) : # 뒤에서 부터
    if stack[i] > max :
        answer.add(stack[i])
        max = stack[i]

print (len(answer))