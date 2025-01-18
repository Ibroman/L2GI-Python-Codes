class Personne:
    def __init__(self, nom, lieun, age):
        self.nom = nom
        self.lieunaissance = lieun
        self.age = age
    def __str__(self):
        return f"{self.nom} agé de {self.age} ans est né(e) à {self.lieunaissance} et est un {self.grade()}"
    def grade(self):
        if self.age<10:
            return "cadet"
        elif self.age<20:
            return "junior"
        else:
            return "adulte"
        
p1=Personne("Ali", "Djibouti", 30)
print(p1)