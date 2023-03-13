class SuperHero:
    people='people'

    def __init__(self, name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def names(self):
        return self.name

    def hp2(self):
        return self.health_points * self.health_points

    def __str__(self):
        return f'Его прозвище {self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Жетиген', 'Жека', 'Сила пять камней', 999999 ,'Я сама не отвратимость...' )

print(hero.names())
print(hero.hp2())
print(hero)
print(hero.__len__())

class AirHero(SuperHero):
    air = "air"

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp2(self):
        self.fly = True
        return self.health_points **2
    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


class EarthHero(SuperHero):
    earth = "earth"

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp2(self):
        self.fly = True
        return self.health_points ** 2

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')



thor = AirHero('thor', 'bog', 'grom', 200, 'хз', damage=300)
cap = EarthHero('cap', 'pon', 'hello', 150, 'ladno', damage=100)

print(thor.hp2())
thor.fly_sky()
print(cap.hp2())
cap.fly_sky()


class Villian(AirHero):
    SuperHero.people = 'monster'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_X(self):...


    def crit(self, hero):
        return self.damage **2

tanos = Villian('tanos', 'tanka', 'kamni', 900, 'pon')
print(Villian.crit(tanos, thor))
print(Villian.crit(tanos, cap))
