import i_game,random
class gamble(i_game.Game):
    def pick(self):
        num = random.randint(1,100)
        print(f" number: {num}")
        user = self.get_user("greater(1) /smaller(2) /equals(3)? ")
        newnum = random.randint(1,100)
        if user != 1 and user != 2 and user != 3:
            print('wrong entry!!')
            return
        if user == 1 and newnum > num:
            print(f"correct {newnum}") 
        elif user == 2 and newnum < num:
            print(f"correct {newnum}")
        elif user == 3 and newnum == num:
            print(f"correct {newnum}")
        else:
            print(f"incorrect {newnum}")
