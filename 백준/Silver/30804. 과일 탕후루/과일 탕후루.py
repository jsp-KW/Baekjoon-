import sys

N = int(sys.stdin.readline())

fruits = list(map(int,sys.stdin.readline().split()))

# 앞에서 a개 빼고, 뒤에서 b 개를 빼서, 두종류 이하로 만들어야함
# 그렇다면, N - (a+b) 일거고,

# [L..R]
# R을 한칸 늘려서 과일을 넣고, 종류가 3개가 되면, L을 오른쪽으로 밀고,
# 매순간마다 윈도우 길이 R-L

cnt = [0]*(10)
fruit_type = 0

L = 0
R = 0
answer = 0

# 5 1 1 2 1  -> 1번째 과일 5번, 2번째 과일 1번, 3번째 과일 1번 4번째 과일 2번, 5번째 과일 1번

while R < N :
    x = fruits[R] 
    if cnt[x] == 0 : 
        fruit_type+=1
    cnt[x] +=1
    R+=1

    while fruit_type > 2:
        y = fruits[L]
        cnt[y] -=1
        if cnt[y] == 0 :
            fruit_type -=1 
        L+=1

    answer = max (answer, R-L)

print(answer)