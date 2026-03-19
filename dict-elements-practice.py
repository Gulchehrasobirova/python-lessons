# Amaliyot
# 1.
python_dict = {
    'boolean':'Mantiqiy qiymat',
    'float':'onlik sonlar',
    'for':'biror amalni qayta-qayta bajarish tsikli',
    'if':'shartlarni teshkirish operatori',
    'integer':'butun son',
    'else':'aks holda operatori',
    'dict':'lug\'at'
}

print("Pyton izohli lug'ati (alifbo tartibida):\n")
for key,value in sorted (python_dict.items()):
    print(f"{key.title()} - {value.title()}")
# 2.
davlatlar_poytaxtlar = {
    'AQSH':'Washington.D.C',
    'Italiya':'Rim',
    'Malayziya':'Kuala',
    "O'zbekiston":'Toshkent',
}
print("Dunyo davlatlari: ")
for poytaxt in sorted(davlatlar_poytaxtlar.values()):
    print(poytaxt)
davlat = input("Davlat nomini kiriting: ").lower()
if davlatlar_poytaxtlar.git(davlat) == None:
    print("kechirasiz bizda bu haqida malumot yoq")
else:

print(f"{davlat.title()}ning poytaxti {davlatlar_poytaxtlar{davlat}.title()} shahri")






