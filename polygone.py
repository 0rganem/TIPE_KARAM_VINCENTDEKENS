class Polygone:
    def __init__(self,pt,coord):
        self.pt = pt #tableau des sommets du polygone
        self.coord = coord #tableau des coord

    def triangulation(self):
        #créer des triangles à l'intérieur du polynome
        triangles = []
        for i in range (1,len(self.pt-1)):
            triangles[i] = [self.coord[0],self.coord[i],self.coord[i+1]]


class Triangle:
    def __init__(self,c1,c2,c3):
        self.c1 = c1 #tuple des coordonnées de c1
        self.c2 = c2
        self.c3 = c3
        self.air = (c1[0]*(c2[1]-c3[1])+c2[0]*(c3[1]-c1[1])+c3[0]*(c1[1]-c2[1]))/2
        

    def pos_pt(self,s1,s2,pt):
        e = (s1[0] - pt[0])*(s2[1] - pt[1]) - (s1[1] - pt[1])*(s2[0] - pt[0])
        return e

    def is_in_tr(self,pt):
        ans = True
        if (self.pos_pt(self.c1,self.c2,pt) < 0):
            ans = False
        elif (self.pos_pt(self.c2,self.c3,pt) < 0):
            ans = False
        elif (self.pos_pt(ssselfff.c3,self.c1,pt) < 0):
            ans =False
        return ans
        
def test() :
    tr= Triangle((2,2),(3,6),(6,5))
    rslt = tr.is_in_tr((4,4))
    print(rslt)

test()
