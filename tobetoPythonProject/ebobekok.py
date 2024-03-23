""" 
def ebob_ekok_hesapla(birinciSayi, ikinciSayi):
    # EBOB hesaplama
    if birinciSayi > ikinciSayi:
        kucuksayi = ikinciSayi
    else:
        kucuksayi = birinciSayi
    for i in range(1, kucuksayi + 1):
        if (birinciSayi % i == 0) and (ikinciSayi % i == 0):
            ebob = i
            
    # EKOK hesaplama
    ekok = (birinciSayi * ikinciSayi) // ebob
    return ebob, ekok

birinciSayi = int(input("Birinci Sayıyı Giriniz: "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz: "))
 
ebob, ekok = ebob_ekok_hesapla(birinciSayi, ikinciSayi)
print("EBOB:", ebob)
print("EKOK:", ekok)
"""


sayi1 = int(input("Birinci Sayıyı Giriniz: "))
sayi2 = int(input("İkinci Sayıyı Giriniz: "))

def ebob(sayi1,sayi2):
    kucukSayi = min(sayi1,sayi2)
    ortakBolenler = []
    for i in range(1,kucukSayi+1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ortakBolenler.append(i)
    ortakBolenler.sort(reverse=True)
    return ortakBolenler[0]


def ekok(sayi1,sayi2):
    carpim = sayi1 * sayi2
    sayi1_katlari = set()
    sayi2_katlari = set() # set() ile küme oluşturulur

    for i in range(1,carpim):
        if sayi1*i != carpim:
            sayi1_katlari.add(sayi1*i)
        else:
            break    # Çarpımı geçtiyse döngüden çık

    for x in range(1,carpim):
        if sayi2*x != carpim:
            sayi2_katlari.add(sayi2*x)
        else:
            break    
    kesisim = sayi1_katlari.intersection(sayi2_katlari) # iki kümenin kesişim kümesi oluşturuldu
    kesisimListe = list(kesisim) # Kümeyi listeye / diziye dönüştürdük 
    kesisimListe.sort()
    if not kesisimListe:  # kesisimListe iki sayının ortak katı olmadığında boş gelebilir bunun için kontrol
        print("girilen sayılar burada işlemde")
        ebobSonuc = ebob(sayi1,sayi2)
        ekokIslem = (sayi1*sayi2)/ebobSonuc
        return ekokIslem
    else:
        print("girilen sayıların ortak katı var burada işlemde")
        return kesisimListe[0]

print(f"EBOB: {ebob(sayi1,sayi2)}")
print(f"EKOK : {ekok(sayi1,sayi2)}")  
