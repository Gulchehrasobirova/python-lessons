# Dictionary elementlari bilan ishlash
phone = {
    'brand': 'Apple',
    'model':"Iphone 17 pro max",
    'color':'silver',
    'storage':'256GB',
    'price':'$1500'
}
# get() motodi - kalit orqali qiymatni olish
print(phone.get("model")) # Iphone 17 pro max
print(phone.get("price","narx topilmadi")) #$1500

# items() metodi -  lug'at elementlarini ( kalit-qiymat) juftliklari sifatida olish
print(phone.items())
for key, value in phone.items():
    print(f"kalit: {key}")
    print(f"qiymat: {value}")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")


# keys() metodi - lug'atning barcha kalitlarini olish
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# Lug'at elementlarini tartib bn chiqarish
print(mahsulotlar) 
print(sorted(mahsulotlar))

print("Do'koningizdagi mahsulotlar")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)































































