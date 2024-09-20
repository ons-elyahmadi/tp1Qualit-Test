from Calcularice import operation, affichage

x = float(input("Entrez le premier nombre : "))
y = float(input("Entrez le deuxième nombre : "))
op = input("Choisissez une opération (Somme, Maximum, Moyenne, puissance) : ")

resultat = operation(x, y, op)
affichage(resultat)