import random,math,enum,time
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class PlayerType(enum.Enum):
    Person = 1
    Computer = 2        
class GameStates(enum.Enum):
    Uninitialized = 1
    Running = 2
    Finished = 3
class Game:
    def __init__(self,matrix_size):
        self.gamestate = GameStates.Uninitialized
        self.trajectory = []
        self.matrix_size = matrix_size
        self.shoots = 0
        self.user = None
        self.computer = None
    def add_player(self,ptype,x=0,y=0):
        if ptype == PlayerType.Person:
            self.user = Point(x,y)
        else:
            self.computer = Point(random.randint(1,self.matrix_size-2),random.randint(1,self.matrix_size-2))
            self.gamestate = GameStates.Running    
    def reset(self):
        self.shoots = 0
        self.trajectory.clear()
        self.gamestate = GameStates.Uninitialized
    def shoot(self,angle,trgt):
        source = None
        target = None
        if trgt == PlayerType.Computer:
            self.shoots += 1
            source = self.user
            target = self.computer
        else:
            source = self.computer
            target = self.user
        radians = math.radians(angle)
        speed = 1
        x = source.x
        y = source.y
        self.trajectory.clear()
        self.trajectory.append(Point(int(x),int(y))) 
        counter = 0
        while True:
            x+=speed*math.cos(radians)
            y+=speed*math.sin(radians)
            if (int(x) == target.x and int(y) == target.y):
                self.gamestate = GameStates.Finished
                return True
            if int(x)<=0 or int(x)>self.matrix_size or int(y)<0 or int(y)>self.matrix_size:
                return False
            self.trajectory.append(Point(int(x),int(y)))                
    def draw(self):
        c = range(self.matrix_size)
        for h in c:
            for w in c:
                if self.user and h == self.user.y and w == self.user.x:
                    print('U',end="")
                elif self.computer and h == self.computer.y and w == self.computer.x:
                    print('C',end="") 
                else:
                    if h == 0 or h == self.matrix_size-1 or w == 0 or w == self.matrix_size-1:
                        print('O',end="")
                    else:
                        point_draw = True
                        for i in self.trajectory:
                            if i.x == w and i.y == h:
                                print('*',end="")
                                point_draw = False
                        if point_draw:
                            print(" ",end="")
            print()                               
gameplay = Game(20)
while True:
    plx = int(input('enter position x: '))
    ply = int(input('enter position y: '))
    gameplay.add_player(PlayerType.Person,plx,ply) 
    gameplay.add_player(PlayerType.Computer)
    gameplay.draw()
    while True:
        angle = int(input('enter angle: '))
        hit = gameplay.shoot(angle,PlayerType.Computer)
        gameplay.draw()
        if hit:
            print('you HIT computer')
        else:
            print("You missed.Computer's turn") 
            time.sleep(2)
            compangle = random.randint(0,360)
            hit = gameplay.shoot(compangle,PlayerType.Person)
            gameplay.draw()
            print(f"computer angle {compangle}")
            if hit:
                print('computer HIT you,you lose!!!')
        if gameplay.gamestate == GameStates.Finished:
            break
    print("******************************")
    print(f"total shots\t{gameplay.shoots}")
    print("*******************************")
    another_game = input('another game (y/n)?')
    if another_game == 'n':
        break
    else:
        gameplay.reset()                                
