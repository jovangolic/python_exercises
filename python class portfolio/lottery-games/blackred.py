import i_game,random
class blackred(i_game.Game):
    def pick(self):
        num = random.randint(1,100)
        user = self.get_user("Red (1) / Black (2)? ")
        if user != 1 and user != 2:
            print('wrong input!!')
            return
        if user == 1 and num >= 50:
            print("correct red")
        elif user == 2 and num < 50:
            print("correct black")
        else:
            msg = "Black" if num < 50 else 'Red'
            print(f"incorrect {msg}")  
                    