import sys


# N명
# M 명의 마음을 모두 읽음
# 기호 1번이고, 1:5 /2 :7 3:7 이면, 2번후보 1명과, 3번후보 1명을돈으로 매수
# 매수해야하는 사람의 최소값은?

N = int(sys.stdin.readline())

people = []
for _ in range (N) :
    temp = int(sys.stdin.readline())
    people.append(temp)


dasom = people[0]
others = people[1:N]


if N == 1 :
    print(0)
    exit()

count = 0
while True :
    others.sort(reverse=True)
    if dasom > others[0] :
        break

    others[0] -=1
    dasom +=1
    count +=1


print(count)