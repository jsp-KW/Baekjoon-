import re
def solution(myStr):
    answer = []
    # a, b , c 를 구분자로 사용
    split_li = ["a","b","c"]
    
    new_str = ""
    
    for ch in myStr :
        if ch in split_li : # 구분자 문자열을 공백으로 만들자
            new_str += ' '
        else:
            new_str += ch

    result = new_str.split()
    
    if not result :
        return ["EMPTY"] 
    else:
        return result
            
            
   
    return answer