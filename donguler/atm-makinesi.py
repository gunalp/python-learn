print("""
*****************************
Atm Makinesine Hoş Geldiniz

İşlemler ;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Çıkmak için 'q' basın

*****************************
""")

bakiye = 1000

while True:
    islem = input("İşlemi Seçiniz:")

    if(islem == "q"):
        print("Sistemden Çıkılıyor...")
        break
    elif(islem == "1"):
        print("Bakiyeniz: {} tl dir".format(bakiye))
    elif(islem == "2"):
        miktar  = int(input("Miktar Giriniz: "))
        bakiye += miktar
    elif(islem == "3"):
        miktar  = int(input("Miktar Giriniz: "))

        if(bakiye - miktar < 0):
            print("Eksik para çekemesin")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem...")