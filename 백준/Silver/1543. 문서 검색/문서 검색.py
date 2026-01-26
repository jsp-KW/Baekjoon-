import sys

# 몇번 등장?
# 문서 abababa 이고, 찾으려는 단어 ababa 라면, 0번째부터 찾을수있고, 2번부터 찾을 수 있음

sentence = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()


len_target = len(target) 
answer = 0
skip = -1
for i in range (0, len(sentence)-len_target +1) :
    if i < skip :
        continue
    
    if target[0] == sentence[i] :

        if sentence[i:i+len_target]  ==  target :
            answer +=1
            skip= i+len_target
   
print(answer)

    
    