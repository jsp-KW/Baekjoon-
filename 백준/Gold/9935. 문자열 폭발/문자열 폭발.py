import sys

# 문자열이, 폭발 문자열 포함시 모두 폭발
# 새로 생긴 문자열 : 남은 문자열 붙여서 새로운 문자열로 만듬
# 폭발 문자열이 문자열에 없을 때까지 계속
#  남아있는 문자 x -> FRULA 


string = sys.stdin.readline().rstrip()
bomb =sys.stdin.readline().rstrip()

last = bomb[-1]
bomb_len = len(bomb)

answer = ""

stack = []

for ch in string :

    stack.append (ch)

    if ''.join(stack[-bomb_len:])  == bomb  and  len(stack)>= bomb_len :
            del stack[-bomb_len:]

answer = ''.join(stack)
print(answer if answer else "FRULA")