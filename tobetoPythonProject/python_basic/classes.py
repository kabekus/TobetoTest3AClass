# 27.03.2024

class Student:

    def __init__(self,name,age):
        self.name = name # burada varsayılan değer ne olursa olsun 
        self.age = age   # bu değişkenlerin değeri dışarıdan gelen değişkenlere eşittir
        print("Yapıcı blok çalıştı ")

    def study(self): # Class içinde method oluşturuyorsak self parametresi olması gerekir 
        print(f"{self.name} is Studying ")