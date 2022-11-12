#kreirati klase Team,Score i Match. Klasa Team sadrzi polje,naziv tima.
#klasa Score sadrzi polja: home and away u kojima se nalazi rezultat meca.
#klasa Match sadrzi polja: home(objekat klase Team), away(objekat klase Team),minute(trenutni minut utakmice)
# i score(trenutni rezultat).
#klasa Match sadrzi metod start kojim zapocinje utakmica. Tokom trajanja utakmice, menjaju se rezultati,
#po slucajnom izboru i prikazuju na izlazu.Utakmica je gotova kada broj minuta dodje do 90.

import random,time,os
class Team:
    def __init__(self,name):
        self.name = name
class Score:
    home = 0
    away = 0
class Match:
    def __init__(self,t1,t2):
        self.home = t1
        self.away = t2
        self.minut = 0
        self.score = Score()
    def getGoals(self):
        return random.randint(1,10)==5, random.randint(1,10)==5
    def start(self):
        self.minut = 0
        while True:
            os.system('cls')
            print(f"{self.home.name} vs {self.away.name}")
            g1,g2 = self.getGoals()
            self.score.home +=1 if g1 else 0
            self.score.away +=1 if g2 else 0
            self.print_score()
            self.minut +=1
            time.sleep(0.2)
            if self.minut > 90:
                print('match over')
                exit()
    def print_score(self):
        print(f"{self.score.home} - {self.score.away} {self.minut} minute")   
t1=Team('Arsenal')
t2=Team('Tottenham')
match = Match(t1,t2)
match.start()             
