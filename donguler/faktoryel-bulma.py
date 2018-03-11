print("""
*****************************
Faktoriyel Bulma Programı Hoş Geldiniz

Çıkmak için 'q' basın

*****************************
""")

while True:
    sayi = input("Sayı: ")

    if(sayi == "q"):
        print("Sistemden Çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1

        for i in range(2,sayi+1):
            print("Faktroiyel: ", faktoriyel,"i: ",i)
            faktoriyel *= i

        print("Faktroiyel: ",faktoriyel)