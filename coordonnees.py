import csv

crd = []
with open ('coord.csv', newline='') as fichier:
    lect = csv.reader(fichier, delimiter=",")
    for lgn in lect :
        crd.append((lgn[1],lgn[2])) #tableau de tuple (latitude,longitude)
crd.pop(0)
print(crd)


def est_dans_polygone(point, polygone):
    x, y = point
    intersections = 0
    n = len(polygone)

    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]  # Boucle sur les arêtes du polygone

        # Vérifie si la demi-droite croise l'arête
        if y1 <= y < y2 or y2 <= y < y1:
            # Calcul de l'abscisse de l'intersection
            x_inter = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_inter:
                intersections += 1
                
    return intersections % 2 == 1


if est_dans_polygone(point, polygone):
    print("Le point est à l'intérieur du polygone.")
else:
    print("Le point est à l'extérieur du polygone.")
