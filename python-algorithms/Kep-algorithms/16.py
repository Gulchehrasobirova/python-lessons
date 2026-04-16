import math

# Kiruvchi ma'lumotni o'qiymiz
n = int(input())

# Faktorialni hisoblaymiz va chiqaramiz
print(math.factorial(n))


n = int(input())
s = 1
for son in range(1, n + 1):
    s *= son
    print(s)