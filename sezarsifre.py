harfler = "abcdefghijklmnopqrstuvwxyz"

yazi = input("Metni gir: ")
adim = int(input("Kaydırma miktarı: "))

cikti = ""

for i in range(len(yazi)):
    if yazi[i] in harfler:
        yeni_index = (harfler.find(yazi[i]) + adim) % len(harfler)
        cikti += harfler[yeni_index]
    else:
        cikti += yazi[i]

print("Sonuç:", cikti) bu kodu anlat detaylı
