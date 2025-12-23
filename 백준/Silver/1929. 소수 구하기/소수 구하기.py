import sys
import math

n1,n2 = map(int,sys.stdin.readline().split())

for number in range (n1, n2+1) :
    if number <2 :
      continue
   
    prime_check = True 
    for i in range(2, int(math.sqrt(number)+1)) :
      if number % i ==0 :
        prime_check = False
        break
    

    if prime_check : print (number)
    
