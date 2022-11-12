import abc
class Game(abc.ABC):
    @abc.abstractmethod
    def pick(self):
        pass
    def get_user(self,msg):
        while True:
            try:
                val = int(input(msg))
                return val
            except:
                print("enter only numeric values")    