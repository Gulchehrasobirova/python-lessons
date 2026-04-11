N = input()
print(type(N))
even_sum = 0
odd_sum = 0
for i in range(len(N)):
    digit = int(N[index])
    if (index + 1) % 2 == 0:
        odd_sum += digit
    else:
        even_sum += digit

diff = abs(even_sum - odd_sum)
if diff == 0 or diff % 11 == 0:
    print("Yes")
else:
    print("No")
print(even_sum, odd_sum)
print(diff)