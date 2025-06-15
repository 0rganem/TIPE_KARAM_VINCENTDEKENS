import csv

crd = []
with open ('crd.csv', newline='') as fichier:
    lect = csv.reader(fichier, delimiter=",")
    next(lect) #ne pas prendre le titre
    for lgn in lect :
		#tableau:latitude,longitude
        crd.append((float(lgn[1]),float(lgn[2]))) 



def est_dans_polygone(point, polygone):
    x, y = point #coordonnées du point
    intersections = 0
    n = len(polygone)

    for i in range(n):
       x1, y1 = polygone[i]
       x2, y2 = polygone[(i + 1) % n] #définie les aretes
       if y1 <= y < y2 or y2 <= y < y1:
            # Calcul de l'abscisse de l'intersection
           x_inter = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
           if x < x_inter:
               intersections += 1
                
    return intersections % 2 == 1

point = (44833.361,-572.19)
#point = (3,3)
cr = [(-1,1),(1,5),(2,4),(5,5),(5,1)]


if est_dans_polygone(point, crd):
    print("Le point est à l'intérieur du polygone.")
else:
    print("Le point est à l'extérieur du polygone.")
