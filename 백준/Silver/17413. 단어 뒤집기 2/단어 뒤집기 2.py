import sys
S = sys.stdin.readline().rstrip()

# < > 사이에는 소문자 알파벳 or  공백만존재

no_reverse = 0
answers = ""
reverse_target  = []

for ch in S :
    if ch == '<' and no_reverse ==0 :
        if reverse_target : 
            answers += "".join(reversed(reverse_target))
            reverse_target.clear()
    
        answers += ch
        no_reverse =1

    elif ch == '>' and no_reverse ==1:
        answers+= ch
        no_reverse =0
    
    elif no_reverse == 1:
        answers+= ch

    elif ch == ' ':
        
        if reverse_target :
            answers += "".join(reversed(reverse_target))
            reverse_target.clear()
        answers+= ' '

    else :
        reverse_target.append(ch)
    

if reverse_target :
    answers+= "".join(reversed(reverse_target))
    
print(answers)



    



