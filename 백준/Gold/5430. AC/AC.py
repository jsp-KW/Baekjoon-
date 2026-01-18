import sys
from collections import deque
#AC 정수배열 연산을 하기 위해 만든 언어
#R 뒤집기, D 버리기

# R 은 배열에 있는 수의 순서를 뒤집는 함수
# D 는 첫번째 수를 버리는 함수
# 배열이 비어있는데 D 함수 사용 -> ERROR
#함수는 조합해서 한번에 사용할 수 있음

T = int (sys.stdin.readline())
answers = []
for _ in range (T) :
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()
    if n == 0 :
        numbers = []
    else : 
        inside = arr[1:-1]
        numbers = inside.split(',')
    rev = False
    l,r = 0,n-1
    ok = True
    for op in p :
        if op == 'R' :
            rev = not rev
        else : # 지울 때, 
            if l>r :
                answers.append('error')
                ok = False
                break
            if not rev:
                l = l+1
            else :
                r= r-1
    if ok :
        if l> r :
            answers.append("[]")
        else :
            if not rev :
                part = numbers [l:r+1]
            else :
                part = numbers [l:r+1] [::-1]
            answers.append("[" + ",".join(part)+ "]")
            
    

for ans in answers:
    print(ans)            
    

