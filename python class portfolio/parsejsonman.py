#kreirati 2 klase.Klasu UserPoint i klasu UserPosition.
#u aplikaciju u intervalima stize sledeci string koji predstavlja trenutne pozicije igraca
#[{id:10,x:10,y:20},{id:5,x:30,y:40},{id:2,x:2,y:7}]
#potrebno je izvicu smislene podatke iz dobijenog stringa i smestiti ih u odgovarajuca polja postojecih klasa
#(objekata) a zatim sve objekte smestiti u listu.

class UserPoint:
    x = 0.0
    y = 0.0
class UserPosition:
    userid = 0
    userpoint = None
    @staticmethod
    def parse_pos(data):
        res = UserPosition()
        arr = data.split(",")
        res.userid = arr[0].split(":")[1]
        res.userpoint = UserPoint()
        res.userpoint.x = arr[1].split(":")[1]
        res.userpoint.y = arr[2].split(":")[1]
        return res
    @staticmethod    
    def parse_position(data):
        res = []
        data = data.replace("[{","")
        data = data.replace("}]","")
        data = data.split("},{")
        for pos in data:
            user_position = UserPosition().parse_pos(pos)
            res.append(user_position)
        return res         
    def __str__(self):
        return f"userid: {self.userid} x: {self.userpoint.x} y: {self.userpoint.y}"    
data = "[{'id':10,'x':10,'y':20},{'id':5,'x':30,'y':40},{'id':2,'x':2,'y':7}]"    
positions = UserPosition().parse_position(data)
for pos in positions:
    print(pos)    