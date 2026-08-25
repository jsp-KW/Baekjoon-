def solution(a, b, c, d):
    answer = 0

    
    # 4개 동일
    if a == b == c == d:
        return 1111 * a

    # 3개 동일
    elif a == b == c:
        return (10*a + d) ** 2

    elif a == c == d:
        return (10*a + b) ** 2

    elif a == b == d:
        return (10*a + c) ** 2

    elif b == c == d:
        return (10*b + a) ** 2


    # 2개 + 2개
    elif a == b and c == d:
        return (a+c) * abs(a-c)

    elif a == c and b == d:
        return (a+b) * abs(a-b)

    elif a == d and b == c:
        return (a+b) * abs(a-b)


    # 딱 한 쌍
    elif a == b:
        return c * d

    elif a == c:
        return b * d

    elif a == d:
        return b * c

    elif b == c:
        return a * d

    elif b == d:
        return a * c

    elif c == d:
        return a * b


    # 전부 다름
    else:
        return min(a, b, c, d)
