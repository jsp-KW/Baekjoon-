import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    a, b = map(int, input().split())
    last = pow(a % 10, b, 10)           # a^b의 끝자리
    out.append('10' if last == 0 else str(last))  # 0이면 10번
print('\n'.join(out))
