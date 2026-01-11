import sys

S = sys.stdin.readline().rstrip("\n")

window_size = 1

sub_str = []

while window_size <= len(S) :
    for i in range (0, len(S)-window_size+1) :
        temp = S[i:i+window_size] 
        sub_str.append(temp)
    
    window_size +=1 

print(len(set(sub_str)))
        