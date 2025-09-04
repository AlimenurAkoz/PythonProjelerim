import json
import os

if os.path.exists("rehber.json"):
    with open("rehber.json","r",encoding="utf-8") as file:
        rehber = json.load(file)
else:
    rehber = {}

def kaydet():
    with open("rehber.json", "w", encoding="utf-8") as f:
        json.dump(rehber, f, ensure_ascii=False, indent=4)

def listele():
    if rehber:
        for isim, numara in rehber.items():
            print(f"{isim}: {numara}")
    else:
        print("Rehber boş")

rehber = {isim.lower(): numara for isim, numara in rehber.items()}

def ara():
    ara = input("Ara:..").lower()
    bulundu = False
    for isim,numara in rehber.items():
        if isim.lower().startswith(ara) or numara.startswith(ara):
            print(f"İsim: {isim}, Numara: {numara}")
            bulundu = True
    if not bulundu:
        print("Kişi bulunamadı.")

def ekle():
    isim = input("İsim: ")
    numara = input("Numara: ")
    rehber[isim] = numara
    kaydet()
    print("Kaydedildi.")

def sil():
    isim = input("Silinecek isim: ")
    if isim in rehber:
        rehber.pop(isim)
        kaydet()
        print("Kayıt silindi.")
    else:
        print("Kişi bulunamadı.")

def duzenle():
    isim = input("Düzenlenecek isim:..")
    if isim in rehber:
        sec = input("Düzenlenecek bilgi: isim/i ya da numara/n")
        if sec == "i":
            yeni_isim = input("Yeni isim:..")
            rehber[yeni_isim] = rehber.pop(isim)
            kaydet()
            print("İsim güncellendi")
        elif sec == "n":
            yeni_numara = input("yeni numara:..")
            rehber[isim] = yeni_numara
            kaydet()
            print("Numara güncellendi")
        else:
            print("Geçersiz giriş")
    else:
        print("Kişi bulunamadı")
while True:
    print("\n------MENÜ------")
    print("1- Rehberi Görüntüle")
    print("2- Kişi Ara")
    print("3- Kişi Ekle")
    print("4- Kişi Sil")
    print("5- Kişiyi Düzenle")
    print("6- Çıkış")

    secim = input("Seçiminiz:..")
    if secim == "1":
        listele()
    elif secim == "2":
        ara()
    elif secim == "3":
        ekle()
    elif secim == "4":
        sil()
    elif secim == "5":
        duzenle()
    elif secim == "6":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim!")


