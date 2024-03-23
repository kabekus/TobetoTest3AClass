""" 
Daire Alanı   : πr² 
Daire Çevresi : 2πr
 * Yarı çapı kullanıcıdan alınan dairenin Alanı ve Çevresi nedir ? (π = 3.14)
"""
pi = 3.14
r = float(input("Yarı çap girin: "))

alan = pi*(r*r)
cevre = 2*pi*r
print(f"Alan: {alan} \nÇevre: {cevre}")