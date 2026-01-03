import sys

# a ,e  , i , o , u 하나를 반드시 포함
# 모음 3개, 혹은 자음 3개 연속으로 오면 x
# 같은글자 연속 두번 x이지만, ee와 oo는 허용


answers = []


while True :
    password = sys.stdin.readline().rstrip("\n")
    check = [0]*(len(password))

    if password == 'end' :
        break

    
    if not any(ch in "aeiou" for ch in password):
        answers.append ("<"+password +">" + " is not acceptable.")
        continue

    prev_value = None
    bad_case = 0

    for i  in range (len (password)) :
        cur_val= password[i]
        if i >=1:
            if prev_value == cur_val and cur_val not in ('e', 'o') :
                bad_case =1
                break
                
        if password[i] not in "aeiou" : #모음이면, 0 ,자음이면 1, 예외적인 e이면 2 ,o 면 3
            check[i] = 1
        elif password[i] == 'e' :
            check[i] =2
        elif password[i] == 'o' :
            check[i] =3 
        elif password[i] in "aiu" :
            check[i] =0

        prev_value = cur_val

    successive_vowels = 0
    successive_cons = 0
    isOk = 1 
    if bad_case :
        answers.append  ("<"+password +">" + " is not acceptable.")
        continue
    
    for value in check :

        
        if value == 0 : # 모음
            if successive_cons  != 0 : # 자음이 0이 아니라면, 
                successive_cons = 0 # 흐름끊기
                successive_vowels +=1
            else :
                successive_vowels +=1

        elif value == 1:  # 자음
            if successive_vowels != 0: #모음이 0이 아니라면,
                successive_vowels = 0
                successive_cons +=1
            else: 
                successive_cons +=1
            

        elif value == 2  or value ==3 : #모음인데 , e
            if successive_cons != 0 : 
                successive_cons = 0
                successive_vowels +=1
            else :
                successive_vowels +=1
        
        if successive_vowels >=3 or successive_cons >=3 :
            isOk = 0
            break
       
    
    if isOk  :
        answers.append  ("<"+password+">" + " is acceptable.")
    else:
        
        answers.append  ("<"+password +">" + " is not acceptable.")

  
for ans in answers :
    print(ans)