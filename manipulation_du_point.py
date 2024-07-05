import math

class Point:

    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    
    def deplacer(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
    def afficher(self):
        print(f"la coordonnees cartesienne est { self.x , self.y}")
    
    def saisir(self):
        self.x = float(input("entrez l'abscisse: "))
        self.y = float(input("entrez l'ordonne: "))

    def distance(self,x,y):
        dx = self.x - x
        dy = self.y - y
        dx_carre = pow(dx,2)
        dy_carre = pow(dy,2)
        somme = dx_carre + dy_carre
        racine = pow(somme,0.5)
        return racine

    def milieu(self,x,y):
        self.x = (self.x + x)/2
        self.y = (self.y + y)/2
    
    def scalaire(self,x,y):
        self.x = self.x * x
        self.y = self.y *y
        somme = self.x + self.y
        return somme
    
    

point1 = Point()
point2 = Point()
Point3 = Point()

point1.saisir()
point2.saisir()
Point3.saisir()

point1.deplacer(3,4)
point1.afficher()
print(f"la distance du premier point est de {point1.distance(2,2)}")

point2.milieu(5,7)
point2.afficher()

print(f"le scalire est {Point3.scalaire(3,2)}")


