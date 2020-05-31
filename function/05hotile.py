class Hotel(object):
    def __init__(self,room=200,bf=15,cf=1.0):
        self.Room = room
        self.Bf = bf
        self.Cf = cf

    def calc_all(self,days=1):
        return (self.Room * self.Cf + self.Bf) * days


if __name__ == "__main__":
    m = Hotel(room=300,cf=0.8)
    print(m.calc_all(10))
    
