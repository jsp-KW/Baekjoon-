import sys

N  = int(sys.stdin.readline())
# 나이순, 먼저가입한 사람이 앞에 오는 순서대로 정렬

cnt = 0
people = []
for _ in range (N) :
    age, name = map(str, sys.stdin.readline().split())
    people.append((int(age),cnt,name))
    cnt +=1

people.sort(key= lambda x : (x[0],x[1]))

for age,_,name in people :
    print(age, name)

