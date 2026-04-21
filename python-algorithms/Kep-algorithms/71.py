def sum_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s += raqam

    return s

n = input()
n1 = (n[0:3])
n2 = (n[3:6])
s1 = sum_digits(n1)
s2 = sum_digits(n2)
if s1 == s2:
    print(True)
else:
    print(False)
