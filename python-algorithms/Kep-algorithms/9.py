# STRINGNI kesib olish va teskaerisiga ogirish
# txt = ' abcd'
# print(txt[1 : 3]) # bc
# print(txt[0 : len(txt)]) # abcd
# print(txt[0 ::]) # abcd
# print(txt[:: -1]) # dcba
# print(txt[:: 2]) # ac   
def reverse_number(number):
  strinf_number = str(number)
  return int (strinf_number[:: -1])
# print(reverse_number(12345))
for num in range(1000, 10000):
   reverse_num = reverse_number(num)
   if reverse_num == 4 * num:
        print(num)
