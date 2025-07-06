import sys

sys.setrecursionlimit(10000)
# M : 가로 길이 N :세로길이
# K  배추가 심어져 있는 위치 개수
# 출력 : 각 테스트 케이스에 따른 필요한 최소의 배추흰 지렁이 마리 수

T = int(sys.stdin.readline())

# 상 하 좌 우  : 네 방향에 다른 배추가 위치한 경우 서로 인접한 것

def dfs(y, x):
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if make_map[y][x] == 0:
        return
    make_map[y][x] = 0
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # 가로 세로 배추 수

    make_map = [[0] * M for _ in range(N)]  # N행 M열

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        make_map[y][x] = 1

    answer = 0
    for y in range(N):
        for x in range(M):
            if make_map[y][x] == 1:
                dfs(y, x)
                answer += 1

    print(answer)
