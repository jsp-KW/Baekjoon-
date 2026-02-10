import sys

t = int(sys.stdin.readline())

answers= []

for _ in range (t) :
    phone= []
    phone_nums_len = int(sys.stdin.readline())
    for _ in range(phone_nums_len):
        temp = sys.stdin.readline().rstrip()
        phone.append(temp)
    phone.sort()
    is_consistent = True
    for i in range (len(phone)-1) :
        if phone[i+1].startswith(phone[i]):
            is_consistent = False
    
    if is_consistent : answers.append("YES")
    else : answers.append("NO")


for ans in answers:
    print(ans)


