import sys

num = (int(sys.stdin.readline()))

if num == 0 :
    print(0)
    print("NO")
    sys.exit(0)
elif num >=1  and num <10 :
    if num ==3 or num==6 or num==9 :
        print(0)
        print("YES")
        sys.exit(0)
    else :
        print(0)
        print('NO')
        sys.exit(0)
        
cnt = 0
Y =0
X= str(num)

while True :
    temp = 0
    Y=X
    for ch in Y :
        temp+= int(ch)
    
    if temp < 10 :
        if temp %3 ==0  and temp!=0:
            print(cnt+1)
            print("YES")
        else:
            print(cnt+1)
            print("NO")
        break
    if temp >=10 :
        X= str(temp)
        cnt+=1
    
