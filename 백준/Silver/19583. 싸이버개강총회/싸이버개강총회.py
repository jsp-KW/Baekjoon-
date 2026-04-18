import sys


# 시작 이전의 채팅기록 닉네임 확인, 시작하자마자 남긴 회원도 확인

S,E,Q =map(str, sys.stdin.readline().split()) #시작, 개총 끝, 스트리밍 끝

start = int(S.split(":")[0] )*60 + int(S.split(":")[1]) 
end=  int(E.split(":")[0] )*60 + int(E.split(":")[1]) 
stream_end = int(Q.split(":")[0] )*60 + int(Q.split(":")[1]) 


cnt = 0 
in_members = set()
out_members =  set()
while True :
    line= sys.stdin.readline().rstrip()
    line = line
    if not line :
        break
    time,nickName = line.split()
    
    check_time = int (time.split(":")[0])*(60) +  int(time.split(":")[1]) 
    if  check_time <= start :
        in_members.add(nickName)
    
    if end <= check_time <= stream_end  :
        out_members.add(nickName)


print(len(in_members & out_members))


