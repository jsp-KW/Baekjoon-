#r행일때, 최대 r-1까지 행을 지울수잇음

#일단 지우고 r이 2일때, 1번지웟는데 중복발생시->해당카운트 0출력
# 1행 지우고 ->중복이 없어야 count +1
# 중복있는 경우, break 후 바로 count증가
import sys
r,c = map(int,sys.stdin.readline().split())

saving_strs= []

for _ in range(r):
    get_str = sys.stdin.readline().rstrip("\n")
    saving_strs.append(get_str)

count =0

cols_str= []
for col in range(c):
    s=""
    for row in range(r):
        s+=saving_strs[row][col]
    cols_str.append(s)


def is_duplicate(cols,start_row):


    seen = set()
    for s in cols:
        t= s[start_row:]
        if t in seen:
            return True
        seen.add(t)
    return False

            
        

after_start_row= 0
while True :

    after_start_row +=1
    
    if after_start_row >=r:
         break
         
    if is_duplicate(cols_str,after_start_row):
         break
    else:
         count+=1

print(count)


