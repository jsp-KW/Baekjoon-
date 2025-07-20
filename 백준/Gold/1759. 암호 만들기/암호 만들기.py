import sys
from itertools import combinations

#최소 1개의 모음 a,e,i,o,u
#최소 2개의 자음
#오름차순 배열로 추측
#사용했을만한 암호 문자의 종류 c가지


#c개의 문자들이 주어졌을때, 가능성이 있는 암호들을 구하라

#입력  : L,C
#소문자이고, 중복되는 건 X

def check(sentence) :
    vowels ='aeiou'
    vowel_cnt = 0
    consonant_cnt = 0
    for s in sentence :
        if s in vowels:
            vowel_cnt +=1
        else:
            consonant_cnt+=1
    
    if vowel_cnt >=1 and consonant_cnt >=2 :
        return True
    else:
        return False
    

answers = []
L,C = map(int, sys.stdin.readline().split())
characters = list(map(str,sys.stdin.readline().split()))
characters.sort()

for combination in combinations(characters,L) :
    one_set = (''.join(map(str,(combination))))
    if check(one_set) == True:
        answers.append(one_set)
    else:
        continue


for ans in answers :
    print (ans)
