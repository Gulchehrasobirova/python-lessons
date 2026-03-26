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
