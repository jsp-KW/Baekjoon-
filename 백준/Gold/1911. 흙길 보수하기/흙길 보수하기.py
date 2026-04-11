import sys

# N개의 물 웅덩이
# L 길이의 널빤지
# 최소개수를 구하자

N, L = map(int,sys.stdin.readline().split())
holes =[]
for _ in range (N) :
    start, end = map(int,sys.stdin.readline().split())
    holes.append((start,end))

holes.sort()

current  = 0
answer = 0

for s,e in holes :
    s = max(s,current)
   
    if s>= e :
        continue 

    length = e - s
    cnt = length // L 
    if length%L != 0 :
        cnt +=1

    answer +=cnt 
    current = s + cnt * L 

print(answer)