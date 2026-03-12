# data types (ma'lumot turlari)
# string,int,float,list,bool,dictionary

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":"yellow",
    "price":"$45000"
}
print(car)
print(type(car))

user = {
    "full name":"Sobirova Gulchehra",
    "email":"sobirovagulchehra@gmail.com",
    "age": 15,
    "is_student":False,
    "favorite_books":["Ikki eshik orasi","Yashamoq","Dunyoning ishlari"]
    }
# 1. valuelarni olish (key orqali)
print(user['age'])
print(user['favorite_books'])

for book in user['favorite_books']:
    print(book)

# 2. yangi key-value qo'shish
user['is_mmarried'] = False
user['hobbies'] = ['reading a book','music a film']
print(user)

# 3.Valuelarni o'zgartirish
user['email']
user['favorite_books'] = "Qulog'im senda qizim"
print(user)

# Bo'sh lug'at(Empy dictionary)
talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print("talaba_1")
print(f"talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")


# 5. Key - value juftligini o'chirish
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(talaba_0)
del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
print(talaba_0)

































































