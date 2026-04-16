# # barcha 4 xonali sonlar
# for n in range(1000, 10000):
#     print(n, end = " ")


# barcha 4 xonali sonlar ichidan raqamalar yig'indisi juft bolgan sonlarni konsolga chiqarish
def sum_of_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)

    return sum
print(sum_of_digits(185))