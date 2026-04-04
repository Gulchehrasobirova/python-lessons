# def add_numbers(a,b):
#     print(a + b)

# add_numbers(5, 10) # 15
# add_numbers(3,7) # 10
 
# def add_numbers(c, d):
#     return c + d

# add_numbers(8, 7) # 15
# result = add_numbers(4, 6)
# print(result) # 10

# berilgan son juft aks holda toq ekanligini tekdhirish uchun funksiya yozish:
def isEven(number):
    if number % 2 == 0:
        return "Juft son"
    else:
        return "Toq son"
print(isEven(4))
print(isEven(7))

text = "Python lessons"
print(len(text)) # 14
# string ichidagi har bir element indexlanadi (0 dan boshlanadi)
print(text[0]) # P
print(text[1]) # y
print(text[2]) # t
print(text[13]) # n 
print(text[-1]) # s
       # for sikl
# 1- usul
for belgi in text:
    print(belgi)
# 2- usul
for index in range(len(text)):
    print(index, text[index])

# Unli harflr (a, e, i, o) sonini hisoblash un funksiya yozing.
# example: "salom" -> 2 ta unli harf bor (a, o)
# python -> 1 ta unli harf bor (o)

vowels = "aeiou"
def count_vowels(word):
    count = 0
    for letter in vowels:
        count += 1
    
    return count
print(count_vowels("Salom"))






























































