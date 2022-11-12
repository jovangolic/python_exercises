#kreirati klasu Airplane sa poljima: name,health,ammo i metodom shoot.
#metod shoot kao parametar prihvata objekat klase airplane.
#u metodi shoot, po slucajnom izboru, oduzima se health jednom avionu i ammo drugom avionu(health duplo vise nego ammo).
#izvrsavati funkcionalnost, sve dok jednom od aviona health ili ammo ne padne ispod nule.

import random
class Airplane:
    def __init__(self,name,health,ammo):
        self.name = name
        self.health = health
        self.ammo = ammo
    def shoot(self,target):
        x=random.randint(0,10)
        target.health-=x*2
        self.ammo-=x
        return self.ammo < 0 or target.health < 0
il=Airplane('Ilyushin',100,100)
sp=Airplane('Spitfire',100,100)    
airplane = (il,sp)
print("round\tname\t\thealth/ammo\t:\t\tname\t\thealth/ammo")   
print('***********************************************************************************')     
runda=0
while True:
    runda+=1
    finished=False
    for i in range(len(airplane)):
        a1=airplane[abs(i-1)]
        a2=airplane[i]
        if a1.shoot(a2):
            finished=True
    print(f"{runda}\t{a1.name}\t{a1.health}/{a1.ammo}\t:\t{a2.name}\t{a2.health}/{a2.ammo}")
    if finished:
        break        