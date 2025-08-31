import sys

#숌스럽게 바꾸면 비슷한 단어
#숌스럽게? -> 단어 a에 등장하는 모든 알파벳-> 다른 알파벳으로
#순서는 바뀌지 않음, 두개의 다른 알파벳을 하나의 알파벳으로x, 임의의 알파벳-> 자기자신 가능

# abca하고 zbxz는 비슷


n = int(sys.stdin.readline())

li = []
for _ in range (n) :
    w = sys.stdin.readline().strip("\n")
    
    before_word = []
    new_count = 1
    change_01 = ""
    before_word.append(w[0])
    change_01 +="0"
    for i in range (1, len(w)):
        if w[i] not in before_word :
            change_01+=str(new_count)
            before_word.append(w[i])
            new_count +=1
        
        else: change_01+=str(before_word.index(w[i]))

    li.append(change_01)

answer = 0

for i in range (n) :
    for j in range(i+1,n) :
        if li[i] == li[j]:
            answer +=1

print (answer)