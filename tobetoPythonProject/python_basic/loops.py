# 22.03.2024


"""
for i in range(10): # range(10) = i < 10 
    print(i)
"""

# Kullanıcının girdiği sayılar arasında en büyüğü bulalım 

"""
büyükSayi = None # None null demek negatif sayıları da dahil edebilmek için kullandık

for i in range(3):
    sayi = int(input(f"{i+1}. sayıyı girin: "))

    if büyükSayi is None or  sayi > büyükSayi:
        büyükSayi = sayi

print(f"Girdiğiniz en büyük sayı: {büyükSayi}")    
"""

'''
numbers = [] 
for i in range(3):
    numbers.append(int(input(f"{i+1}. sayıyı girin: ")))

print(numbers)
numbers.sort(reverse=True) #Defaul olarak küçükten büyüğe sıralar 
print(numbers)
print(max(numbers))

index = int(input("Sayılar arasında en büyük kaçıncı elemanı istiyorsun? "))
print(numbers[index-1])
'''
"""
students = ["Ahmet", "Hakan","Kabe","Ercan","Tuba"]

for i in range(len(students)) : 
    if i>2:
        break # İlgili döngünün o anda kırılmasını sağlar ve tekrar döngüye devam etmez
    print(f"{i+1}. Öğrenci: {students[i]}")

for student in students: #Foreach 
    if student == "Ercan":
        continue # Şarttaki değeri pas geçip döngüye devam eder
    print(f"Merhaba {student}")
"""

'''
i = 0
while i < 10:
    print(i)
    i += 1
'''

