import sys

# N개의 문자로 이루어진 문자열 S
# S로 문자열 T를 만드는 규칙
# S의 가장 앞의 문자 하나를 문자열 T 마지막에 추가
# S의 가장 뒤의 문자 하나를 문자열 T의 마지막에 추가

sentence =[]

N = int (sys.stdin.readline())

T = ""
for _ in range (N) :
    word = sys.stdin.readline().rstrip("\n")
    sentence.append(word)

cnt = 0
l,r =  0, N-1

while l <= r :
   
    if cnt == 80 :
        T += "\n"
        cnt = 0
    start_word=sentence[l]
    back_word= sentence[r]
  
    if start_word <  back_word :
        T+= start_word
        l = l+1
    elif start_word > back_word :
        T += back_word
        r=  r-1
        
    
    else :
        
        left, right =  l+1, r -1
        check = False
        while left <=right :
            if sentence[left] < sentence[right] :
                T+= start_word
                l = l+1
                check = True
                break
            elif sentence[left] > sentence[right] :
                T += back_word
                r = r -1 
                check =True
                break
            else : 
                left +=1 
                right-=1
        
        if not check :
            T += start_word 
            l = l+1

    cnt +=1 

print (T)
