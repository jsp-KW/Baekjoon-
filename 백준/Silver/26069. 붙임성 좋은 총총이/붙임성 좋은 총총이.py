import sys

N = int(sys.stdin.readline())
#ChongChong

dance ={'ChongChong'}
# key : 이름 value : -1 춤x, 1춤 ㅇ

for _ in range (N) :
    A,B = map(str, sys.stdin.readline().split())
    if A not in dance and B in dance :
        dance.add(A)
    if A in dance and B not in dance :
        dance.add(B)


print(len(dance))