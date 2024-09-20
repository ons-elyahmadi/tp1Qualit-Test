

from Mathematique import  Somme,Maximum,Moyenne,puissance

def operation(x, y, op):
    if op == 'Somme':
        return Somme(x, y)
    elif op == 'Maximum':
        return Maximum(x, y)
    elif op == 'Moyenne':
        return Moyenne(x, y)
    elif op == 'puissance':
        return puissance(x, y)
    else:
        return "Opération non valide"

def affichage(resultat):
    print(resultat)
