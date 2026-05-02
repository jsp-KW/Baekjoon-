from collections import Counter 

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    list1 = []
    list2 = []
    
    for i in range (0, len(str1) -1) :
        test = str1[i:i+2]
        if test.isalpha() :
            list1.append(test)
    for i in range (0, len(str2) -1):
        test = str2[i:i+2]
        if test.isalpha() :
            list2.append(test)
    
    c1 = Counter (list1)
    c2 = Counter (list2)
    
    if not c1 and not c2 :
        return 65536
    
    interaction = c1&c2 
    union = c1 | c2
    
    
    same_len = sum (interaction.values())
    add_len = sum (union.values())
  
    
    result = (same_len / add_len)*(65536)
    
    
    
    return int(result)