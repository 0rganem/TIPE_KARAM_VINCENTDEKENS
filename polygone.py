class polygone:
    def __init__(self,pt,coord):
        self.pt = pt
        self.coord = coord

    def triangulation(self):
        #créer des triangles à l'intérieur du polynome
        triangles = []
        for i in range (1,self.pt-1):
            triangles[i] = [self.coord[0],self.coord[i],self.coord[i+1]]


class triangle:
    def __init__(self,c1,c2,c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.air = (c1[0]*(c2[1]-c3[1])+c2[0]*(c3[1]-c1[1])+c3[0]*(c1[1]-c2[1]))/2
        

    def baricentre(self,x,y):
        
