#kreirati klase Bankomat i Card. Klasa Card treba da ima polje za naziv i stanje.
#Klasa Bankomat treba da ima polje card(objekat klase Card) i metode set_card i withdraw.
#metod set_card postavlja karticu u bankomat.Metod withdraw, skida odredjenu sumu sa kartice.
#Ukoliko ne postoji dovoljno sredstava ili kartica nije u bankomatu, metod withdraw prijavljuje gresku.

class Card:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
class Bankomat:
    def __init__(self):
        self.card = None
    def set_card(self,value):
        self.card = value
    def withdraw(self,amount):
        if self.card:
            if self.card.balance > amount:
                self.card.balance-=amount
                print(f"success, new balance: {self.card.balance}")
            else:
                print('not enough funds')    
        else:
            print('card not set')   
b=Bankomat()                 
card = Card('Mastercard',10)
b.set_card(card)
b.withdraw(2)            