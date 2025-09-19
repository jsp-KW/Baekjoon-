import sys


# NXN

N,M = map(int,sys.stdin.readline().split())

maps = []

for _ in range (N) :
    line = list(map(int,sys.stdin.readline().split()))
    maps.append(line)


#누적합 배열 만들기
# 1,1 ~ 해당 좌표까지의 직사각형 모양의 합

prefix = [[0]*(N+1) for _ in range (N+1)]

for i in range (1,N+1) :
    for j in range (1,N+1) :
        prefix[i][j] = maps[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]




answer= []
for _ in range (M) :
    tar = list(map(int,sys.stdin.readline().split()))
    
    start_x,start_y = tar[0],tar[1]
    end_x,end_y = tar[2],tar[3]

    # sum = 0

    # for i in range (start_x,end_x +1) :
    #     for j in range (start_y,end_y +1) :
    #         sum += maps[i][j]

    # 마지막좌표 기준으로 직사각형부분합 - 시작좌표 x-1부터 마지막좌표y(위쪽) - 시작좌표 열 -1부터 종료좌표 열까지(왼쪽) + 두번 빠진 곳 보충
    sum = prefix[end_x][end_y]-prefix[start_x-1][end_y] -prefix[end_x][start_y-1] +prefix[start_x-1][start_y-1]
    answer.append(sum)

for ans in answer :
    print (ans)