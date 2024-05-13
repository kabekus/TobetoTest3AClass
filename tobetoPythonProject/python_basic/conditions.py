#20.03.2024


note = int(input("Lütfen ortalamanızı girin: ")) #Kullanıcıdan alınan veri string türünde olduğu iin tip dönüşümü yaptık.

if note > 80 :
    message = "Bravooo"
elif note > 50:
    message = "Güzel not" 
    if note > 40:
        message = "40 ile 50 arasımı :O"
else:
    message = "Dersten Kaldın"    

print(message)

