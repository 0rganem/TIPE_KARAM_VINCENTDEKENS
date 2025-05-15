class polygone:
    def __init__(self,pt,coord):
        self.pt = pt #tableau des sommets du polygone
        self.coord = coord #tableau des coord

    def triangulation(self):
        #créer des triangles à l'intérieur du polynome
        triangles = []
        for i in range (1,len(self.pt-1)):
            triangles[i] = [self.coord[0],self.coord[i],self.coord[i+1]]


class triangle:
    def __init__(self,c1,c2,c3):
        self.c1 = c1 #tuple des coordonnées de c1
        self.c2 = c2
        self.c3 = c3
        self.air = (c1[0]*(c2[1]-c3[1])+c2[0]*(c3[1]-c1[1])+c3[0]*(c1[1]-c2[1]))/2
        

    def pos_pt(self,s1,s2,pt):
        e = (s1[0] - pt[0])*(s2[1] - pt[1]) - (s1[1] - pt[1])*(s2[0] - pt[0])
        return e

    def is_in_tr(self,pt,tr):
        ans = True
        if (pos_pt(tr.c1,tr.c2,pt) < 0):
            ans = False
        else if (pos_pt(tr.c2,tr.c3,pt) < 0):
            ans = False
        else if (pos_pt(tr.c3,tr.c1,pt) < 0):
            ans =False
        return ans
        
        
