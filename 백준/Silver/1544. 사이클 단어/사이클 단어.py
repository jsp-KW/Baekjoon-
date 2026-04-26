import sys

n = int(sys.stdin.readline())
words= [] 

for _ in range (n) :
    word = sys.stdin.readline().rstrip("\n")
    if not words :
        words.append(word)

    else:

        is_same = False

        for base in words : 
            if len(word) == len(base) and word in base+ base :
                is_same = True
                break
        
        if not is_same  :
            words.append(word)


print(len(words))
                
