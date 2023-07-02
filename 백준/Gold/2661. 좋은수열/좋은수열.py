
def bad_seq (s):
    length = len(s) 
    for i in range(1,length//2 +1) :
        if   s [-i:] == s[-2*i : -i]:
            return True
    return False

def good_seq (N, s =""):
    if len(s) ==N:
        print(s)
        exit(0)
    for num in "123" :
        next_s = s+num 
        if not bad_seq(next_s):
            good_seq(N, next_s)

N = int (input())
good_seq(N)
