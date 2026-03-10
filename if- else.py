# Tarmoqlanish operatori.if- agar, else - aks holda
# age = int(input("yoshingizni kiriting: "))
# if age < 18:
#     print("siz hali yoshsiz, kirish mumkin emas")
# else:
#     print("sizga kirishga ruhsat bor")  

# ball = int(input("imtihondan olgan ballingizni kiriting: "))
# if ball < 56:
#     print("siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70:
#     print("3 baho oldingiz")
# elif ball >= 70 and ball < 86:
#     print("4 baho oldingiz")
# elif ball >= 86 and ball < 100:
#     print("5 baho oldingiz")
# else:
#     print("siz 0 dan 100 gacha ball kiriting")

# yosh = int(input("yoshingizni kiriting: "))
# if yosh < 16:
#      print("siz hali yoshsiz, pasport mumkin emas")
# else:
#     print("sizga pasportga ruhsat bor") 

#                2026
#N1
# son = int(input("xohlagam sonni kiriting: "))
# if son > 0:
#     print("musbat son")
# else:
#     print("manfiy son")
#N2
# son = int(input("xohlagam sonni kiriting: "))
# if son % 2 == 0:
#     print("juft son")
# else:
#      print("toq son")  
#N3
# son = int(input("xohlagam sonni kiriting: "))
# if son % 5 == 0:
#      print("5 ga bolinadi")
# else:
#      print("5 ga bolinmaydi")  
#N4
# son = int(input("xohlagam sonni kiriting: "))
# if son % 2 == 0 and son % 3 == 0:
#     print("6 ga bolinadi")
# else:
#     print("6 ga bolinmaydi")
#N5
# if a + b > c and b + c > a and a + c > b:
#     print("uchburchak yasab boladi")
# else:
#     print("uchburchak yasab bolmaydi")
#N6
# a= int(input("1-sonni kiriting: "))
# b= int(input("2-sonni kiriting: "))
# if  a > b:
#     print("a")
# else:
#     print("a,b")
#N7
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# if a <= b:
#     a=0
#     print("a,b")
# else:
#     print("a,b")

#N8
# import math
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# if a >= b >= c :
#     print( 2 * a, 2 * b, 2 * c)
# else:
#     print(int(math.fabs(a))(a),int(math.fabs(a))(b),int(math.fabs(a))(c) )

#N9
# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# a = x = 2 * x * y
# b = y = (x + y) / 2 
# if x > y:
#    x = a
#    y = b
# else:
#     y = a
#     x = b
    # print(x,y)

#N10
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# if a < b < c:
#     print("Yes")
# else:
#     print("No")
# print(max(15,-5,0,104,189,89.77))
# print(min(15,-5,0,104,189,89.77))
# #N11
# a = float(input("x sonni kiriting: "))
# b = float(input("y sonni kiriting: "))
# print(max(a,b),min(a,b))

#N12
# x = float(input("x sonni kiriting: "))
# y = float(input("y sonni kiriting: "))
# z = float(input("z sonni kiriting: "))
# print(max(a,b,z),min(a,b,z))

# x = float(input("x sonni kiriting: "))
# y = float(input("y sonni kiriting: "))
# z = float(input("z sonni kiriting: "))
# A = max(x + y + z, x,y,z)
# B = min(x + y / 2 , x, y, z,) ** 2
# print(f"{A:2f} {B:2f}")


#1
# x = float(input("x sonni kiriting: "))
# y = float(input("y sonni kiriting: "))
# if x < 0 and y < 0:
#     print()
# elif x < 0 or y < 0:
#     x = x + 0.5
#     y = y + 0.5
#     print(x ,y)
# else: x > 0 and y > 0.5
# print(x,y)


# import math
# a = int(input("1-: "))
# b = int(input("2-: "))
# x = int(input("3-: "))
# D = b ** 2 - 4 * a * x
# if D > 0:
#     x1 = (-b + math.sqrt(D)) / 2 * a
#     x2 = (- b - math.sqrt(D)) / 2 * a
#     print("%.2f" % x1, "%.2f" %x2 )
# elif D == 0:
#     x = - b / (2 * a)
#     print("%.2f" % x)
# else:
#     print("No")


#N40
# x = int(input("1-sonni kiriting: "))
# y = int(input("2-sonni kiriting: "))
# z = int(input("3-sonni kiriting: "))
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2
# print(x,y,z)


#N38
# x = float(input("x sonni kiriting: "))
# y = float(input("y sonni kiriting: "))
# z = float(input("z sonni kiriting: "))
# if 1 <= x <= 3:
#     print(x)
# if 1 <= y <= 3:
#     print(y)
# if 1 <= z <= 3:
#     print(z)


#N42 
# a = float(input("1 sonni kiriting: "))
# b = float(input("2 sonni kiriting: "))
# c = float(input("3 sonni kiriting: "))
# d = float(input("4 sonni kiriting: "))
# if a <= b <= c <= d:
#    print(max(a,b,c,d))
# else:
#     print(min(a,b,c,d))

# Uy ishi
# a = float(input("1 sonni kiriting: "))
# b = float(input("2 sonni kiriting: "))
# c = (a + b) / 2
# d = 2 * (a * b)
# if a < b:
#     a = c 
#     b = d
# elif a > b:
#     a = c
#     b = d
# print(a,b)

#N.41
# x = float(input("1 sonni kiriting: "))
# y = float(input("2 sonni kiriting: "))
# z = float(input("3 sonni kiriting: "))
# min_value = min( x,y,z)
# if x < 1 and y < 1 and z < 1:
#     if min_value == x:
#         x = (y + z) / 2
#     elif min_value == y:
#         y = ( x+ y) / 2
#     else:
#         z = ( x + z) / 2
# else:
#          x = x
#          y = y
#          z = z
# print(x,y,z)






































