# Funksiya -  ma'lum bir vazifani bajaradigan kod blokidir.
# Ularni qayta ishlatish mumkin, bu kodni takrorlashdan qochishga yordam beradi va dastur tuzilishini yaxshilaydi.
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")

salom_ber() # Funksiyani chaqirish
salom_ber() #Funksiyani yana bir marta chaqirish

               #  Funksiyaga qiymat uzatish
# Parametrlar - funksiyaga qiymat uzatish un ishlatiladi
def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

salom_ber("Ali") 
salom_ber("Vali")

def yigindi(a,b):
    print(a + b)

yigindi(5,10) # 15 ni chiqaradi
yigindi(7,3) # 10
  

# def yosh_hisobla(ism = "olim",tugilgan_yil = "1987"):
#     yosh = 2026 - tugilgan_yil
#     print(f"{ism}ning yoshi: {yosh}")

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993)


# 1
def tugilgan_yilni_hisobla():
    name = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    joriy_yil = 2026
    tugilgan_yil = joriy_yil - yosh
    print(f"{ism},siz {tugilgan_yil} - yilda tugilgansiz.")
tugilgan_yilni_hisobla()

# 2
def kvadrat_kub(son):
    kvadrat = son ** 2
    kub = son ** 3
    print(f"{son}ning kvadrati: {kvadrat}")
    print(f"{son}ning kubi: {kub}")
son = int(input("sonni kiriting: "))
kvadrat_kub(son)

# 3
def juft_toq(son):
    if son % 2 == 0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")
son = int(input("son kiriting"))
juft_toq(son)