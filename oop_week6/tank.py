class Tank:
    def __init__(self,ชื่อ,กระสุน,พลังชีวิต):
        self.name = ชื่อ
        self.ammo = กระสุน
        self.hp = พลังชีวิต
    def add_ammo(self,กระสุน):
        if self.ammo >= 10:
            print("กระสุนยังเต็มอยู่")
        else :
            self.ammo+= กระสุน
            print("รีโหลด")
    def fire_ammo(self,enemy):
        self.ammo -=1
        enemy.hp -=1
tank1 = Tank("A1",10,5)
tank2 = Tank("A2",5,5)
tank3 = Tank("A3",9,5)
tank2.fire_ammo(tank3)
print(tank2.ammo)
print(tank3.hp)