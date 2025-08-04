n = int(input())
a = list(map(int, input().split()))

visited = [False] * n
cnt = 0

for i in range(n):
    if not visited[i]:
        cnt += 1
        visited[i] = True
        j = a[i]
        while j != i:
            visited[j] = True
            j = a[j]

if cnt == 1:
    print(0)
else:
    print(cnt)
