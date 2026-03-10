# # Loop - sikl
# # 1.for loop  #2.while loop
# students = ["Farida","Charos","Kumush","Ozod"]
# # print(students(0))
# # print(students(1))
# # print(students(2))
# # print(students(3))
# # for student in students:
# #    print(f"Hurmatli {student}, sizni interyuga taklif qilamiz")
# #    print("hurmat bilan,Gulchehra")

# # nums = list(range(1,11))
# # for numbers in nums:
# #    # print(numbers)
# #  print(f"{numbers} sonining kvatati {numbers ** 2} ga teng")

# # sonlar = list(range(20))
# # #  start_default_value = 0
# # print(sonlar) # [0,1,...,18,19]
# # # [0,1,4,9,16...,324,361]
# # sonlar2 = []
# # for son in sonlar:
# #  sonlar2.append(son ** 2)

# # print(sonlar2)

# # 2 - USUL
# # for index in range(len(sonlar)):
# #     print(index) #element indexi
# #     print(sonlar[index]) # element

# #  1-marta => index = 0 => sonlar[0] = 0


# # kinolar = []
# # for n in  range(5):
# #   kinolar.append(input (f"{n+1} - kinoni kiriting:  "))
# # print(kinolar)    

# # people = int(input("necha inson bilan ko'rishdingiz?: "))
# # people = []
# # for in range(people):
# #   people = input(f"{n+1} - ko'rishgan insonlaringiz kimlar edi?:  ")
# # people.append(people)


# # telefon = int(input("sizga nechta telefon modeli yoqadi: "))
# # telefon = []
# # for n in range(3):
# #   telefon.append(input(f"{n+1} telefon modeli: "))
# # print(telefon)


# numbers = [23,76,43,22,73,89,69,7]
# # min_value = min(numbers)
# # print(min_value)

# # for number in numbers:
# #   print(number / min_value) 

# # s = 0
# # for number in numbers:
# #     s = number
# # print(s)

# # #     1 dan 50 gacha bo'lgan juft sonlar ro'yxati
# # s = 0
# # for son in range(2,50,2):
# #  s += son
# #  print(s)

# # # n! = 1 * 2 * 3 * ... (n - 1) * n
# # kopaytma = 1
# # for son in range(1,11):
# #    kopaytma *= son #kopaytma = kopaytma * son
# # print(kopaytma)
 
# # #   1 dan 20 gacha top sonlar kopaytmasini yig'indisiga nisbati?
# # kopaytma = 1
# # s = 0
# # for son in range(1,20,2):
# #    kopaytma *= son
# #    s += son
# # print(kopaytma / s)

# # nums = [24,60,54,34,95]
# # s = 0
# # for num in nums:
# #    s += son ** 2
# #    print(son + s)

# # # o'rtacha qiymat = s / length
# # s = 0
# # for son in nums:
# #    s += son
# # length = len(nums)
# # k = s / length
# # print(k)

# # nums = [12,-5,15,89,-75,0,-18]
# # # musbar elementlar yigindisi 
# # # manfiy elementlar ko'paytmasi
# # s = 0
# # k = 1
# # for son in nums:
# #     if son > 0:
# #         s += son
# # else:
# #     k *= son
# #     print(s)
# #     print(k)

# # Uy ishi
# # kopaytma = 1
# # s = 0   
# # for n in range(2,20,2):
# #     kopaytma *= n
# # for n in range(1,20,2):
# #     s += n
# # print(kopaytma / s)

# # nums = [12,-5,15,89,-75,0,18]
# # # o'rta arifmetik = s / length
# # s = 0
# # for son in nums:
# #     s += son

# # length = len(nums)
# # average_value = s / length
# # print(average_value)

# # import math
# # kopaytma = 1
# # nums = [12,-5,15,89,-75,18]
# # for n in nums:
# #     kopaytma *= n

# # orta_geometrik = math.pow(kopaytma,1/len(nums))
# # print(orta_geometrik)

# # numbers  = [7,97,-58,90]
# # s = 0
# # counter = 0
# # for son in numbers:
# #     if son % 2 == 0:
# #      s += son
# #      counter += 1
# # # print(s)
# # # print(counter)


# # # sonlar= [97,97,-92,14,22]
# # # s = 0
# # # for  son in sonlar:
# # #     if son % 2 == 0 or son % 3 == 0 or son % 5 == 0:
# # #         son == son
# # # print(s)

# # # import math
# # # sonlar = [ 44,34,42,83,43,64]
# # # s = 0
# # # for n in sonlar:
# # #     if  n % 2 == 0 or n % 5 == 0:
# # #         s *= n
# # # print(math.sin(n)) 

# # nums = (93,64,-90,74,62,-83,58,15,-37)
# # s = 0
# # c = 0
# # for n in nums:
# #     if n < 0:
# #         s += n
# #         c += 1
# #         print(s / c)

# # m = int(input("M sonni kiriting: "))
# # numbers = (12,88,30,87)
# # s = 0
# # for n in numbers:
# #     if n > m:
# #         s += n
# # print(s)

# # M = int(input("M sonni kiriting: "))
# # nums = [85,15,57,68,18,67,7,45,69,21,1,5,98,34]
# # s = 0
# # for son in nums:
# #     if M > n :
# #         s += n ** 2
# # print(s)
# # import math
# # k = 0
# # s = 0
# # number = [44,59,-75,73 ]
# # for n in number:
# #     k += n ** 2
# #     s  += n
# # length = len(number)
# # c = s / length
# # print(c)
# # print(k)
# #            UY ishi
# # l = [74, 0, 1, 33]

# # m = min(l)
# # k = l.index(m)

# # l[k], l[-1] = l[-1], l[k]

# # print(*l)
# # nums = [7, 11, 83, 18, 31]

# # K = int(input("K ni kiriting: "))
# # M = int(input("M ni kiriting: "))

# # k = 1
# # for son in nums:
# #     if son == K or son == M:
# #         k *= son

# # print(k)

# # # 127
# # numbers =[46, 23, -52, 34, 6, -18, 52]
# # plan
# # 1. eng kichik element = min
# # 2. manfiy elementlarni topish
# # 3. manfiy elementlarni min ** 2 ga almashtirish => numbers [2] = 23
# # min_value = min(numbers)
# # for index in range(len(numbers)):
# #    element = numbers[index]
# #    if element[index] < 0:
# #      numbers[index] = min_value ** 2

# # print(numbers)
# # 104
# # 1- min elementni topish
# # 2- oxirgi elementni topish
# # 3 - joyini almashtirish
# # sonlar = [74, 0, 1, 33]
# # minimum_value = min(sonlar)
# # last_element = sonlar[-1]
# # min_index = sonlar.index(minimum_value)
# # sonlar[min_index] = last_element
# # sonlar[-1] = minimum_value
# # print(sonlar)
# # 124
# k = int(input("k sonini kiriting"))
# nums = [29, 50, -14, 4, 27, -56]
# maximum_value = max(nums)
# index = k - 1
# nums(max.index) = maximum_value
# print(nums)

a = 5; b = 3
# natija: a = 3; b = 5
#  1 - usul
# temporary variable - vaqtinchalik o'zgaruvchi
c = a # 5
a = b # 3
b = c # 5
print(a,b)

#  2 - usul
a, b = b , a
print(a, b)

#   3 - usul 










































