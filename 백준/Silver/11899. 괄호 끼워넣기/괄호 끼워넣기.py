import sys
temp = sys.stdin.readline().rstrip()

stack = []
for ch in temp :
    if ch == ')': 
        if stack and  stack[-1] == '(':
                stack.pop()
        else:
            stack.append(ch)
    else:
        stack.append(ch)


print(len(stack))
