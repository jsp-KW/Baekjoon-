def solution(arr):
    answer = 0
    # n개의 수들의 배수중 공통이 되는 가장 작은 숫자
    
    
    def gcd (a,b) :
        while b!=0 :
            temp = a% b
            a=b
            b= temp
        return a
    
  
    # 2 / 684
    # 6
    while len(arr) >1 :
        
        first = arr[0] #2
        
        target = arr[1:] # 6 8 14
        
        second = target[0] # 6
        
        res = (first * second) // gcd (first, second) 
        arr[0] = res 
        arr.pop(1)
       # 6 6 8 14
       # 6 8 14
       # 24 14
       # 168

    return arr[0]