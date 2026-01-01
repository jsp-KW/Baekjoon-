import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

# 길이가 N인 수열
# 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러번 등장하지 않는 경우의 수
# 투 포인터는 매 r마다 ‘중복 없는 suffix의 개수’를 한 번에 더하는 알고리즘
visited = [False] * 100001

l = 0
ans = 0 

for r in range (N) :
    while visited [numbers[r]] :
        visited[numbers[l]] =  False
        l +=1

    visited[numbers[r]] = True
    ans += (r-l +1)


print (ans)