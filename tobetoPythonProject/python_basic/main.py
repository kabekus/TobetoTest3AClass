#20.03.2024


print("Merhaba Test 3A")
text = "Merhaba python"
print (type(text))


studentCount = 45 
print(5 + studentCount)

print(studentCount == 40) #False
print(studentCount == 45) #True
print(studentCount != 78) #True

# String Interpolation => Metin birleştirme denebilir 

text1 = "Merhaba"
text2 = "Kabe"
totalText = text1 + text2
print(totalText) 

totalText ="{message} Sayın {name}".format(message="Selamlar" ,name=text2)
print(totalText) 

totalText = f"Hoşgeldiniz {text2}"
print(totalText) 