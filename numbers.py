# data types - ma'lumot turlari
# 1.String (matn) => "test" , 'test'
# 2. Number (son) 👇
# integer (butun son "5,-5,3,467")
# float(o'nli son "2.3,22.454") 
# 3.boolean (mantiqiy qiymat "true-rost false-yolg'on")
# pi = 3.14159
# radius = 10
# diametr = 2 * radius
# print("Aylana uzunligi ", pi * diametr, " ga teng.")

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) 
# print(a*b)
# print(a**b)
# print(2*(a+b))

# aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
# print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")
# aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik

# KONSTANTA - o'zgarmas qiymat
# PI = 3.14
# G = 9.81

# x = 7 
# y = 5
# z = -7
# x,y,z, = 7,5,-7
# print(x - z + y) #19

# TYPECASTING - Ma'lumot turlarini o'zgartirish
# type chacking - ma'lumot turlarini teshkirish
# username = "adminjon"
# # type() function
# print(type(username)) #'str'
# print(type("tester"))#'str'
# print(type(12))#'inte'
# print(type(12.34))#'float'

# ism = "Jobr"
# yosh = "36"
# massage = ism + " "  + yosh + " yoshda"
# print(massage)
# age = 36
# print(type(age))
# age = str(age)
# print(type(age))

# print(str(36.89))
# print(int(121.29))
# print(int(15.0))
# print(float(18))
# print(int('12.77'))

# input() va son bn ishlash
# yosh = input("iltimos,yoshingizni kiriting:")
# t_yil = 2025 - int(yosh)
# print(type(yosh))
# print(t_yil)

# # amaliyot
# son = int(input("istalgan sonni kirting:"))
# xabar1 = f"{son} ning kvadrati {son**2}ga teng"
# xabar2 = f"{son} ning kvadrati {son**3}ga teng"
# input(xabar1,xabar2)

# yosh = int(input("Yoshingiz nechida?"))
# t_yil = 2025-yosh
# print("Siz ", t_yil, " da tug'ilgansiz")

# a = float(input("Birinchi sonni kiriting: "))
# c = float(input("Ikkinchi sonni kiriting: "))
# print(f"{a}+{c}=", a+c)
# print(f"{a}-{c}=", a-c)
# print(f"{a}*{c}=", a*c)
# print(f"{a}/{c}=", a/c)
# Amaliyot
# uchburchakning 1 - tomonini kiriting
# uchburchakning 2 - tomonini kiriting
# uchburchakning 3 - tomonini kiriting
# a = float(input("Uchburchakning birinch tomonini kiriting: "))
# b = float(input("Uchburchakning ikkinchi tomonini kiriting: "))
# c = float(input("Uchburchakning uchinchi tomonini kiriting: "))
# p = (a + b + c) / 2
# yuza = (p * (p-a)*(p-b)*(p-c))**(1/2) 
# print (f"Uchburchak tomonlari {a},{b},{c}bo'lsa, uning yuzi {yuza} ")

#  1 - doiraning radiusi: 3
#  2 - doiraning radiusi: 4
#  3 - doiraning radiusi: 5
# f-si: s1 = math.pi * r1 **2
# natija: Radiusi 3 ga teng doiraning yuzi 12.85 ga teng
import math
r1 = 3
r2 = 4
r3 = 5
s1 = math.pi * r1 **2
s2 = math.pi * r2 **2
s3 = math.pi * r3 **2
print(f"birinchi doiraning radiusi {s1} ga teng")
print(f"ikkinchi doiraning radiusi {s2} ga teng")
print(f"uchinchi doiraning radiusi {s3} ga teng")
 

























































































































































