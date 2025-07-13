d = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                d[i][j][k] = 1
            elif i < j < k:
                d[i][j][k] = d[i][j][k - 1] + d[i][j - 1][k - 1] - d[i][j - 1][k]
            else:
                d[i][j][k] = (
                    d[i - 1][j][k]
                    + d[i - 1][j - 1][k]
                    + d[i - 1][j][k - 1]
                    - d[i - 1][j - 1][k - 1]
                )

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0: 
        ans = 1
    elif a > 20 or b > 20 or c > 20:
        ans = d[20][20][20]
    else:
        ans = d[a][b][c]
    print(f"w({a}, {b}, {c}) = {ans}")
