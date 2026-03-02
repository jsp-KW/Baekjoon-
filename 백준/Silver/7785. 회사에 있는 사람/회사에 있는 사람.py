import sys


n = int(sys.stdin.readline())

logs= set()
for _ in range (n) :
    people,status = map(str,sys.stdin.readline().split())
    if status == 'enter' :
        logs.add(people)
    elif status == 'leave' :
        if people in logs :
            logs.remove(people)
        else :
            continue


answers = list(logs)

answers.sort(reverse=True)

for ans in answers:
    print(ans)