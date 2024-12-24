from random import randint
class Note:
    def __init__(self, matiere):
        self.matiere=matiere
        self.note=randint(0,20)

    def __str__(self):
        return f"Matière:{self.matiere} \t Note:{self.note}"
    
somme = 0
for i in range(200):
    n=Note("Matiere " + str(i))
    print(n)
    somme += n.note
moyenne = somme / 200
print("Moyenne = ", moyenne)