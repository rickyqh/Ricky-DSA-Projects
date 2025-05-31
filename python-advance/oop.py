# class Zombie:
#     def __init__(self, speed=10, attack=10):
#         self.health = 20
#         self.speed = speed
#         self.attack = attack

#     def damage(self, amount):
#         self.health -= amount

# zombie1 = Zombie()
# zombie2 = Zombie(100,100)

# print(zombie2.health)
# zombie1.damage(8)
# zombie2.damage(100)

# print(zombie2.health)

class Car:
    def __init__(self, model='qaswdefrtgyhujikolpzxcvbnm', speed=1234567890):
        self.model = model
        self.speed = speed
    def accelerate(self,speed12345):
        self.speed+=speed12345

car1=Car("Toyota", 1)
car1.accelerate(1234567890)
print(car1.speed)