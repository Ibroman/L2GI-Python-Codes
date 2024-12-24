class Evaluation:
    def __init__(self, n:list):
        self.nombres=n
        self.moyenne=sum(n)/len(n)

    def moyenne(self):
        return self.moyenne
    
    def maximun(self):
        return max(self.nombres)

    def minimun(self):
        return min(self.nombres)
    
    def getEvaluation(self):
        if self.moyenne<10:
            print("Echec")
        elif self.moyenne<12:
            print("Passable")
        elif self.moyenne<15:
            print("Bien")
        else:
            print("Très bien")

nombres=(13,5.65,12.56,20,17.5)
e1=Evaluation(nombres)
print(e1.moyenne)
e1.getEvaluation()
print(e1.maximun())
print(e1.minimun())