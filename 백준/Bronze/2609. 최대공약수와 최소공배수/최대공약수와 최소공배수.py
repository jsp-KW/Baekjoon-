import sys

num1, num2 = map(int, sys.stdin.readline().split())

def gcd (a,b) :
    while b!=0 :
        temp = b
        b = a % b
        a = temp
    
    return a


result1 = 0
if num1 >= num2 : result1 = gcd (num1, num2)
else : result1 = gcd (num1, num2)


result2 = (num1*num2) // result1 

print (result1)
print (result2)
