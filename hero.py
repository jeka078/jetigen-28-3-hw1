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




