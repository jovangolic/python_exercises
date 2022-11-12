#kreirati aplikaciju bingo.Aplikacija prihvata imena korisnika i brojeve sve dok postoji unos.
#aplikacija zamislja pet od N brojeva i prikazije ih na izlazu.
#aplikacija prikazuje koji su korisnici pogodili koje brojeve(ukoliko postoje pogoci)
#ukoliko neki korisnik pogodi sve brojeve, na izlazu se ispisuje poruka BINGO.

import random,time,os
class Ticket:
    def __init__(self,name,numbers):
        self.name = name
        self.numbers = numbers
class Bingo:
    def __init__(self):
        self.round = 0
        self.tickets = []
        self.numbers = []
    def enter_nums(self):
        while True:
            print('entering ticket: ')
            user = input('your name:  ')
            nums = input('numbers (x,y,z..):  ')
            if not user or not nums:
                print('no tickets entered')
                break
            else:
                self.tickets.append(Ticket(user,list(map(int,nums.split(",")))))   
    def check_result(self):
        winner = False
        for ticket in self.tickets:
            presek = []
            for num in self.numbers:
                if num in ticket.numbers:
                    presek.append(num)
            if len(presek)>0:
                winner = True
                if len(presek) == len(self.numbers):
                    print(f"user {ticket.name} has BINGO")
                else:
                    print(f"user {ticket.name} hit number: {presek}")
        if not winner:
            print("we don't have winner for this round")     
    def start(self):
        self.round=0
        while True:
            os.system('cls')
            self.round+=1
            print(f"round: {self.round}")
            self.numbers.clear()
            self.tickets.clear()
            self.enter_nums()
            self.numbers = random.sample(range(1,11),5)
            print('starting draw....')
            for i in range(5):
                time.sleep(1)
                print(self.numbers[i],end=" ")
            print()
            self.check_result()
            time.sleep(10)
b = Bingo()
b.start()                



