import sys
from collections import Counter
word = sys.stdin.readline().rstrip("\n").upper()

counter= Counter(word)
most = counter.most_common(2)

first_item= most[0]

prev_val = first_item[1]


for i in range (1,len(most)) :
    cur_item = most[i]
    
    if prev_val == cur_item[1] : 
        print ("?")
        sys.exit(0)


print (first_item[0])

    
    
    
    
    