import sys

N, M = map(int,sys.stdin.readline().split())


dic = {0:"zero",1:"one",2:"two" ,3:"three" ,4:"four",5:"five",6:"six",7:"seven",8:"eight", 9:"nine"}

nums = [ (str(i)) for i in range (N, M+1)]

new_list = []
for n in nums :
    if len(n) == 1:
        new_list.append((dic[int(n)], n))
    
    elif len(n)==2  :
        
        temp = dic[int(n[0])] + " " + dic[int (n[1])]
        new_list.append((temp,n))


new_list.sort(key= lambda x: (x[0]))

cnt= 0
answer= ""
for i in range (0, len(new_list)):
    if cnt ==10:
        answer+="\n"
        cnt =0
    answer+= new_list[i][1] + " " 
    cnt +=1
    
print(answer)