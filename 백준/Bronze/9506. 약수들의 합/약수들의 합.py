import sys

answers = []
while True :
    n = int (sys.stdin.readline())
    if n == -1 :
        break
    
    divisions = []

    for i in range (1,n) :
        if n% i == 0  :
            divisions.append(i)

        
    if sum(divisions) == n :
     
        answer = "" 
        answer+=(str(n) +" = " + "")
        for i in range (0,len(divisions)) :
            if i == len(divisions) -1 :
                answer+=( str(divisions[i]))
            else: answer+=(str(divisions[i]) + " + ")
        
        answers.append(answer)

    else :
        answers.append(str(n)+ " is NOT perfect.")

for ans in answers :
    print (ans)