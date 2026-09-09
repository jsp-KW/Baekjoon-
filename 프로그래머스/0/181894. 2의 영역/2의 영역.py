def solution(arr):
    answer = []
    
    left = -1
    right = -1
    for i in range (0,len(arr)): 
        if arr[i] == 2 and left ==-1:
            left = i
        elif arr[i] ==2 and left != -1 :
            right = i
    
    if left ==- 1:
        return [-1]
    if right ==-1 :
        return arr[left :left+1]
    
    
    return arr[left:right+1]
     