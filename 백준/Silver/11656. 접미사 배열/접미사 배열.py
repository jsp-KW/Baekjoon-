import sys

# 접비사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해놓은 배열
#
S = sys.stdin.readline().rstrip()
answers = []
for i in range (0, len(S)) :
    temp = S[i:]
    answers.append(temp)

answers.sort ()
for a in answers:
    print(a)