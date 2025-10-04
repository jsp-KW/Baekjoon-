import sys

# 가로로 2칸, 세로로 N 칸 
# 입력 : 우리의 크기 N
# 출력: 사자를 배치하는 경우의 수를 9901로 나눈 나머지를 출력하기

# 우리 총 크기 2N
# 쉽게 생각하면
# 사자를 놓을 방법은 총 3가지이다
# 아무 사자도 놓지 않은 경우, 첫번째 열에 놓는 경우, 두번째 열에 놓는경우

# 만약 I번째 행에 아무사자도 놓지 않는다면? -> I-1번째 행에는 3가지 경우 다 해도 괜찮
# 왼쪽에 놓는다면 -> 오른쪽, 아무 사자도 놓지 않은 경우 
# 오른쪽은 왼쪽과 비슷하게 구하면
# 밑 수식이 완성

N = int(sys.stdin.readline().rstrip())

# dp = [[0]*(3)for _ in range (N+1)]

# dp[1][0] = 1
# dp[1][1] = 1
# dp[1][2] = 1

prev = [1,1,1]
for i in range (2,N+1) :
    
    temp = [0,0,0]
    temp[0] = (prev[0]+prev[1]+prev[2])
    temp[1] = (prev[2] + prev[0])
    temp[2] = (prev[1]+ prev[0])
    prev = temp


answer = (prev[0]+prev[1]+prev[2])% 9901
print(answer)