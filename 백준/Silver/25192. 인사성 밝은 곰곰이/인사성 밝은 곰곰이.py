import sys


#엔터는 새로운 사람이 채팅방에 입장
# 새로운 사람 입장후 처음 채팅 입력하는 사람은 반드시 곰곰티콘
# 횟수는?
 

N = int(sys.stdin.readline())

users  =set ()
answer = 0

for _ in range (0,N) :
    inputs =  sys.stdin.readline().rstrip("\n")
  
    if inputs == 'ENTER' :
        answer+= len(users)
        users.clear()
    else :
        users.add(inputs)

answer +=  len(users)
print(answer)

