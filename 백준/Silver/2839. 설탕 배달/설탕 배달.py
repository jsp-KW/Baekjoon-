import sys
input = sys.stdin.readline

# 3kg, 5kg 봉지 있음


n = int (input())

count = 0


while n >=0 :
    if n % 5 ==0 :
        count +=int(n //5)
        print (count)
        break

    n = n-3
    count +=1

else :
    print (-1)