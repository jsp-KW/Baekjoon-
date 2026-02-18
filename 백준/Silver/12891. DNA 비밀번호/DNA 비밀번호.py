import sys


# 모든 문자가 A,C,G,T 로 이루어져 있으면 DNA 문장ㄹ
# DNA 문자열 만들고, 부분문자열을 비밀번호로 사용하기로 마음먹었음


temp_pwd_len , use_pwd_len = map(int,sys.stdin.readline().split())

make_str = sys.stdin.readline().rstrip()

# A C G T  의 최소개수

conditions = list (map(int,sys.stdin.readline().split()))
dic =  {'A':0, 'C': 0,"G":0 ,"T" :0}
# A: 0, C:1 ,G:2, T:3 index
cnt = 0

for i in range (0,use_pwd_len):
    dic[make_str[i]] +=1

if dic['A'] >= conditions [0] and dic['C'] >= conditions[1] and dic['G'] >= conditions[2] and  dic['T'] >= conditions[3] :
    cnt +=1


# 한칸씩 슬라이딩
# 오른쪽을 기준i 로, 왼쪽에서 빠지는건 i에서 used_pwd_len 을 빼주는것, 

for i in range (use_pwd_len, temp_pwd_len) :
    dic[make_str[i]] +=1

    dic[make_str[i-use_pwd_len]] -=1 
    if dic['A'] >= conditions [0] and dic['C'] >= conditions[1] and dic['G'] >= conditions[2] and  dic['T'] >= conditions[3] :
     cnt +=1




print(cnt)