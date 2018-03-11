"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

sonuc = a*b*c

print("Birinci Sayı: {}\nİkinci Sayı: {}\nÜçüncü Sayı: {}\nSonuç: {}\n".format(a,b,c,sonuc))