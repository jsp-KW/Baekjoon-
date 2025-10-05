import sys
sys.setrecursionlimit(100000)


def find(x):
    if parent[x] !=x :
        parent[x] = find(parent[x])
    return parent[x]

def union (a,b):
    a = find(a)
    b= find(b)
    if a!=b : # 부모가 다르면 넣기
        parent[b] = a



test = 0
answers= []
while True :
    n, m = map(int,sys.stdin.readline().split())


    if n ==0 and m ==0 : 
        break

    test +=1
    parent = [i for i in range (n+1)]

    for i in range (m) :
        student1, student2 = map(int, sys.stdin.readline().split())
        union(student1,student2)
    

    res = len(set(find(i) for i in range (1,n+1)))
    answers.append (f"Case {test}: {res}")

print ("\n".join(answers))

    