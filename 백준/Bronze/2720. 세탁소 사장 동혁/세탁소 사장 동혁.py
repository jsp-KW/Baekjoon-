import sys
t = int(input())
li= []
for i in range (t) :
    c = int(input())
    li.append(c)


for cent in li :
    sub = []
    sub.append(cent // 25 )
    cent = cent % 25
 
    sub.append(cent // 10)
    cent = cent % 10
  
    sub.append(cent // 5)
    cent = cent % 5

 
    sub.append(cent// 1)
    cent = cent % 1
  
 
    print(*sub)   