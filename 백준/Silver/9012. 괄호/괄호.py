import sys

n = int(sys.stdin.readline())

answers = []
for _ in range (n) :
    sentence = sys.stdin.readline().rstrip("\n")
    stack = []
    ok = True
    for ch in sentence  :
        if ch == '(' :
            stack.append(ch)
        elif ch == ')' :
            if len(stack) !=0 :
                stack.pop()
               
            else :
                ok = False
                break
            
    if ok and not stack: 
        answers.append("YES")
    else :
        answers.append("NO")

for ans in answers :
    print (ans)
