# 22.03.2024


# def = Definition : Tanımlama
"""
def ortalamaHesaplama():
    vize = int(input("Vize: "))
    final = int(input("Final: "))
    ortalama = (vize * 0.4) + (final * 0.6)
    print(f"Ortalmanız: {ortalama}")

def ortalamaHesaplama2():
    vize = int(input("Vize: "))
    final = int(input("Final: "))
    ortalama = (vize * 0.4) + (final * 0.6)
    return f"Ortalmanız: {ortalama}" # Çağırıldığı yere değer götürür o yüzden fonk. çağırdığımızda print içinde çağırmak gerekli

ortalamaHesaplama()
print(ortalamaHesaplama2())
"""

vizeInput = int(input("Vize: "))
finalInput = int(input("Final: "))

def ortalamaHesaplama(vize:float,final:float) -> float: #(vize,final) şeklinde de yazılabilir, dışarıda yaptığımız kod okunabilirliğini arttırmak için
    ortalama = (vizeInput * 0.4) + (finalInput * 0.6)
    print(f"Ortalmanız: {ortalama}")
    #return f"Ortalmanız: {ortalama}"

ortalamaHesaplama(vizeInput,finalInput)
#print(ortalamaHesaplama(vizeInput,finalInput))