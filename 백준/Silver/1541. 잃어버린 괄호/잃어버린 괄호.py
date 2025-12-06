import sys

s = sys.stdin.readline().rstrip("\n")

if not s  :
    exit()
# split 을 활용하여 먼저 쪼갠후,
# 맨처음은 더하고, 나머지 -로
# 가장 처음과 마지막은 숫자이기 때문에, 처음은 양수가 나옴
# 괄호 안 값이 커야 최소

result = 0


split_s = s.split("-")

if len(split_s) == 1:
    print(sum(map(int,s.split("+"))))
else:

    result += sum(map(int,split_s[0].split("+")))
    # 두번째 부분부터 + 값 다더하고 빼주면 최소
    for i in range (1,len(split_s)):
        result = result - sum(map(int,split_s[i].split("+")))


    print (result)
    