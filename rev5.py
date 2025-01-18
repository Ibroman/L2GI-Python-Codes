class Ecole:
    def __init__(self):
        self.notes = []
    def getTotalPoints(self):
        total_points=0
        for elt in self.notes:
            total_points += elt[0] * elt[1]
        return total_points
    def getTotalCoeff(self):
        total_coeff=0
        for elt in self.notes:
            total_coeff += elt[1]
        return total_coeff
    def getMoyenne(self):
        return self.getTotalPoints() / self.getTotalCoeff()
    def ajouterNote(self, note, coeff):
        self.notes.append((note, coeff))

    def __str__(self):
        for elt in self.notes:
            print(f"Note: {elt[0]}")
            print(f"Coefficient: {elt[1]}")
        msg = "Ecole ABCD\n"
        msg = f"Total des points: {self.getTotalPoints()}\n"
        msg += f"Total des coefficients: {self.getTotalCoeff()}\n"
        msg += f"Moyenne: {self.getMoyenne()}\n"
        return msg

e=Ecole()
e.ajouterNote(10,2)
e.ajouterNote(15,3)
print(e)