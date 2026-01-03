import sys
from collections import deque
N = int (sys.stdin.readline())
# deque 으로 구현

answers = []
q = deque()

for _ in range (N) :
   
    operation = sys.stdin.readline().rstrip("\n")
    
    if "push" in operation  :

        op, num = operation.split()[0] , int(operation.split()[1])

        if op == 'push_back' :
            q.append(num)
        
        elif op == 'push_front':
            q.appendleft(num)

    elif "pop" in operation :
            if operation == 'pop_back' :
                if len(q) == 0: answers.append(-1)
                else: answers.append(q.pop())
            
            elif operation == 'pop_front' : 
                if len(q) == 0 : answers.append (-1)
                else: answers.append(q.popleft())


    else:
        if operation == 'size' :
            answers.append(len(q))
        elif operation == 'empty' :
            if len(q) == 0 : answers.append(1)
            else: answers.append(0)
        
        elif operation == 'front' :
            if len(q) > 0: answers.append(q[0])
            else : answers.append (-1) 
        elif operation == 'back' :
            if len(q) > 0 : answers.append(q[-1])
            else : answers.append(-1)


for ans in answers:
    print(ans)
    
        

