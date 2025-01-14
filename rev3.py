print("Ecole ABCD")
nombre = int(input("Combien de matieres ?"))
total_points=0
total_coeff=0
for i in range(nombre):
    note = float(input("Note:"))
    coefficient = int(input("Coefficient:"))
    total_points+=note*coefficient
    total_coeff+=coefficient
print(f"Total des points {total_points}")
print(f"Total des coefficient {total_coeff}")
print(f"Moyenne = {total_points/total_coeff}")