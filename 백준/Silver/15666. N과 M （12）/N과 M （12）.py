import sys


# N개의 길이, M개를 고른 수열
# 여러번 골라도됨, 비내림차순

N,M= map(int,sys.stdin.readline().split())
numbers  = list(set(map(int,sys.stdin.readline().split())))

numbers.sort()

idx = 0
answers =[]

def dfs (start, depth) :
    if depth == M :
        print(*answers)
        return
    
    for i in range (start, len(numbers)):
        answers.append (numbers[i])
        dfs (i, depth +1)
        answers.pop()

dfs (0,0)