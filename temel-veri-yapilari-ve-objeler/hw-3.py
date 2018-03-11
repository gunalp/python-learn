"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve
sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""

yakıt = float(input("Yakıt Bilgisi:"))
km = int(input("Kaç Km:"))

sonuc = yakıt*km

print("Ödenecek Tutar: {} tl".format(yakıt*km))
