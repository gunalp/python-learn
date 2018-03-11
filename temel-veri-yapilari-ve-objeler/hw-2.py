"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

boy = float(input("boy:"))
kilo = int(input("kilo:"))

indeks = kilo/(boy**2)

print("Beden Kitle İndeksi: {}\n".format(indeks))
#print("Beden Kitle İndeksi:",kilo / (boy ** 2))