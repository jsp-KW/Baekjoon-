#소수 :  2부터 1하고 본인만 약수로 가지는 수
from itertools import permutations
import math
def solution(numbers):
    answer = 0
    candidates = set()
    for i in range (1,len(numbers) +1 ) :
        for p in permutations(numbers,i) :
            candidates.add (int(''.join(p)))
    answer = len(candidates)
    
    for target in candidates :
        if target <= 1 :
            answer -=1
            continue
        if target == 2 :
            continue
        else:
            if target % 2 ==  0 :
                answer-=1
                continue
                
            for i in range (3, target) :
                if target%i == 0 :
                    answer-=1
                    break
        
                
    return answer