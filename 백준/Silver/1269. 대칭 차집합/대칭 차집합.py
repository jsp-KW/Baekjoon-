import sys

N,M = map(int,sys.stdin.readline().split())
A= list(map(int, sys.stdin.readline().split()))
B= list(map(int, sys.stdin.readline().split()))

A_set , B_set = set(A), set(B) # set을 씀으로써 내부 탐색 조회 시간복잡도 O(1)
# hash table 기반이라

print(len(A_set -B_set) + len( B_set-A_set))