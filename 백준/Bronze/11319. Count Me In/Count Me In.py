import sys

N = int(sys.stdin.readline())

sentence = []
for i in range(0,N) :
    temp = sys.stdin.readline().rstrip() # 줄바꿈 제거 꼭 써주기!!! 밑에 출력때 하나 더 세짐
    sentence.append(temp)



vowels = ['A','E','I','O','U','a','e','i','o','u']
for s in sentence:
    answer = 0
    consonants = 0
    for ch in s:
        if ch == ' ':
            continue
        elif ch in vowels:
            answer +=1
        else :
            consonants +=1

    print (consonants , answer)


# strip()	좌우 모든 공백 (' ', \t, \n)문자열 전체 정리할 때
# rstrip()	오른쪽 끝만	readline() + 줄바꿈 제거할 때 
# lstrip()	왼쪽만	필요할 땐 거의 없음 (특수 케이스)
