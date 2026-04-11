import math

S, P = map(int, input().split())

D = S*S - 4*P

if D < 0:
    print(-1)
else:
    sqrtD = int(math.isqrt(D))
    if sqrtD * sqrtD != D:
        print(-1)
    else:
        x = (S + sqrtD) // 2
        y = (S - sqrtD) // 2
        if x + y == S and x * y == P:
            print(x, y)
        else:
            print(-1)
