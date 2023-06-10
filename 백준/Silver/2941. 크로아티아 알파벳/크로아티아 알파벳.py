import sys

cro_word = ["c=","c-","dz=", "d-","lj","nj","s=","z="]

string = sys.stdin.readline().rstrip()

for s in cro_word:
    string = string.replace(s,"!")
    
print (len(string))
