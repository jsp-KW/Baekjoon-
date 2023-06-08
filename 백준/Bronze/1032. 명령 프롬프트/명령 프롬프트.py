
n = int(input())

li =[]

for i in range (n):
    li.append(input().rstrip())

result = ""

for i in range (len(li[0])) :

    char = li[0][i]
    same_char = all (ch[i]== char for ch in li)

    if same_char :
        result += char
    else:
        result +="?"



print (result)

    
