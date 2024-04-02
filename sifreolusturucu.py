import random
import string

def ismi_bol(isim):
    # İsmi ortadan ikiye bölen fonksiyon
    uzunluk = len(isim)
    orta_nokta = uzunluk // 2
    ilk_kisim = isim[:orta_nokta]  # İsimdeki ilk yarı
    ikinci_kisim = isim[orta_nokta:]  # İsimdeki ikinci yarı
    return ilk_kisim, ikinci_kisim

def guclu_sifre_mi(sifre):
    # Şifrenin gücünü değerlendiren fonksiyon
    return any(c.islower() for c in sifre) and any(c.isupper() for c in sifre) and any(c.isdigit() for c in sifre)

def sifre_olustur(uzunluk, isim, karakter_seti):
    # Şifre oluşturan fonksiyon
    if uzunluk < 8:
        print("Şifreniz en az 8 karakterden oluşmalıdır.")
        return None

    # Kullanılacak karakter setini belirleme
    if karakter_seti == 1:
        # Sadece harf ve rakamları içeren karakter seti
        karakterler = string.ascii_letters + string.digits
    elif karakter_seti == 2:
        # Harf, rakam ve özel karakterleri içeren karakter seti
        karakterler = string.ascii_letters + string.digits + string.punctuation.replace(" ", "")
    else:
        # Geçersiz karakter seti seçimi durumu
        print("Geçersiz karakter seti seçimi.")
        return None

    # İsmi ortadan ikiye böl
    ilk_kisim, ikinci_kisim = ismi_bol(isim)

    # Rastgele sıralanmış şifre bölgeleri oluşturma
    sifre_bolge1 = ''.join(random.sample(ilk_kisim, len(ilk_kisim)))
    sifre_bolge2 = ''.join(random.sample(ikinci_kisim, len(ikinci_kisim)))

    # Şifreyi oluşturma
    sifre = sifre_bolge1 + ''.join(random.choice(karakterler) for i in range(uzunluk - len(ilk_kisim) - len(ikinci_kisim))) + sifre_bolge2

    # Şifrenin gücünü kontrol etme
    if not guclu_sifre_mi(sifre):
        print("Şifre güçlü değildir. Daha güçlü bir şifre kullanmanız önerilir.")
        return None

    return sifre

while True:
    try:
        # Kullanıcıdan şifre uzunluğu, isim ve karakter seti seçimi alma
        uzunluk = int(input("Oluşturmak istediğiniz şifrenin uzunluğunu girin (en az 8 karakter): "))
        isim = input("İsminizi girin: ")
        karakter_seti = int(input("Kullanmak istediğiniz karakter setini seçin:\n1. Sadece harf ve rakamlar\n2. Harf, rakam ve özel karakterler\nSeçiminiz: "))

        # Şifreyi oluşturma fonksiyonunu çağırma
        sifre = sifre_olustur(uzunluk, isim, karakter_seti)
        if sifre:
            # Şifre oluşturulduğunda kullanıcıya gösterme
            print("Oluşturulan şifre:", sifre)
            break  # Döngüden çıkma ve programın sonlanması
    except ValueError:
        # Geçersiz giriş durumu
        print("Geçersiz giriş. Lütfen doğru değerleri girin.")
