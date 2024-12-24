class Contact:
    def __init__(self, nom :str, tel : str):
        self.nom = nom
        self.telephone = tel
    def __str__(self):
        return f"{self.nom}\t {self.telephone}"

class Repertoire:
    def __init__(self):
        self.contacts = []
    def AjouterContact(self, c):
        self.contacts.append(c)
    def Rechercher(self, nom :str):
        for c in self.contacts:
            if c.nom.__contains__(nom):
                print(c)

c1=Contact("mohamed", "123456")
c2=Contact("ahmed", "456123")
rp=Repertoire()
rp.AjouterContact(c1)
rp.AjouterContact(c2)
rp.Rechercher("me")
