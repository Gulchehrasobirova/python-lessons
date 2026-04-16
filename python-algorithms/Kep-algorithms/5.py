# n = int(input())
# s = 0
# for number in range(1, n + 1):
#     s += number 

# print(s)

import math
n = int(input())
s = 0
for number in range(1, n + 1):
    s += math.sqrt(number) 

print(s)


n = int(input())
1 + 2 + 3 + ... + (n + 1) + n
s = 0
for son in range(1, n + 1):
    s += son 
print(s)

# axample: n = 5
# sikl qadamlari:
# 1. son = 1; 0 + 1 = 1 = 5
# 2. son = 2; 1 + 2 = 3 = 5
# 3. son = 3; 3 + 3 = 6 = 5
#  Natija s = 15

import math
n = int(input())
s = 0
for son in range(1, n + 1):
    s += int(math.isqrt(son))
print(s)




