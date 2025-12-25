import sys

answer = []
while True :

    stack = [] 

    temp = sys.stdin.readline().rstrip()

    if temp == '.' : 
        break

    check = True
    
    for t in temp : # 열린 괄호만 스택에서 관리
        if t in '([' :
            stack.append(t)
        elif t == ']' : 
            if not stack or stack[-1] != '[' : # 균형이 깨짐
                check = False 
                break
            stack.pop()  # 균형이 맞으면, 열린괄호 [  stack에서 제거
        elif t == ')' :
            if not stack or stack[-1] != '(' :
                check = False
                break
            stack.pop()

                
    if check and not stack :
        answer.append ("yes")
    else :
        answer.append("no")



for ans in answer :
    print (ans)