def solution(board):
    answer = 0

    row = len(board)
    col = len(board[0])

    dp = [[0] * col for _ in range(row)]

    for y in range(row):
        for x in range(col):
            if board[y][x] == 1:
                if y == 0 or x == 0:
                    dp[y][x] = 1
                else:
                    dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1

                answer = max(answer, dp[y][x])
            else:
                continue

    return answer * answer