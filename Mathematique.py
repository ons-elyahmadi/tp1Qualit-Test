def Somme(x,y):
    return x+y
def Maximum(x,y):
   if x>y:
       return x
   else:
       return y
def Moyenne(x,y):
    return (x+y)/2
def puissance(x, y):
    resultat = 1
    if x==0 and y<0:
         raise ValueError("entrée non valide")
    for _ in range(abs(int(y))):  
        resultat *= x
    if y < 0:
        resultat = 1 / resultat
    
    return resultat 