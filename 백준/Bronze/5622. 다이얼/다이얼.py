import sys

dic =  {'WXYXZ' : 10,  'TUV':9 , 'PQRS': 8 ,'MNO' : 7 ,
        'JKL': 6, 'GHI':5 , 'DEF': 4, 'ABC':3 
        
        }

s = sys.stdin.readline().rstrip() 
answer = 0
for ch in s :
   for k,v in dic.items() :
      if ch in k :
         answer+= v


print(answer)