import sys

N = int(sys.stdin.readline())

expected_scores = []

for _ in range (N) :
    score =int(sys.stdin.readline())
    expected_scores.append(score)

# 불만도의 합을 최소로 하는 프로그램

# 1 2 3 4 5 
# 2명 1명 1명 0명 1명

# A-B
# 불만도의 총 합을 최소로 하면서, 등수를 매기려고한다


expected_scores.sort()
ans = 0

for i in range (N) :
    ans += abs(expected_scores[i] -(i+1))

print(ans)