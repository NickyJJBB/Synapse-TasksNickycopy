import random

class ChessPlayer:
    def __init__(self,name,age,ELO,Tenacity,isBoring):
        self.name=name
        self.age=age
        self.ELO=ELO
        self.Tenacity=Tenacity
        self.isBoring=isBoring
        self.score=0

c1=ChessPlayer("Courage of the cowardly dog",25,1000.39,1000,False)
c2=ChessPlayer("Princess Peach",23,945.65,50,True)
c3=ChessPlayer("Walter White",50,1650.73,750,False)
c4=ChessPlayer("Rory Gilmore",16,1700.87,500,False)
c5=ChessPlayer("Anthony Fantano",37,1400.45,400,True)
c6=ChessPlayer("Beth Harmon",20,2500.34,150,False)

a=[c1,c2,c3,c4,c5,c6]

def simulateMatch(p1,p2):
    if (p1.ELO-p2.ELO)>100:
        p1.score+=1

    if (p2.ELO-p1.ELO)>100:
        p2.score+=1

    if (p1.isBoring or p2.isBoring) and (abs(p1.ELO-p2.ELO)<100):
        p1.score+=0.5
        p2.score+=0.5
    elif 100>=(p1.ELO-p2.ELO)>=50:
        n=random.randint(1,10)
        t=n*p2.Tenacity
        if t>p1.ELO:
            p2.score+=1
        else:
            p1.score+=1
    elif 100>=(p2.ELO-p1.ELO)>=50:
        n=random.randint(1,10)
        t=n*p1.Tenacity
        if t>p2.ELO:
            p1.score+=1
        else:
            p2.score+=1
    elif abs(p1.ELO-p2.ELO)<50:
        if p1.Tenacity>p2.Tenacity:
            p1.score+=1
        else:
            p2.score+=1

for i in range(6):
    for j in range(6):
        if i!=j:
            simulateMatch(a[i],a[j])

max=a[0].score
wname=""
print("The final results are:")
for l in range(6):
    if max<a[l].score:
        max=a[l].score
        wname=a[l].name
    print(a[l].name," - ",a[l].score)

print("The winner of the tournament is",wname,"with a score of",max)