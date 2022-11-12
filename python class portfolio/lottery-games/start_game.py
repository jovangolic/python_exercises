import importlib,i_game,os
def start(): 
    while True:
        os.system("clear")
        game_name = input("Choose game (gamble,blackred): ")
        game_mod = None
        try:
            game_mod = importlib.import_module(game_name)
        except:
            print("Sorry, game does not exist")
            exit()

        game_class = getattr(game_mod,game_name)
        
        if not issubclass(game_class,i_game.Game):
            print("Sorry, game is not valid")

        game_obj = game_class()
        game_obj.pick()
        input("Press enter to play again")        