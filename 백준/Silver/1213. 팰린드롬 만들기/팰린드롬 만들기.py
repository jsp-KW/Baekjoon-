import sys
from collections import Counter

hansoo_name = sys.stdin.readline().strip()

# 펠린드롬 -> 앞뒤로 읽어도 똑같은 문자열
# 주어진 문자열 -> 만들수 있으면 출력, 없으면 안된다고 출력
# 주어진 문자열의 길이가 짝수인 경우 -> 홀수개인 문자 존재x
# 홀수인 경우 -> 홀수개 문자 1개만 존재

def can_make(string) :
    counter = Counter(string)
    
    odds_ch = []
    for ch,count in counter.items() :
        if count % 2!=0 :
            odds_ch.append(ch)
    length = len(string)

    if (length % 2==0 and len(odds_ch) !=0) or (length %2 !=0 and len(odds_ch) !=1):
        return "I'm Sorry Hansoo"
    
    mid_ch = odds_ch[0] if length %2 ==1 else ""
    result = ""
    left_string = []
    for ch in sorted(counter.keys()) :
        left_string.append(ch* (counter[ch]//2))
        
    left="".join(left_string)
    result = left+mid_ch+left[::-1]

    return result

print(can_make(hansoo_name))