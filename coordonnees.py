import csv

crd = []
with open ('coord.csv', newline='') as fichier:
    lect = csv.reader(fichier, delimiter=",")
    for lgn in lect :
        crd.append((lgn[1],lgn[2])) #tableau de tuple (latitude,longitude)
crd.pop(0)
print(crd)

def droite_cont(tab):
    ans = []
    for i in range (len(tab)-1):
        eq = 
