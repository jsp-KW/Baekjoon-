def solution(my_string, target):
    answer = 0
    length = len(target)
    if length ==1 :
        if target in my_string :
            return 1
        else:
            return 0
    else:
        for i in range (0, len(my_string) - length+1) :
            check = my_string[i:i+length]
            if check == target :
                return 1

    return answer