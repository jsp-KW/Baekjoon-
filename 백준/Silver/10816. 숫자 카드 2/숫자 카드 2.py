import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
card_cnt = Counter(cards)


M = int(sys.stdin.readline())
checks =list(map(int, sys.stdin.readline().split()))



answer = [card_cnt[c] for c in checks]

# for c in checks :
#     cnt =0
#     for card  in cards :
#         if c == card :
#             cnt +=1

#     answer.append(cnt)   

print(' '.join(map(str, answer)))