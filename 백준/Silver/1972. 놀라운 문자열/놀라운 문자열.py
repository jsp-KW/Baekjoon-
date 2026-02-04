import sys

# 길이가 N, N-2쌍까지 정의
# 

answers = []
while True :
    target = sys.stdin.readline().rstrip()
    
    if target == '*' :
        break

    n = len(target) 
    check = True
    for i in range (n-1):
        s = set ()
        for j in range (0,n-i-1) :
            put = target[j] + target[j+i+1]
            if put not in s :
                s.add (put)
            else : 
                check = False
                break

    if not check :
        answers.append(target+ " is NOT surprising.")
    else :
         answers.append (target + " is surprising.")

for ans in answers:
    print (ans)
     