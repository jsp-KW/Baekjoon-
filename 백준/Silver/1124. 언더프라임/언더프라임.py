import sys

# 자연수 x를 소인수분해 -> 곱해서 x가 되는 소수의 목록을 얻을 수 있음
# 12 -> 2* 2 * 3 1은 소수가 아님

# 소인수 분해해서 소수의 목록길이가 소수라면, 언더프라임

# 입력 정수 A,B
# 출력 A보다 크거나 같고, B보다 작거나 같은 언더프라임 개수

def is_prime(n) :
    if n<2 :
        return False
    for i in range (2, int(n**0.5)+1) :
        if n% i == 0 :
            return False
    return True

A,B = map(int, sys.stdin.readline().split())



result= 0
for num in range (A,B+1) :
    
    temp =  num
    is_underPrime = []

    # while num % 2  == 0 :
    #     is_underPrime.append(2)
    #     num =num// 2
    # while num% 3 ==0 :
    #     is_underPrime.append(3)
    #     num = num//3
    # while num % 5 == 0:
    #     is_underPrime.append(5)
    #     num //= 5

    # while num % 7 == 0:
    #     is_underPrime.append(7)
    #     num //= 7
    
    # if num >1 :
    #     is_underPrime.append(num)

    # if is_prime(len(is_underPrime)) :
    #     result+=1

    div =  2 
    while div * div <= temp :
        while temp % div == 0 :
            is_underPrime.append(div)
            temp = temp // div
        div +=1

    if temp >1 :
        is_underPrime.append(temp)
    
    if is_prime(len(is_underPrime)) :
        result +=1

print (result)

