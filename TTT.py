class Person():
    def __init__(self, name, health, professy, age, skill):
        self.name = name
        self.health = health
        self.professy = professy
        self.age = age
        self.skill = skill

    def get_damage(self, damage):
        self.health = self.health - damage
        return self.health

    def get_info(self):
        print(self.name, self.health)

class Zombies():
    def __init__(self, name, health, professy, age, skill):
        self.name = name
        self.health = health
        self.professy = professy
        self.age = age
        self.skill = skill
    
    def get_info_about_zombie(self):
        print(self.name, self.health, self.skill)

class nZombie(Zombies):
    def brains(self):
        print('Мозгии!')

ntZombie = Zombies('Зомби', 50, 'Съедать мозги', 500, 'Нет')
Zuumik = nZombie('Зумик', 50, 'Съедать мозги', 500, 'Нет')
Zuumik.get_info_about_zombie()
Zuumik.brains()

Bob = Person('Боб', 100, 'Штурмовик', 35, 'Неуязвимость')
Bob.get_info()
Bob.get_damage(40)
Bob.get_info()