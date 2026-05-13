from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    li = list (map(str, numbers))
    
    def compare (a,b) :
        if a+b > b+a :
            return -1
        elif a+b < b+a :
            return 1
        else :
            return 0
        
    li.sort (key=cmp_to_key(compare))
    
    
    if li[0] == '0' :
        return "0"

    return ''.join(li)