#20.03.2024


sayilar = [30,675,200,"bu bir sayı değil"]
print(sayilar)
print(sayilar[1]) # Burada 30 değil 675 gösterir çünkü ilk elemanın index değeri 0'dır.

sayilar.append(30) # Dizinin sonuna yeni eleman eklemeye yarar.
print(sayilar)

sayilar.remove(30) # soldan başlar ilk gördüğü 30 değerini siler.
print(sayilar)

sayilar.pop(2) # index numarasına göre siler ama hiç index verilmemişse en son olan veriyi siler.
print(sayilar)

sayilar.extend([100,200,300]) # Diziye birden fazla eleman eklemeye yarar.
print(sayilar)

sayilar.clear() # Tüm diziyi silmeye yarar.
print(sayilar)