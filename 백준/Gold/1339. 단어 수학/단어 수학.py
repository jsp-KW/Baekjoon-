import sys


N = int (sys.stdin.readline())

# 단어는 N개 대문자로만, 0~9까지의 숫자중 하나만 바꿔서 N개의 수를 합한다
# 같은 알파벳은 같은숫자, 두개이상의 알파벳이 같은 숫자로 바뀌어지면 안된다.
# 
words = []
for _  in range (N) :
    temp = sys.stdin.readline().rstrip()
    words.append(temp)

ch_weights = {}
for word in words :
    for i in range (0, len(word)) :
        weight = 10**(len(word)-i-1)
        ch = word[i]
        
        if ch in ch_weights :
            ch_weights[ch] +=weight
        else :
            ch_weights[ch] = weight


weights = sorted (ch_weights.values (), reverse= True)
# i번째 숫자 안썻으면 -1, 썻으면 해당 숫자로 초기화

# 합이 최대가 되려면? , 큰숫자가 앞자리에 있어야함

num = 9
ans =0
for w in weights :
    ans += w*num
    num-=1

print (ans)