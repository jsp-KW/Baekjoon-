import sys

N,M = map(int,sys.stdin.readline().split())

# 1. 자주 나오는 단어 앞으로
# 2. 해당 단어 길이 길수록
# 3. 알파벳 사전순 앞에있는 단어일수록 앞에 배치

word_dict = {}
# 외울 단어의 길이 기준이 되는 M
# M이상의 단어만 외운다
for _ in range (N) :
    word = sys.stdin.readline().strip()
    if word not in word_dict  :
        word_dict[word] =1
    else :
        word_dict [word] +=1 


li = list(word_dict.items())
li.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for t in li :
    if len(t[0]) >= M :
        print (t[0])
