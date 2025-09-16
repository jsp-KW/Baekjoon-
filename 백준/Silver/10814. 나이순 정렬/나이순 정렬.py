import sys

n = int (sys.stdin.readline())

people = []
register_cnt = 0
for _ in range (n) :
    line =list( map(str,sys.stdin.readline().split()))
    age = int(line[0])
    name = line[1]
    register_cnt +=1
    people.append((age,name,register_cnt))


people.sort(key= lambda x: (x[0],x[2]))

for tup in people :
    print (tup[0],tup[1])